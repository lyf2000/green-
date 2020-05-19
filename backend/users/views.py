import datetime

from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView as passwordResetConfirmView, \
    PasswordResetDoneView as passwordResetDoneView, PasswordResetCompleteView as passwordResetCompleteView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.timezone import make_aware

from users.forms import SignupForm, PasswordRestForm, SetPasswordForm
from users.models import User
from users.tasks import send_register_confirmation_email
from users.tokens import account_activation_token


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            domain = current_site.domain
            to_email = form.cleaned_data.get('email')
            send_register_confirmation_email.delay(user.pk, domain, to_email)

            return HttpResponse('Please confirm your email address (if it exists) to complete the registration')
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
    success_url = reverse_lazy('users:password_reset_done')

class PasswordResetConfirmView(passwordResetConfirmView):
    form_class = SetPasswordForm
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('users:password_reset_complete')


class PasswordResetDoneView(passwordResetDoneView):
    template_name = 'users/password_reset_done.html'

class PasswordResetCompleteView(passwordResetCompleteView):
    template_name = 'users/password_reset_complete.html'