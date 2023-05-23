from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseForbidden, HttpRequest, HttpResponseBadRequest
from typing import Union
# Create your views here.
import json
import requests

@csrf_exempt
def get_directory(request):
    directory = [{"key": "dev.test",
                  "server": "18.138.8.34"},
                 {"key": "internal.test",
                  "server":  "54.179.124.22"},
                 {"key": "upshot.global",
                  "server":  "54.179.124.22"},
                 {"key": "upshot-partners.com",
                  "server": "18.138.251.23"},
                 {"key": "upshot.technology",
                  "server": "18.138.251.23"},
                 {"key": "upshot.demo",
                  "server": "18.142.177.244"},
                 {"key": "demo.com",
                  "server": "18.142.177.244"},
                 {"key": "external.test",
                  "server": "18.142.65.252"},
                 ]
    return JsonResponse({"status": "ok", "result": directory})
    pass


@csrf_exempt
def find_server_for_mobile(request: HttpRequest) -> Union[JsonResponse, HttpResponseBadRequest]:
    directory = [{"key": "dev.test",
                  "server": "18.138.8.34"},
                 {"key": "internal.test",
                  "server":  "54.179.124.22"},
                 {"key": "upshot.global",
                  "server":  "54.179.124.22"},
                 {"key": "upshot-partners.com",
                  "server": "18.138.251.23"},
                 {"key": "upshot.technology",
                  "server": "18.138.251.23"},
                 {"key": "upshot.demo",
                  "server": "18.142.177.244"},
                 {"key": "demo.com",
                  "server": "18.142.177.244"},
                 {"key": "external.test",
                  "server": "18.142.65.252"},
                 ]
    input_data = request.body
    input_as_json = json.loads(input_data)
    servers = [obj["server"] for obj in directory]
    servers = list(set(servers))
    phone_number = input_as_json.get("phone_number", None)

    body = {"phone_number": phone_number}
    # servers = ['18.138.8.34']
    for s in servers:
        url = f"http://{s}/api/ask_mobile_num"
        response = requests.post(url, json=body)
        if response.status_code == 200:
            return JsonResponse({"status": "ok", "server": s})

    return HttpResponseBadRequest(f"No server found for mobile {phone_number}")
