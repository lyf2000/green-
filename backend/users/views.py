from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView as passwordResetConfirmView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from users.forms import SignupForm, PasswordRestForm, SetPasswordForm
from users.models import User
from users.tokens import account_activation_token


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('users/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })


            to_email = form.cleaned_data.get('email')
            msg = EmailMultiAlternatives(mail_subject, '', 'from_email', [to_email])
            msg.attach_alternative(message, "text/html")
            msg.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def reset(request):
    if request.method == 'POST':
        form = PasswordRestForm(request.POST)
        if form.is_valid():
            to_email = [form.cleaned_data['email']]

            # current_site = get_current_site(request)
            # user = request.user
            # mail_subject = 'Activate your blog account.'
            # message = render_to_string('users/acc_active_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            # })
            #
            # to_email = form.cleaned_data.get('email')
            # msg = EmailMultiAlternatives(mail_subject, '', 'from_email', [to_email])
            # msg.attach_alternative(message, "text/html")

            form.save(html_email_template_name='users/password_reset_email.html', request=request)
    form = PasswordRestForm()
    return render(request, 'users/password_reset.html', {'form': form})

class Reset(PasswordResetView):
    form_class = PasswordRestForm
    template_name = 'users/password_reset.html'
    html_email_template_name = 'users/password_reset_email.html'

class PasswordResetConfirmView(passwordResetConfirmView):
    form_class = SetPasswordForm
    template_name = 'users/password_reset_confirm.html'
