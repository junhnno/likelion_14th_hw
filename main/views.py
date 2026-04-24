from django.shortcuts import render, redirect, get_object_or_404
from .models import *

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
    return render(request, 'main/new_post.html')

def postpage(request):
    posts = Post.objects.all()
    return render(request, 'main/postpage.html', {'posts': posts})

def detail(request, post_id):
    detail_post = get_object_or_404(Post, pk=post_id)
    return render(request, 'main/detail.html', {'post': detail_post})

def edit(request, post_id):
    edit_post = get_object_or_404(Post, pk=post_id)
    return render(request, 'main/edit.html', {'post': edit_post})

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.POST['writer']
    new_post.pub_date = request.POST['pub_date']
    new_post.content = request.POST['content']
    new_post.grade = request.POST['grade']
    new_post.save()
    return redirect('main:postpage')

def update(request, post_id):
    update_post = get_object_or_404(Post, pk=post_id)
    update_post.title = request.POST['title']
    update_post.writer = request.POST['writer']
    update_post.pub_date = request.POST['pub_date']
    update_post.content = request.POST['content']
    update_post.grade = request.POST['grade']
    update_post.save()
    return redirect('main:postpage')

def delete(request, post_id):
    delete_post = get_object_or_404(Post, pk=post_id)
    delete_post.delete()
    return redirect('main:postpage')