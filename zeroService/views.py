# from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# def index(request):
#     return HttpResponse(u"你好")


@csrf_exempt
def index(request):
    return JsonResponse({"result": 0, "msg": "success"})