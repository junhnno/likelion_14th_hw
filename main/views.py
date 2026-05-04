from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from datetime import date

def mainpage(request):
    context = {
        'generation': 14,                   
        'reviews': [
            'Templates 폴더 생성',
            'views.py 작성 -> request로 불러올 페이지 설정',
            'urls.py 작성 -> client가 보는 화면 설정',
            'Template 언어 -> 반복문, 상속',
            'navbar 상속',
            'static 폴더 생성 -> css, image',
        ]
    }
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    return render(request, 'main/secondpage.html')

def new_post(request):
    if not request.user.is_authenticated:
        return redirect('account:login')
    return render(request, 'main/new_post.html', {'today': date.today().strftime('%Y-%m-%d')})

def postpage(request):
    posts = Post.objects.all()
    return render(request, 'main/postpage.html', {'posts': posts})

def detail(request, post_id):
    detail_post = get_object_or_404(Post, pk=post_id)
    return render(request, 'main/detail.html', {'post': detail_post})

def edit(request, post_id):
    if not request.user.is_authenticated:
        return redirect('account:login')
    
    edit_post = get_object_or_404(Post, pk=post_id)

    if edit_post.writer != request.user.username:
        return redirect('main:detail', edit_post.id)
    
    return render(request, 'main/edit.html', {'post': edit_post})

def create(request):
    if not request.user.is_authenticated:
        return redirect('account:login')
    
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user.username
    new_post.pub_date = request.POST['pub_date']
    new_post.content = request.POST['content']
    new_post.save()

    return redirect('main:detail', new_post.id)

def update(request, post_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    update_post = get_object_or_404(Post, pk=post_id)

    if update_post.writer != request.user.username:
        return redirect('main:detail', update_post.id)
    
    update_post.title = request.POST['title']
    update_post.writer = request.user.username
    update_post.writer = request.POST['writer']
    update_post.pub_date = request.POST['pub_date']
    update_post.content =request.POST['content']
    update_post.save()

    return redirect('main:detail', update_post.id)

def delete(request, post_id):
    if not request.user.is_authenticated:
        return redirect('account:login')
    
    delete_post = get_object_or_404(Post, pk=post_id)
    
    if delete_post.writer != request.user.username:
        return redirect('main:detail', delete_post.id)

    delete_post.delete()

    return redirect('main:postpage')