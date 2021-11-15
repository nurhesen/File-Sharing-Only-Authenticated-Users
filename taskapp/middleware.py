from django.http import HttpResponseRedirect

from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse

class AuthRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('taskapp:create')) # or http response
        return None