from django.contrib.auth.models import User


class EmailAuthBackend(object):

    """
    Authenticate using email address.
    """
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            print('User.DoseNotExist')
            return None

    def get_user(self, user_id):
        try:
            User.objects.get(pk=user_id)
        except User.DoesNotExist:
            print('User.DoseNotExist')
            return None