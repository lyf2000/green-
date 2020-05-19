from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from users.tokens import account_activation_token

UserModel = get_user_model()

@shared_task
def send_register_confirmation_email(user_id, domain, to_email):
    user = UserModel.objects.get(id=user_id)
    mail_subject = 'Activate your blog account.'
    message = render_to_string('users/acc_active_email.html', {
        'user': user,
        'domain': domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })


    msg = EmailMultiAlternatives(mail_subject, '', 'from_email', [to_email])
    msg.attach_alternative(message, "text/html")
    msg.send()