from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from tokens.users.activation import account_activation_token
from django.core.mail import EmailMessage


def send_email(user):
    mail_subject = 'Activate your account.'
    message = render_to_string('activate_email.html', {
        'user': user,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
        'token': account_activation_token.make_token(user),
    })
    print(message)
    # TODO send email - add .env variables
    '''
    email = EmailMessage(
        mail_subject, message, to=[user.email]
    )
    email.send()
'''