from django.forms import ModelForm
from .models import Tag, Quote, Author
from django import forms


class TagForm(ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Tag
        fields = ['name', 'tags']


class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['quote', 'author', 'tags']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
