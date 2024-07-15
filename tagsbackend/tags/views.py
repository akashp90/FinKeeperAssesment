from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Tag
from django.views import generic
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from .forms import PostForm, TagForm

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print("Post tags: " + post.tag_names)
    return render(request, 'post_detail.html', {'post': post})

def edit_tags(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = TagForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = TagForm(instance=post)
    return render(request, 'edit_tags.html', {'form': form, 'post': post})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('home_feed')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

def home_feed(request):
    posts = Post.objects
    tags = request.GET.get('tags')
    filter_type = request.GET.get('filter_type')

    if tags:
        tag_names = [tag.strip() for tag in tags.split(',')]
        tag_objects = Tag.objects.filter(name__in=tag_names)
        safe_tag_names = ",".join(tag_objects.order_by("name").values_list("name", flat=True))

        if filter_type == 'all':
            all_posts = posts.all()
            post_ids = []
            for post in all_posts:
            	if post.tag_names == safe_tag_names:
            		post_ids.append(post.id)
            posts = Post.objects.filter(id__in=post_ids)
        elif filter_type == 'any':
            posts = posts.filter(tags__in=tag_objects).distinct()
    else:	
    	posts = posts.all()


    return render(request, 'home.html', {'posts': posts})
