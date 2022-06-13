from django.shortcuts import redirect, render
from devapp.forms import PostForm
from .forms import PostForm

# Create your views here.
def home(req):
    return render(req, 'index.html')

def postcreate(req):
    if req.method == 'POST' or req.method == 'FILES':
        form = PostForm(req.POST, req.FILES)
        if form.is_valid:
            form.save()
        return redirect('home')
    else:
        form = PostForm()
        return render(req, 'post_form.html', {'form' : form})