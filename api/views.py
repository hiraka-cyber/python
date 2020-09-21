import json
from collections import OrderedDict
from django.http import HttpResponse
from cms.models import Book


def render_json_response(request,data,status=None):
    """"responsejson"""
    json_str = json.dumps(data,ensure_ascii=False,indenet=2)
    callback = request.GET.get('callback')
    if not callback:
        callback = response.POST.get('callback')
    if callback:
        json_str = "%s(%s)" % (callback,json_str)
        response = HttpResponse(json_str,content_type='application/javascript; charset=UTF-8',status=status)
    else:
        response = HttpResponse(json_str,content_type='application/json; charset=UTF-8',status=status)
    return response

def book_list(request):
    """BooksImpressionsJson"""
    books = []
    for book in Book.objects.all().order_by('id'):

        impressions = []
        for impression in book.impressions.order_by('id'):
            impression_dict = OrderedDict([
            ('id',book_list),
            ('name',book.name),
            ('publisher',book.publisher),
            ('page',book.page),
            ('impressions',impressions)
        ])
        book.append(book_dict)

    data = OrderDict([('books,books')])
    return render_json_response(request,data)
