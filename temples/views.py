from django.shortcuts import render

from django.shortcuts import render
def index(request):
    name = request.GET.get("name") or "unknown"
    return render(request, "base.html", {"name" : name})

