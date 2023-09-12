from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import IlastoPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import IlastoPost
from .models import Uniformcolor
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import IlastoPost
from django.db.models import Q
from .forms import SearchForm
from django.contrib.auth.decorators import login_required


class IndexView(ListView):
    template_name ='index.html'
    queryset = IlastoPost.objects.order_by('-posted_at')
    paginate_by = 9

@method_decorator(login_required,name='dispatch')
class CreateIlastView(CreateView):
    form_class = IlastoPostForm
    template_name = 'post_ilast.html'
    success_url =reverse_lazy('ilast:post_done')
    def form_valid(self, form):
        postdeta = form.save(commit=False)
        postdeta.user = self.request.user
        selected_uniformcolor = Uniformcolor.objects.first()
        postdeta.uniformcolor = selected_uniformcolor
        postdeta.save()
        return super().form_valid(form)
    
class PostSuccessView(TemplateView):
    template_name = 'post_success.html'

class CategoryView(ListView):
    template_name ='index.html'
    paginate_by = 9

    def get_queryset(self):
      category_id = self.kwargs['category']
      categories = IlastoPost.objects.filter(
        category=category_id).order_by('-posted_at')
      return categories

class UserView(ListView):
    template_name ='index.html'
    paginate_by = 9

    def get_queryset(self):
      user_id = self.kwargs['user']
      user_list = IlastoPost.objects.filter(
        user=user_id).order_by('-posted_at')
      return user_list

class DetailView(DetailView):
    template_name='detail.html'
    model=IlastoPost

class MypageView(ListView):
    template_name='mypage.html'
    paginate_by = 9
    def get_queryset(self):
        queryset = IlastoPost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return queryset

class IlastDeleteView(DeleteView):
    model = IlastoPost
    template_name = 'ilast_delete.html' 
    success_url = reverse_lazy('ilast:index') 
    def delete(self,request,*args,**kwargs):
        return super().delete(request,*args,**kwargs)

class CreateIlastView(CreateView):
    form_class = IlastoPostForm
    template_name = 'post_ilast.html'
    success_url = reverse_lazy('ilast:post_done')

    def form_valid(self, form):
        post_data = form.save(commit=False)
        post_data.user = self.request.user
        selected_uniformcolor = Uniformcolor.objects.first()
        post_data.uniformcolor = selected_uniformcolor
        post_data.save()
        form.save_m2m()
        return super().form_valid(form)
    
class IlastEditView(UpdateView):
    model = IlastoPost
    form_class = IlastoPostForm
    template_name = 'ilast_edit.html'  # 画像の編集画面のテンプレート
    success_url = reverse_lazy('ilast:top')  # 編集完了後のリダイレクト先

def search(request):
    form = SearchForm(request.GET)
    results = []

    if form.is_valid():
        query = form.cleaned_data.get('query')
        tags = form.cleaned_data.get('tags')
        category = form.cleaned_data.get('category')
        uniformcolor = form.cleaned_data.get('uniformcolor')

        results = IlastoPost.objects.all()

        if query:
            results = results.filter(Q(title__icontains=query) | Q(comment__icontains=query))

        if tags:
            results = results.filter(tags__name__in=tags)

        if category:
            results = results.filter(category=category)

        if uniformcolor:
            results = results.filter(uniformcolor=uniformcolor)

    context = {'form': form, 'results': results}
    return render(request, 'search_results.html', context)
