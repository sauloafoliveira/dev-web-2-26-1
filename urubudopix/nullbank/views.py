from django.shortcuts import render

# Create your views here.
def index_nullbank(req):
    return render(req, "index_nb.html")
