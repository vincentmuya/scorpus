from django.shortcuts import render
from django.http  import HttpResponse
from . models import TrackForms

# Create your views here.
def welcome(request):
    return render(request, 'all-scoots/index.html')

def search_results(request):
    
    if 'ReferenceId' in request.GET and request.GET["ReferenceId"]:
        search_term = request.GET.get("ReferenceId")
        searched_ref = Article.search_by_ReferenceId(search_term)
        message = f"{search_term}"

        return render(request, 'all-news/search.html',{"message":message,"ReferenceIds": searched_ref})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-scoots/search.html',{"message":message})
