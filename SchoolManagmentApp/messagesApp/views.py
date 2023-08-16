from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .forms import FullEmailForm, ShortEmailForm
from .models import Message


@login_required
def get_inbox(request):
    if request.method == "GET":
        inbox_messages = Message.objects.filter(
            receiver=request.user.profile, is_delete_receiver=False
        ).order_by("-id")
        inbox_messages_not_read = Message.objects.filter(
            receiver=request.user.profile,
            is_delete_receiver=False,
            is_read_receiver=False,
        ).count()
        for email in inbox_messages:
            email.is_sender = False
        paginator = Paginator(inbox_messages, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            "page_obj": page_obj,
            "not_read": inbox_messages_not_read,
            "view_name": "Inbox",
        }
        return render(request, "inbox.html", context)


@login_required
def get_outbox(request):
    if request.method == "GET":
        outbox_messages = Message.objects.filter(
            sender=request.user.profile, is_delete_sender=False
        ).order_by("-date")
        inbox_messages_not_read = Message.objects.filter(
            receiver=request.user.profile,
            is_delete_receiver=False,
            is_read_receiver=False,
        ).count()
        for email in outbox_messages:
            email.is_sender = True
        paginator = Paginator(outbox_messages, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            "page_obj": page_obj,
            "not_read": inbox_messages_not_read,
            "view_name": "Outbox",
        }
        return render(request, "outbox.html", context)


@login_required
def get_important(request):
    if request.method == "GET":
        inbox_messages = Message.objects.filter(
            receiver=request.user.profile, is_delete_receiver=False, 
            is_important=True
        ).order_by("-date")
        inbox_messages_not_read = Message.objects.filter(
            receiver=request.user.profile,
            is_delete_receiver=False,
            is_read_receiver=False,
        ).count()
        for email in inbox_messages:
            email.is_sender = False
        paginator = Paginator(inbox_messages, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            "page_obj": page_obj,
            "not_read": inbox_messages_not_read,
            "view_name": "Important emails",
        }
        return render(request, "important.html", context)


@login_required
def delete_email(request, id):
    user = request.user.profile
    message = Message.objects.get(id=id)

    if message.receiver.id == user.id:
        if message.is_important:
            messages.error(request, "You cannot delete important message.")
            return redirect("inbox")
        if message.is_delete_sender == True:
            message.delete()
        else:
            message.is_delete_receiver = True
            message.save()

        return redirect("inbox")

    elif message.sender.id == user.id:
        if message.is_delete_receiver == True:
            message.delete()
        else:
            message.is_delete_sender = True
            message.save()
        return redirect("outbox")
    else:
        return render(request, "403.html")


@login_required
def email_is_important(request, id):
    user = request.user.profile
    message = Message.objects.get(id=id)
    source = request.GET.get("source")

    if source == "important":
        if message.receiver.id == user.id:
            if message.is_important:
                message.is_important = False
            else:
                message.is_important = True
            message.save()
            return redirect("important")
        else:
            return render(request, "403.html")

    if source == "email_detail":
        if message.receiver.id == user.id:
            if message.is_important:
                message.is_important = False
            else:
                message.is_important = True
            message.save()
            return redirect(reverse("email_detail", args=[id]))
        else:
            return render(request, "403.html")
    else:
        if message.receiver.id == user.id:
            if message.is_important:
                message.is_important = False
            else:
                message.is_important = True
            message.save()
            return redirect("inbox")
        else:
            return render(request, "403.html")


@login_required
def get_email_details(request, id):
    if request.method == "POST":
        previous_email = get_object_or_404(Message, id=id)
        form = ShortEmailForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.receiver = previous_email.sender
            email.title = f"Re: {previous_email.title}"
            email.sender = request.user.profile
            email.is_read_receiver = False
            email.is_read_sender = True
            email.is_delete_receiver = False
            email.is_delete_sender = False
            email.save()
            messages.success(request, "Email has been sent.")
            return redirect("inbox")
        else:
            messages.error(request, "Error occurs, email has not been sent.")
            return redirect("inbox")

    else:
        user = request.user.profile
        email = get_object_or_404(Message, id=id)
        if email.receiver.id == user.id:
            form = ShortEmailForm()
            inbox_messages_not_read = Message.objects.filter(
                receiver=request.user.profile,
                is_delete_receiver=False,
                is_read_receiver=False,
            ).count()
            email = get_object_or_404(Message, id=id)
            email.is_read_receiver = True
            email.save()
            context = {
                "email": email,
                "not_read": inbox_messages_not_read,
                "form": form,
            }
            return render(request, "email_details.html", context)
        else:
            return render(request, "403.html")


@login_required
def get_sent_email_details(request, id):
    if request.method == "GET":
        user = request.user.profile
        email = get_object_or_404(Message, id=id)
        if email.sender.id == user.id:
            form = ShortEmailForm()
            inbox_messages_not_read = Message.objects.filter(
                sender=request.user.profile,
                is_delete_sender=False,
                is_read_sender=False,
            ).count()
            context = {
                "email": email,
                "not_read": inbox_messages_not_read,
                "form": form,
            }
            return render(request, "send_email_details.html", context)
        else:
            return render(request, "403.html")


@login_required
def create_email(request):
    if request.method == "POST":
        form = FullEmailForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.sender = request.user.profile
            email.is_read_receiver = False
            email.is_read_sender = True
            email.is_delete_receiver = False
            email.is_delete_sender = False
            email.save()
            messages.success(request, "Email has been sent.")
            return redirect("inbox")
        else:
            messages.error(request, "Error occurs, email has not been sent.")
            return redirect("inbox")

    else:
        form = FullEmailForm()
        inbox_messages_not_read = Message.objects.filter(
            receiver=request.user.profile,
            is_delete_receiver=False,
            is_read_receiver=False,
        ).count()
        context = {
            "not_read": inbox_messages_not_read,
            "form": form,
        }
        return render(request, "send_email.html", context)
