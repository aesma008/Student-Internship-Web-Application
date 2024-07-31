from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage

from django.contrib import messages
from django.contrib.auth import login, get_user_model, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.safestring import mark_safe

from .forms import RegisterForm
from .models import Profile
from .tokens import account_activation_token


def activate(request, uidb64, token):
    storage = messages.get_messages(request)
    for _ in storage:
        pass  # Iterate through and consume existing messages
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('login')


def activateEmail(request, user, to_email):
    storage = messages.get_messages(request)
    for _ in storage:
        pass  # Iterate through and consume existing messages
    mail_subject = "Activate your user account."
    message = render_to_string("collegehub/template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, mark_safe(f'Hello <b>{user}</b>, please check your <b>{to_email}</b> inbox to '
                                            f'complete'
                                            f'registration of your account. <b>Note:</b> Check your spam folder.'))
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')


def register(request):
    storage = messages.get_messages(request)
    for _ in storage:
        pass  # Iterate through and consume existing messages
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data['email'])
            # Create or update the profile with the university field
            Profile.objects.update_or_create(user=user, defaults={'university': form.cleaned_data.get('university')})
            return redirect('login')
        else:
            # Extract form errors
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = error_list[0]  # Assuming you want only the first error message for each field
    else:
        form = RegisterForm()
        errors = {}

    return render(request, 'collegehub/register.html', {'form': form, 'errors': errors})


def login_view(request):
    storage = messages.get_messages(request)
    for _ in storage:
        pass  # Iterate through and consume existing messages
    if request.method == 'POST':

        post_data = request.POST.copy()
        post_data['username'] = post_data.get('username', '').lower()

        form = AuthenticationForm(data=post_data)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Successfully Logged in.")
            return redirect('home')
        else:
            # Extract form errors
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = error_list[0]  # Assuming you want only the first error message for each field
    else:
        errors = {}
        form = AuthenticationForm()
    return render(request, 'collegehub/login.html', {'form': form, 'errors': errors})


@login_required(login_url="/login/")
def home_view(request):
    storage = messages.get_messages(request)
    for _ in storage:
        pass  # Iterate through and consume existing messages
    return render(request, 'collegehub/home.html')


def logout_view(request):
    storage = messages.get_messages(request)
    for _ in storage:
        pass  # Iterate through and consume existing messages
    # Clear any existing messages
    storage = messages.get_messages(request)
    for _ in storage:
        pass  # Iterate through and consume existing messages

    logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect('/login')


@login_required(login_url="/login/")
def settings_view(request):
    storage = messages.get_messages(request)
    for _ in storage:
        pass  # Iterate through and consume existing messages
    user = request.user
    if request.method == 'POST':
        university = request.POST.get('university')
        if user.profile.university != university:
            user.profile.university = university
            user.profile.save()
            messages.success(request, "Profile saved successfully.")
        else:
            messages.error(request, "Please make a change!")
    return render(request, 'collegehub/settings.html')


@login_required(login_url="/login/")
def password_reset_view(request):
    storage = messages.get_messages(request)
    for _ in storage:
        pass  # Iterate through and consume existing messages
    user = request.user
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        try:
            validate_password(password1, user)
            password1 = request.POST.get('password1')
            user.set_password(password1)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password updated successfully.")
            return redirect('settings')
        except ValidationError as e:
            messages.error(request, "<br>".join(e.messages))
    return render(request, 'collegehub/password_reset.html')
