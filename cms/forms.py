from django.forms import ModelForm
from cms.models import Book,Impression


class BookForm(ModelForm):
    """BooksForm"""
    class Meta:
        model = Book
        fields = ('name','publisher','page',)

class ImpressionForm(ModelForm):
    """ImpressionForm"""
    class Meta:
        model = Impression
        fields = ('comment',)
