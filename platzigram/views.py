from django.http import HttpResponse

# Test view for checking the server running OK. This section is not part of the app
def hello_world(request):
    return HttpResponse('Hello, my beautiful World!')
