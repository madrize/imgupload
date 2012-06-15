from django.shortcuts import render_to_response
from django.template import RequestContext
from imgup.models import Img
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def get_images(request,template="imgupload/get_images.html"):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/")
    
    try:
        images = Img.objects.filter(uploader=request.user)
    except:
        images = None
		# no images
		# display no image message
    
    paged = Paginator(images,4)
    
    # check the page request, if its not an int, return first page
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1
    
    # if page request is out of range, return last page
    try:
        imgs = paged.page(page)
    except (EmptyPage, InvalidPage):
        imgs = paged.page(paged.num_pages)
    
    return render_to_response(template,
                                {"images":imgs},
                                context_instance=RequestContext(request))