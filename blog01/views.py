from django.shortcuts import render
from .models import Post, Author, Category


def category_post(request, category_name):
    category = Category.objects.get(name=category_name)
    posts = Post.objects.filter(category=category)
    category_list = Category.objects.all()

    return render(request, 'blog/category_details_new.html', {'posts': posts, 'category_list': category_list, 'name': category_name})



def author_list(request):
    authors = Author.objects.all()
    category = Category.objects.all()
    context = {
        'authors': authors,
        'category_list': category
    }

    return render(request, 'blog/author_list_new.html',context)

def authors_post (request, author_name):
    author = Author.objects.get(name=author_name)
    posts = Post.objects.filter(author=author)
    category = Category.objects.all()

    return render(request, 'blog/author_details_new.html', {'posts': posts, 'category_list': category, 'name': author_name})



def post_list(request):
    posts = Post.objects.all()
    category = Category.objects.all()
    context = {
        'post_list': posts,
        'category_list': category
    }

    return render(request,'blog/post_list_new.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    category = Category.objects.all()
    context = {
        'post': post,
        'category_list': category
    }
    return render(request, 'blog/post_details_new.html', context)

def test(request):
    return render(request, 'blog/test2.html')

