from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import cache_page
from eventApp.models import Subject
from gradesApp.forms import GradesForm, SemesterForm
from usersApp.models import ClassUnit, Parent, Student
from .decorators.auth_decorators import teacher_and_staff_only
from .forms import GradesForm
from .models import Grades, Semester


@login_required
def view_grades(request, semester=None):
    scope = 15
    kids_grades = {}
    subjects = Subject.objects.all()

    if not semester:
        semester = Semester.objects.last()
    else:
        try:
            semester = get_object_or_404(Semester, id=semester)
        except:
            semester = Semester.objects.last()

    if request.user.profile.account_type == "Student":
        student = get_object_or_404(Student, user=request.user.profile)

        grades = {
            subject: Grades.objects.filter(
                student=student, subject=subject, semester=semester
            )
            for subject in subjects
        }

        kids_grades[student] = grades

        for subject_grades in grades.values():
            max_length = len(subject_grades)
            if max_length > scope:
                scope = max_length

    elif request.user.profile.account_type == "Parent":
        parent = get_object_or_404(Parent, user=request.user.profile)
        kids = parent.children.all()

        for kid in kids:
            grades = {
                subject: Grades.objects.filter(
                    student=kid, subject=subject, semester=semester
                )
                for subject in subjects
            }

            kids_grades[kid] = grades

            for subject_grades in grades.values():
                max_length = len(subject_grades)
                if max_length > scope:
                    scope = max_length
    else:
        messages.error(
            request,
            "Sorry, you do not have permission to access this \
                page or the provided URL data is incorrect.",
        )
        return redirect("home")

    if request.method == "GET":
        form = SemesterForm()

        context = {
            "subjects": subjects,
            "grades": grades,
            "form": form,
            "iterateover": range(scope),
            "kids_grades": kids_grades,
        }

        return render(request, "view_grades.html", context)
    else:
        form = SemesterForm(request.POST)

        if form.is_valid():
            semester = form.cleaned_data["semester"].id
            return redirect("view_grades", semester=semester)

        else:
            return redirect(".")


@login_required
@teacher_and_staff_only
@cache_page(60 * 15)
def view_grades_teacher(request):
    if request.method == "GET":
        form = GradesForm()
        return render(request, "view_grades_teacher_menu.html", {"form": form})

    else:
        form = GradesForm(request.POST)
        if form.is_valid():
            class_unit_id = form.cleaned_data["class_unit"].id
            subject_id = form.cleaned_data["subject"].id
            semester_id = form.cleaned_data["semester"].id

            return redirect(
                "view_grades_teacher_final",
                semester=semester_id,
                class_unit=class_unit_id,
                subject=subject_id,
            )
        else:
            messages.error(
                request, "An error occurred. Check the  \
                    correctness of the data and try again."
            )
            return render(request, "view_grades_teacher_menu.html",
                        {"form": form})


@login_required
@teacher_and_staff_only
@cache_page(60 * 15)
def view_grades_teacher_final(request, semester, class_unit, subject):
    try:
        semester_obj = get_object_or_404(Semester, id=semester)
        class_unit_obj = get_object_or_404(ClassUnit, id=class_unit)
        subject_obj = get_object_or_404(Subject, id=subject)
    except:
        messages.error(
            request,
            "Sorry, you do not have permission to access this page, or \
                the provided URL data is incorrect.",
        )
        return redirect("home")

    if request.method == "GET":
        scope = 15
        kids_grades = {}
        students = class_unit_obj.students_in_class.all()

        for student in students:
            grades = Grades.objects.filter(
                student=student, subject=subject_obj, semester=semester_obj
            )
            kids_grades[student] = grades

            max_length = grades.count()

            if max_length > scope:
                scope = max_length

        form = GradesForm()
        context = {
            "class_unit": class_unit_obj,
            "subject": subject_obj,
            "form": form,
            "iterateover": range(scope),
            "kids_grades": kids_grades,
        }

        return render(request, "view_grades_teacher.html", context)

    else:
        form = GradesForm(request.POST)

        if form.is_valid():
            class_unit_id = form.cleaned_data["class_unit"].id
            subject_id = form.cleaned_data["subject"].id
            semester_id = form.cleaned_data["semester"].id

            return redirect(
                "view_grades_teacher_final",
                semester=semester_id,
                class_unit=class_unit_id,
                subject=subject_id,
            )
        else:
            messages.error(
                request, "Wystąpił błąd. Sprawdź poprawność danych i \
                    spróbuj ponownie."
            )
