from django.shortcuts import redirect, render, get_object_or_404
from devapp.forms import PostForm
from .forms import PostForm, CommentForm, FreeCommentForm, FreePostForm
from .models import Post, FreePost

# Create your views here.
def home(req):
    # posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-date')
    return render(req, 'index.html', {'posts': posts})

def postcreate(req):
    if req.method == 'POST' or req.method == 'FILES':
        form = PostForm(req.POST, req.FILES)
        if form.is_valid:
            form.save()
        return redirect('home')
    else:
        form = PostForm()
        return render(req, 'post_form.html', {'form' : form})

def detail(req, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(req, 'detail.html', {'post_detail': post_detail, 'comment_form' : comment_form})

def new_comment(req, post_id):
    field_form = CommentForm(req.POST)
    if field_form.is_valid:
        form = field_form.save(commit=False)
        form.post = get_object_or_404(Post, pk=post_id)
        form.save()
    return redirect('detail',post_id)


# FREE============================================================

def freehome(req):
    # posts = Post.objects.all()
    posts = FreePost.objects.filter().order_by('-date')
    return render(req, 'free_index.html', {'posts': posts})

def freepostcreate(req):
    if req.method == 'POST' or req.method == 'FILES':
        form = FreePostForm(req.POST, req.FILES)
        if form.is_valid:
            unfinished = form.save(commit=False)
            unfinished.author = req.user
            unfinished.save()
        return redirect('freehome')
    else:
        form = FreePostForm()
        return render(req, 'free_post_form.html', {'form' : form})

def freedetail(req, post_id):
    post_detail = get_object_or_404(FreePost, pk=post_id)
    comment_form = FreeCommentForm()
    return render(req, 'freedetail.html', {'post_detail': post_detail, 'comment_form' : comment_form})

def new_freecomment(req, post_id):
    field_form = FreeCommentForm(req.POST)
    if field_form.is_valid:
        form = field_form.save(commit=False)
        form.post = get_object_or_404(FreePost, pk=post_id)
        form.save()
    return redirect('freedetail',post_id)