from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseForbidden
# Create your views here.
import json


@csrf_exempt
def get_directory(request):
    directory = [{"key": "dev.test",
                  "server": "18.138.8.34"},
                 {"Key": "internal.test",
                  "server":  " "},
                 {"key": "external.test",
                  "server": " "}]
    return JsonResponse({"status": "ok", "result": json.dumps(directory)})
    pass

