from django import forms
from mysite.models.Book import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'isbn', 'publisher', 'published_date', 'author', 'cover']
        # fields = '__all__'
        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 '
                                                         'text-gray-700 leading-tight focus:border-indigo-700 '
                                                         'focus:outline-none focus:bg-white'}),
            'isbn': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 '
                                                    'text-gray-700 leading-tight focus:border-indigo-700 '
                                                    'focus:outline-none focus:bg-white'}),
            'publisher': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded w-full py-2 px-3 '
                                                         'text-gray-700 leading-tight focus:border-indigo-700 '
                                                         'focus:outline-none focus:bg-white'}),
            'published_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight '
                         'focus:border-indigo-700 focus:outline-none focus:bg-white'}, format="%Y-%m-%d"),
            'author': forms.TextInput(attrs={
                'class': 'shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight '
                         'focus:border-indigo-700 focus:outline-none focus:bg-white'})
        }

    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        return data
