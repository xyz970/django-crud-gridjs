from django.views.generic.base import TemplateView, View
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, reverse
from django.http import JsonResponse, HttpResponse
from mysite.models.Book import Book
from mysite.helper import helper_functions
from mysite.FormRequest.BookForm import BookForm
from django.core.serializers import serialize


def getBookData(req):
    data_url = reverse('getAllData')
    template_name = 'index.html'
    return render(request=req, template_name=template_name, context={'data_url': data_url})


def getBookDetail(req, slug):
    model = Book.objects.filter(
        slug__exact=slug
    ).first()
    # data = serialize('json', model)
    template_name = 'book-detail.html'
    context = {
        'model': model
    }
    # return helper_functions.send_json_res(model)
    return render(request=req, template_name=template_name,context=context)


def insertPage(req):
    form = BookForm()
    domain = get_current_site(req).domain
    tempUpload = reverse('tempUpload')
    tempRevert = reverse('revertFile')
    context = {'domain': domain, 'tempUpload': tempUpload, 'form': form, 'tempRevert': tempRevert}
    return render(request=req, template_name='book-insert.html', context=context)

def filterBookData(req,keyword):
    book = Book
    obj = book.objects.filter(
        book_name__icontains=keyword
    )
    data = serialize('json', obj)
    return helper_functions.send_json_res(data)

def storeBookData(req):
    if req.method != 'POST':
        return JsonResponse(
            {'error': 'true',
             'message': 'Request method must be POST'
             }, status=402)
    else:
        form = BookForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/')


def getAllBook(req):
    data = serialize('json', Book.objects.all())
    # json = {'data': data}
    return helper_functions.send_json_res(data)


class BookView(TemplateView):
    pass
