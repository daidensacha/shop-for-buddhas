from django.shortcuts import render, redirect
from .models import Category, Post, Comment
from .forms import CommentForm
from taggit.models import Tag


def blog_posts(request, tag_slug=None):
    posts = Post.objects.all()
    categories = Category.objects.all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags_in=[tag])

    context = {
        "posts": posts,
        "categories": categories,
        'tag': tag,
    }

    return render(request, "blog/blog_posts.html", context)


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request,
                  'blog/post_detail.html',
                  {'post': post, 'form': form}
                  )
