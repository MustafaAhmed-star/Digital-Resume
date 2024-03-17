from django.contrib.auth.models import User


def project_context(request):
    context = {
        'me':User.object.first(),
    
    
    }
    
    return context