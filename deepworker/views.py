# views.py

from django.http import HttpResponse

def greeting(request):
    return HttpResponse("Hello Martin. 장고 아주 잘 돌아감 헤헷!")