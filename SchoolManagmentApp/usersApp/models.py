from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
# Users

class Profile(models.Model):
    TEACHER = "Teacher"
    PARENT = "Parent"
    STUDENT = "Student"
    TYPE_ACCOUNT_CHOICES = [
        (TEACHER, "Teacher"),
        (PARENT, "Parent"),
        (STUDENT, "Student"),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/avatars/', default='users/avatars/anonymous.png', blank=True)
    phone_number = models.CharField(max_length=9, blank=True, null=True)
    account_type = models.CharField(max_length=10, choices=TYPE_ACCOUNT_CHOICES, default=STUDENT)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} \'s profile'
        

class ClassUnit(models.Model):
    start_year = models.IntegerField(
        validators=[MinValueValidator(2023), ], default=2023
    )
    study_year = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(7)],
        default=1
    )
    letter_mark = models.CharField(
        max_length=1,
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')],
        null=False,
        blank=False
    )

    def __str__(self):
        return f"Class {self.study_year}{self.letter_mark}"

class Student(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='student', limit_choices_to={'account_type': 'Student'})
    klasa = models.OneToOneField(ClassUnit, models.DO_NOTHING, blank=False, null=False, related_name='students_in_class')

    def __str__(self):
        return f'{self.user.user.first_name} {self.user.user.last_name} - student'

class Parent(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='parent', limit_choices_to={'account_type': 'Parent'})
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='children')

class Teacher(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='teacher')
