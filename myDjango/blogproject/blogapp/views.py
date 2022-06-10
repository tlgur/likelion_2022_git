from django.shortcuts import render, redirect, get_object_or_404
from .models import blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm

def home(request):
    posts = blog.objects.all()
    return render(request, 'home.html', {'posts' : posts}) 

def new(request):
    return render(request, 'new.html')

def create(request):
    if(request.method == 'POST'):
        post = blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

def formcreate(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
        return redirect('home')
    else: 
        form = BlogForm()
        return render(request, 'form_create.html', {'form' : form})


def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            post = blog()
            form.save()
        return redirect('home')
    else: 
        form = BlogModelForm()
        return render(request, 'form_create.html', {'form' : form})

def detail(request, blog_id):
    blog_detail = get_object_or_404(blog, pk=blog_id)
    comment_form = CommentForm()
    
    return render(request, 'detail.html', {'blog_detail':blog_detail, 'comment_form': comment_form})

def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid:
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(blog, pk=blog_id)
        finished_form.save()
    return redirect('detail', blog_id)