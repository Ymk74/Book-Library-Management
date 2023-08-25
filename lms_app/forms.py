from django import forms
from .models import Book , Category


class CategoryForm(forms.ModelForm):
    class Meta :
        model = Category
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'})
        }





class BookForm(forms.ModelForm):
    class Meta :
        model = Book
        fields = '__all__'    


        