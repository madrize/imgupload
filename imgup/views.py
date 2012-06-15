from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from imgup.forms import ImgUploadForm
from imgupload.settings import *
import os
from imgup.models import Img

def upload_file(request):
    if request.method == 'POST':
        form = ImgUploadForm(request.POST, request.FILES)
        if form.is_valid():
            myf = request.FILES['file']
            filename = myf._get_name()
            saved = open(os.path.join(str(STATICFILES_DIRS[0]),filename),"wb+")
            for x in myf.chunks():
                saved.write(x)
            # add the image to database
            i = Img(uploader=request.user, img_name=filename)
            i.save()
            return HttpResponseRedirect('/')
    else:
        form = ImgUploadForm()
    return render_to_response('imgupload/upload.html', {'form': form},context_instance=RequestContext(request))