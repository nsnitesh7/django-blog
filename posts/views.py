from django.http import HttpResponse
# Create your views here.


def post_create(request):
	return HttpResponse("<h1>This is posts create page.</h1>")

def post_detail(request):
	return HttpResponse("<h1>This is posts detail page.</h1>")

def post_list(request):
	return HttpResponse("<h1>This is posts list page.</h1>")

def post_update(request):
	return HttpResponse("<h1>This is posts update page.</h1>")

def post_delete(request):
	return HttpResponse("<h1>This is posts delete page.</h1>")

