"""Platzigram middleware"""

# Django
from django.shortcuts import redirect
from django.urls import reverse


class CompleteProfileMiddleware:
    """Evaluates if profile is missing picture and biography, if so, takes the user to the profile page/view"""

    def __init__(self, get_response):
        """Initiate middleware, this is loaded by django when the server starts"""
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.profile_picture or not profile.biography:
                    if request.path not in [reverse('profile'), reverse('logout')]:
                        return redirect('profile')

        response = self.get_response(request)
        return response
