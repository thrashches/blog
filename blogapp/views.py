from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Post, Comment
from django.shortcuts import get_object_or_404
from .forms import CommentForm

# Create your views here.


class PostList(ListView):
    model = Post
    template_name = 'index.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'


class PostCreate(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'
    success_url = '/'


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    template = 'post.html'
    form = CommentForm(request.POST)
    context = {
        'post': post,
        'form': form
    }

    if request.user.is_authenticated:
        if request.method == 'POST':
            print(request.POST)
            if form.is_valid():
                comment = Comment()
                comment.text = form.cleaned_data['text']

                comment.posted_by = request.user
                comment.post = post
                comment.save()
    else:
        context = {
            'post': post
        }

    return render(request, template_name=template, context=context)


'''
def post_create(request):
    
'''
## TODO: поле автор поста должно подставляться из post запроса
## TODO: исправить в шаблоне кнопку NEW. Она не должна отображатьсяя если пользователь не залогинен

# TODO: настроить перенаправление в случае успешного создания объекта на новый объект.