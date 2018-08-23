from django.shortcuts import render
from django.http  import HttpResponse
from .models import TrackForms,NewForm
from django.contrib.auth.decorators import login_required
from .forms import NewNewFormForm
from django.db import transaction
# Create your views here.
def welcome(request):
    return render(request, 'all-scoots/index.html')


def search_results(request):

    if 'referenceID' in request.GET and request.GET["referenceID"]:
        search_term = request.GET.get("referenceID")
        searched_ref = NewForm.search_by_referenceID(search_term)
        message = f"{search_term}"

        return render(request, 'all-scoots/search.html',{"message":message,"referenceID":searched_ref})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-scoots/search.html',{"message":message})
def profile(request):
    return render(request,'all-scoots/index.html')

def logout(request):
    return render(request, 'all-scoots/index.html')

def cargo_list(request):
    scoty = NewForm.objects.all()
    print(scoty)
    return render(request,'all-scoots/cargo.html',{"scoty":scoty})

@login_required(login_url='/accounts/login/')
def new_cargo(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewNewFormForm(request.POST, request.FILES)
        if form.is_valid():
            newnewformform = form.save(commit=False)
            newnewformform .save()
    else:
        form = NewNewFormForm()
    return render(request, 'all-scoots/new_cargo.html', {"form": form})

@transaction.atomic
def edit_cargo(request):
    if request.method =='POST':
        form=NewNewFormForm(request.POST, request.FILES, instance=request.NewNewFormForm)
        if form.is_valid():
            form.save()
            return redirect('all-scoots/cargo.html')
    else:
        form = NewNewFormForm(request.POST, request.FILES)
        return render(request, 'all-scoots/edit_cargo.html', {"form": form})
