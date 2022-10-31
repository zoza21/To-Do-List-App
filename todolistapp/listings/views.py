from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
#have to import module name

from listings.models import Listing
from django.shortcuts import render
from listings.models import Todolist
from listings.forms import Todoform
from listings.forms import Listform
from django.shortcuts import redirect
from django.contrib import messages


	
def listings(request):
	listings = Listing.objects.all()
	return render(request, 'listings/listings.html', {'listings' : listings})
	

def todolist(request):
	
	if request.method == 'POST': 
		form = Todoform(request.POST)
		if form.is_valid():
			
			cd = form.cleaned_data
			itemform = Todolist.objects.create(
				item = cd['item'],
				details = cd['details'],
			)
			
			itemform.save()
			return redirect('todolist')
	
	else: 
		form = Todoform()
	
	return render(request, 'listings/todolist.html', {"form": Todoform(),})
	

def showlist(request):
	form = Todolist.objects.all()
	return render(request, 'listings/showlist.html', {'form': form})
	

def deleteitem(request, id):
	form = Todolist.objects.get(id=id)
	if request.method == "POST":
		form.delete()
		#messages.success(request, "Item successfully deleted")
		return redirect('showlist')
	
	return render(request, 'listings/deleteitem.html', {'form': form})