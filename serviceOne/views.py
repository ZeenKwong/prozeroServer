from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request):
    # return JsonResponse({"result": 0, "msg": "success"})
    return JsonResponse({'say':'miss me'})
    # return render(request, 'test1/htmlTest.html')
