import os
from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
# Set the default settings module for the 'wsgi' command.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproje.settings')

# Get the WSGI application.
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'users.settings')
>>>>>>> origin/main
application = get_wsgi_application()
