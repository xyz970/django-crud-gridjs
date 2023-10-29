from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.http.response import HttpResponse
import os
from pathlib import Path
from django.conf import settings

@csrf_protect
def uploadFile(request):
    if request.method == 'POST':
        photo = request.FILES['cover']
        fs = FileSystemStorage()
        filename = fs.save(photo.name, photo)
        uploaded = fs.url(filename)
        jsonRes = {'message': uploaded}
        return HttpResponse(filename)


def revertFile(request, filename):
    fs = FileSystemStorage()
    BASE_DIR = Path(__file__).resolve().parent.parent
    path = settings.MEDIA_ROOT+'/'+filename
    os.remove(path)
    jsonRes = {'message': 'file deleted'}
    return JsonResponse(jsonRes)


class FileHandling(TemplateView):
    pass
