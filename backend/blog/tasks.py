from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from blog.models import Meet


@shared_task
def remind_meets(meet_id):
    meet = Meet.objects.get(id=meet_id)
    mail_subject = 'MEETIIIING AAAAA.'
    for user in meet.participants.all():
        print(user)
        context = {
            'username': user.username,
            'meet_date': meet.meet_date.strftime('%d/%m/%Y %H:%M'),
        }
        send_message.delay('blog/meeting_remind.html', context, mail_subject, user.email)

@shared_task
def send_message(template_name, message_context, mail_subject, to_email):
    message = render_to_string(template_name, message_context)
    msg = EmailMultiAlternatives(mail_subject, '', '', [to_email])
    msg.attach_alternative(message, "text/html")
    msg.send()