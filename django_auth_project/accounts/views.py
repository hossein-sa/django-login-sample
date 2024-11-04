from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


def home(request):
    # Render the home page
    return render(request, 'home.html')  # Assumes home.html is in the global templates directory


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'login.html')  # Assumes login.html is in the global templates directory


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()  # Create the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            # Authenticate and log in the user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Registration successful, but authentication failed. Please log in.')
        else:
            # Display form errors
            messages.error(request, 'Registration failed. Please check the form and try again.')
            print("Form errors:", form.errors)  # Optional: For debugging in the console

    else:
        form = UserCreationForm()

    return render(request, 'register.html',
                  {'form': form})  # Assumes register.html is in the global templates directory


def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            associated_users = User.objects.filter(email=email)

            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password_reset_email.txt"  # Ensure this template exists
                    context = {
                        "email": user.email,
                        'domain': 'localhost:8000',  # Update to your actual domain in production
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email_message = render_to_string(email_template_name, context)
                    send_mail(subject, email_message, 'admin@example.com', [user.email], fail_silently=False)
                messages.success(request, 'A password reset link has been sent to your email.')
            else:
                messages.error(request, 'No user is associated with this email address.')

            return redirect("password_reset_done")

    form = PasswordResetForm()
    return render(request, 'forgot_password.html',
                  {"form": form})  # Assumes forgot_password.html is in the global templates directory


def logout_view(request):
    logout(request)
    return redirect('home')  # Redirects to home after logout
