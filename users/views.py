from django.shortcuts import render

# Create your views here.
def verification_pending(request):
    return render(request, 'users/verification.html',{})

