from django import forms
from django.forms import ModelForm
from taggit.forms import TagField
from .models import IlastoPost

class IlastoPostForm(ModelForm):
    tags = TagField()  # タグの入力用フィールド

    class Meta:
        model = IlastoPost
        fields = ['category', 'title', 'comment', 'image1', 'image2', 'tags']

class SearchForm(forms.Form):
    query = forms.CharField(label='検索クエリ')