from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm, EditForm

def home(request):
	my_name = {'user': "jacsarona"}
	return render(request, 'home.html', my_name)
#	if request.method == 'POST':
#		form = ListForm(request.POST or None)
#		if form.is_valid():
#			form.save() #insert into table where field == "";
#			all_items = List.objects.all()
#			context = {'all_items': all_items}
#			return render(request, 'home.html', context)
#	else:
#		all_items = List.objects.all # select * from List
#		context = {'all_items': all_items}
#		return render(request, 'home.html', context)

def about(request):
	my_name = "James Angelo C. Sarona"
	return render(request, 'about.html', {"myname": my_name})

def contact(request):
	my_name = {'user': "jacsarona"}
	return render(request, 'contact-us.html', my_name)

def listings(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None)
		if form.is_valid():
			form.save()
			all_items = List.objects.all()
			context = {'all_items': all_items, "user": "jacsarona"}
			return render(request, 'listings.html', context)
	else:
		all_items = List.objects.all()
		context = {'all_items': all_items, "user": "jacsarona"}
		return render(request, 'listings.html', context)
	
	my_name = {'user': "jacsarona"}
	return render(request, 'listings.html', my_name)

def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete() # delete something from your table
	return redirect('listings')

def strike(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True #update
	item.save()
	return redirect('listings')

def unstrike(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('listings')

def edit(request, list_id):
	if request.method == 'POST':		
		list_item = List.objects.get(pk=list_id)
		form = EditForm(request.POST or None)
		if form.is_valid():
			updated_item = form.cleaned_data.get("item")
			list_item.item = updated_item
			list_item.save()
			return redirect('listings')
	else:
		list_item = List.objects.get(pk=list_id)
		context = {"list_id": list_id, "list_item": list_item}
		return render(request, 'edit.html', context)