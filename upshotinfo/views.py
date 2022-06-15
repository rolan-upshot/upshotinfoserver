from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseForbidden
# Create your views here.
import json


@csrf_exempt
def get_directory(request):
    directory = [{"key": "dev.test",
                  "server": "18.138.8.34"},
                 {"key": "internal.test",
                  "server":  "54.179.124.22"},
                 {"key": "ext.test",
                  "server": "18.142.65.252"},
                 {"key": "demo.test",
                  "server": "13.250.99.218"}]
    return JsonResponse({"status": "ok", "result": directory})
    pass

