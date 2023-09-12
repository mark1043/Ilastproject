from django import forms
from django.forms import ModelForm
from taggit.forms import TagField
from .models import IlastoPost
from .models import Category
from .models import Uniformcolor
from django.contrib.auth.models import User

class IlastoPostForm(ModelForm):
    tags = TagField()  # タグの入力用フィールド

    class Meta:
        model = IlastoPost
        fields = ['category', 'title', 'comment', 'uniformcolor', 'image1', 'image2', 'tags']

class SearchForm(forms.Form):
    query = forms.CharField(label='検索クエリ', required=False)
    tags = TagField(label='タグ', required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='カテゴリ', required=False)
    uniformcolor = forms.ModelChoiceField(queryset=Uniformcolor.objects.all(), empty_label='ユニフォームカラー', required=False)