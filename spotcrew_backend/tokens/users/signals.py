from django.core.mail import EmailMessage
from django.dispatch import receiver
from django.template.loader import render_to_string
from django_rest_passwordreset.signals import reset_password_token_created
from django.urls import reverse


@receiver(reset_password_token_created)
def password_reset_token_created(sender, reset_password_token, *args, **kwargs):
    mail_subject = 'Reset your password.'
    message = render_to_string('reset_password_email.html', {
        'username': reset_password_token.user.username,
        'token': reset_password_token.key
    })
    email = EmailMessage(
        mail_subject, message, to=[reset_password_token.user.email]
    )
    email.send()

    '''
        'reset_url': "{}?token={}".format(
            reverse('password_reset:reset-password-request'),
            reset_password_token.key
        )
        '''