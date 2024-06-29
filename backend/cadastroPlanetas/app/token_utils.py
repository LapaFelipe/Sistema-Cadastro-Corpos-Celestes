from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

def is_token_blacklisted(token):
    try:
        OutstandingToken.objects.get(token=token)
        return True  # Token encontrado na blacklist
    except OutstandingToken.DoesNotExist:
        return False  # Token não encontrado na blacklist