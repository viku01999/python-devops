import django
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY='dev',
    ALLOWED_HOSTS=['*'],
)

django.setup()

def hello(request):
    return HttpResponse("Hello from Order Service!")

urlpatterns = [
    path('', hello),
]

if __name__ == "__main__":
    execute_from_command_line()
