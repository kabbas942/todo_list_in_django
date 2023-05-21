from django.shortcuts import render,HttpResponse,redirect
from .modelForm import todoListForm
from .models import todoList
from django.forms.models import model_to_dict
# Create your views here.
def index(request):
    RecordList = todoList.objects.all()   
    return render(request,"index.html",{'todoList':RecordList})
def addEvent(request):
    if request.method == 'POST':
        form = todoListForm(request.POST)        
        if form.is_valid():
            # Process the form data
            print(form.errors)
            form.save()
            # Redirect or return a response
            return redirect("/")
    else:
        form = todoListForm()
    return render(request, 'addEvent.html', {'form': form})


def deleteEvent(request,deleteId):
    todoList.objects.filter(id = deleteId).delete()
    return render(request, 'index.html')

def updateEvent(request,updateId):
    Record = todoList.objects.get(id=updateId)    
    if request.method == 'POST':
        form = todoListForm(request.POST,instance = Record)        
        if form.is_valid():
            # Process the form data
            form.save()
            # Redirect or return a response
    else:
        form = todoListForm(initial=model_to_dict(Record))
    return render(request, 'updateEvent.html', {'form': form,'updateId':updateId})

def loginUser(request):
    return HttpResponse("loginUser")
def logoutUser(request):
    return HttpResponse("logoutUser")


def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')  # Get the search query from the request's GET parameters
        RecordList = todoList.objects.filter(title__icontains=query)  # Perform case-insensitive search on the 'name' field
        if RecordList:
            recordParameter={'todoList':RecordList} 
        else:
            RecordList = todoList.objects.filter(description__icontains=query)
            recordParameter={'todoList':RecordList}
    return render(request,"index.html",recordParameter)



    