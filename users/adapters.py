from allauth.account.adapter import DefaultAccountAdapter


class CustomUserAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        user = super().save_user(request, user, form, False)
        user.first_name =  request.data.get('first_name', '')
        user.last_name = request.data.get('last_name', '')
        user.department = request.data.get('department', '')
        user.role = request.data.get('role', '')
        user.save()
        return user

