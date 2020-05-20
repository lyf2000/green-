from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http.response import JsonResponse
import ast
# Create your views here.
from django.views.generic import DetailView

from blog.api.filters import PostFilter
from blog.forms import PostForm, MeetForm
from blog.models import Meet, Post


# def index(request):
#     if request.is_ajax():
#         print('AJAX')
#         coords = ast.literal_eval(request.POST.get('coords', None))
#         return JsonResponse({'data': 'OK'})
#
#     return render(request, 'blog/index.html')


def post_list(request):
    f = PostFilter(request.GET, queryset=Post.objects.all())
    return render(request, 'blog/post_list.html', {'filter': f})


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


def map(request, pk):
    meet = Meet.objects.get(id=pk)
    return render(request, 'blog/map_test.html', {'meet': meet})


def meet_create(request):
    if request.method == 'POST':
        meet = MeetForm(request.POST)
        if meet.is_valid():
            meet = meet.save()
            a=2
    form = MeetForm()
    return render(request, 'blog/meet_create.html', {'form': form})


class BookForm(forms.ModelForm):
    """
    Your `forms.ModelForm` subclass representing the `Book` model directly.
    """

    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'main_img']


@login_required
def post_create(request):
    if request.method == 'POST':
        post = PostForm(request.POST, request.FILES)
        if post.is_valid():
            post.save()

        else:
            context = {}
            context['form'] = post
            return render(request, 'blog/post_create.html', context)
    form = PostForm(initial={'author': request.user})
    context = {
        'form': form
    }

    return render(request, 'blog/post_create.html', context)
