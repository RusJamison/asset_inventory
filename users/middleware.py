from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


allowed_urls = [
        reverse('verification_pending'),
        reverse('account_login'),
        reverse('account_logout'),
        reverse('admin:index'),
        reverse('account_signup'),
    ]

class PreventUnverifiedUserMiddleware:
    """
    Middleware to prevent unverified users from accessing any view.
    """

    def __init__(self, get_response):
        self.get_response = get_response

 
    def __call__(self, request):
        # Check if the user is authenticated and not verified
        if request.user.is_authenticated and not request.user.is_verified:
            if request.path not in allowed_urls:
                messages.warning(request, "Your account is not verified. Please contact support.")
                return redirect('verification_pending')  # Redirect to a verification pending page or home

        response = self.get_response(request)
        return response
