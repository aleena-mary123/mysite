from django.shortcuts import render

def home(request):
	return render(request,"home.html",{})

def about(request):
	from pages.namer import name
	# my_name = "Hey, My Name Is John Smith"
	# return render(request,"about.html", {"Name": my_name})
	return render(request,"about.html", {"my_stuff": name})
def contact(request):
	return render(request,"contact.html",{})