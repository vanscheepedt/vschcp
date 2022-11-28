from django.http import HttpRequest
from django.views import View


class Users(View):
    """
    View to manage users (authors):
    ** get -- retrieve the user;
    ** post -- create new user;
    ** put -- edit the user;
    ** delete -- remove the user;
    """
    def post(self):
        return
