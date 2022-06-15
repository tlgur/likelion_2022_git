from django.shortcuts import redirect, render, get_object_or_404
from devapp.forms import PostForm
from .forms import PostForm, CommentForm
from .models import Post

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