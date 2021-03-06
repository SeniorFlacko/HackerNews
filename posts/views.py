from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def home(request):
    return render(request,"index.html", {})

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Succesfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())

	else:
		messages.error(request,"Not Succesfully Created")

	context ={
		"form":form,
	}
	return render(request,"post_form.html",context)

def post_detail(request,id):
	instance = get_object_or_404(Post,id=id)
	context = {
		"title" : instance.title ,
		"instance" : instance , 
	}
	return render(request,"post_detail.html",context)


def post_list(request):
	queryset = Post.objects.all().order_by("-timestamp")
	context = {
		"title":"Lista de objetos", 
		"object_list":queryset
	}
	return render(request,"post_list.html",context)

def post_update(request,id=None):
	instance = get_object_or_404(Post,id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Item Saved")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title" : instance.title ,
		"instance" : instance , 
		"form" : form,
	}
	return render(request,"post_form.html",context)

def post_delete(request,id=None):
	instance = get_object_or_404(Post,id=id)
	instance.delete()
	messages.success(request,"Successfully deleted")
	return redirect("posts:list")