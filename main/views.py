from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProjectForm
from .models import Project, Email
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    projects = Project.objects.all()[:6]
    context = {"projects": projects}

    return render(request, "home.html", context)


def filter_search(request):
    term = request.GET.get("filter_term", "all").strip().lower()

    projects = Project.objects.all()

    if term != "all" and term:
        projects = projects.filter(badges__icontains=term)

    return render(request, "partials/project_partial.html", {"projects": projects})


def search(request):
    term = (request.GET.get("term") or "").strip()

    projects = Project.objects.filter(title__icontains=term)
    print("Trigger Search")
    # Update Search Optimization Later Using Q
    if len(projects) == 0:
        return render(request, "partials/projects_notfound.html", {})

    return render(request, "partials/project_partial.html", {"projects": projects})


@login_required
def project_form(request):
    if request.method == "POST":
        form_instance = ProjectForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("form")

    form = ProjectForm()

    return render(request, "form.html", {"form": form})


def email(request):
    if request.method == "POST":
        name = request.POST.get("name")
        sender_email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        to_emails = ["sharushan0000@gmail.com", "sharushankumaresan11@gmail.com"]


        # Save the email detail to the database
        email_instance = Email(name=name, 
                               email=sender_email, 
                               subject=subject, 
                               message=message)
        
        email_instance.save()
        
        try:
            # Send an email
            send_mail(
                subject=subject,  # subject
                message=f"From : {sender_email} \n\n {message} \n",  # message
                from_email=settings.DEFAULT_FROM_EMAIL,  # from email
                recipient_list=to_emails,  # to email
            )
            messages.success(
                request,
                f"Thank you for reaching out, {name}. I have received your message and will respond within 24 hours.",
            )
        except Exception as e:
            messages.error(request, "Something Wrong ")

    return render(request, "sections/contact.html", {})
