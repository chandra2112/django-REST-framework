from django.http import HttpResponse,JsonResponse

def home_page(request):
    friends=[
        "mudit",
        "ram",
        "laxman"
    ]
    return JsonResponse(friends, safe = False)