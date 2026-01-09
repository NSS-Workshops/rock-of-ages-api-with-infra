from django.http import JsonResponse
import requests

def health_check(request):
    return JsonResponse({
        "status": "ok",
        "instance": get_instance_id()
    })

def get_instance_id():
    try:
        return requests.get(
            "http://169.254.169.254/latest/meta-data/instance-id",
            timeout=0.2
        ).text
    except:
        return "unknown"