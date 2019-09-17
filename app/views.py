from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic

from app.forms import CommentForm
from app.models import Post, Comments, Tag


# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 2


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def add_comment_to_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})


def comment_approve(request, slug):
    comment = get_object_or_404(Comments, slug=slug)
    comment.approve()
    return redirect('post_detail', slug=comment.post.slug)


def comment_remove(request, slug):
    comment = get_object_or_404(Comments, slug=slug)
    comment.delete()
    return redirect('post_detail', slug=comment.post.slug)


def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'tag_detail.html', context={'tag': tag})
