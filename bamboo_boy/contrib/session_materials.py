from ..materials import Clump
from importlib import import_module
from django.contrib.auth import backends

try:
    from django.test.client import RequestFactory
    from django.contrib.auth import login
    from django.conf import settings
except ImportError:
    raise EnvironmentError("This module requires Django.")


class LoginClump(Clump):

    def __init__(self, obj, user=None, *args, **kwargs):
        self.user_to_login = user
        self.logged_in = False
        super(LoginClump, self).__init__(obj, *args, **kwargs)

    def deliver_canopy(self):
        if not self.logged_in:
            self.login()

        super(LoginClump, self).deliver_canopy()

    def retract_canopy(self):
        self.logged_in = False
        super(LoginClump, self).retract_canopy()

    def login(self):
        SessionStore = import_module(settings.SESSION_ENGINE).SessionStore
        sesh = SessionStore()
        sesh.save()  # To generate session_id

        # We'll need a request to call the login() function
        request = RequestFactory()
        request.session = sesh
        request.META = {}

        self.user_to_login.backend = 'django.contrib.auth.backends.ModelBackend'  # Cheat and make them appear authenticated.

        try:
            login(request, self.user_to_login)
        except AttributeError:
            raise TypeError("Need a User to login.  This can be specified in three ways: 1) set request.user 2) set the user_to_login attribute of your LoginClump 3) pass a User object to the with_canopy decorator")

        try:
            target = "%s:%s/" % (self.obj.server_thread.host, self.obj.server_thread.port)
            print "Target: %s" % target
            self.obj.wd.get(target)
        except AttributeError:
            raise TypeError("In order to build this canopy, the decorated class must have an attribute 'wd' (a WebDriver instance).  Please modify %s to include this." % self.obj)

        request.session.save()

        self.obj.wd.add_cookie({'name': settings.SESSION_COOKIE_NAME, 'value': sesh.session_key})
        self.logged_in = True
