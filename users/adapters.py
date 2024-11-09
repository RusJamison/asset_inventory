from allauth.account.adapter import DefaultAccountAdapter


class AccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        print("health facility ", data.get("health_facility"))
        heath_facility = data.get("health_facility")
        user.username = data.get("username")
        user.email = data.get("email")
        user.health_facility = heath_facility
        if "password1" in data:
            user.set_password(data.get("password1"))
        if commit:
            user.save()
        return user
