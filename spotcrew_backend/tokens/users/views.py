from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from tokens.users.activation import account_activation_token
from users.models import User


# TODO class view
@api_view(['GET'])
@parser_classes((JSONParser,))
def activate(request, uidb64, token, *args, **kwargs):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return Response({"msg": 'Thank you for your email confirmation. Now you can login your account.'})
    else:
        return Response({"msg": 'Activation link is invalid!'}, status=status.HTTP_400_BAD_REQUEST)
