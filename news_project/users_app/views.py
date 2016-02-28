from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator
from .models import category ,post,tag
# Create your views here.


#categories pagination

def catt(request):
	testcat= category.objects.all()
	return render(request,'cat.html',{"testcat":testcat})



def postcat(request,categoryn):
	pcat= post.objects.filter(post_category_id=categoryn)
	paginator = Paginator(pcat,5)  #Show 5 posts per page
	page_num=request.GET.get('page')
	try:
        	box = paginator.page(page_num)
	except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        	box = paginator.page(1)
	except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        	box= paginator.page(paginator.num_pages)

	return render(request, 'index.html',{"box":box})
