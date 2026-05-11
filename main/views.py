from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from datetime import date


# tag 관련 함수 ------------------------
def save_tags(post):
    words = post.content.split()
    tag_list = []

    for w in words:
        if len(w) > 0 and w[0] == '#':
            tag_list.append(w[1:])

    post.tags.clear()

    for t in tag_list:
        tag, _ = Tag.objects.get_or_create(name=t)
        post.tags.add(tag)


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'main/tag_list.html', {'tags': tags})


def tag_post_list(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    posts = tag.posts.all()
    return render(request, 'main/tag_post_list.html', {'tag': tag, 'posts': posts})
# comment 관련 함수--------------------------

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    post_id = comment.post.id

    if request.user == comment.writer:
        comment.delete()

    return redirect('main:detail', post_id)


def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.writer:
        return redirect('main:detail', comment.post.id)

    if request.method == 'POST':
        comment.content = request.POST['content']
        comment.save()
        return redirect('main:detail', comment.post.id)

# --------------------------------------------


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
        return redirect('accounts:login')
    return render(request, 'main/new_post.html', {'today': date.today().strftime('%Y-%m-%d')})


def postpage(request):
    posts = Post.objects.all()
    return render(request, 'main/postpage.html', {'posts': posts})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST' and request.user.is_authenticated:
        new_comment = Comment()
        new_comment.post = post
        new_comment.writer = request.user
        new_comment.content = request.POST['content']
        new_comment.save()
        return redirect('main:detail', post_id)

    comments = Comment.objects.filter(post=post)

    return render(request, 'main/detail.html', {'post': post, 'comments': comments})


def edit(request, post_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    edit_post = get_object_or_404(Post, pk=post_id)

    if edit_post.writer != request.user:
        return redirect('main:detail', edit_post.id)

    return render(request, 'main/edit.html', {'post': edit_post})


def create(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = request.POST['pub_date']
    new_post.content = request.POST['content']
    new_post.grade = request.POST['grade']
    new_post.save()

    save_tags(new_post)

    return redirect('main:detail', new_post.id)


def update(request, post_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    update_post = get_object_or_404(Post, pk=post_id)

    if update_post.writer != request.user:
        return redirect('main:detail', update_post.id)

    update_post.title = request.POST['title']
    update_post.writer = request.user
    update_post.pub_date = request.POST['pub_date']
    update_post.content = request.POST['content']
    update_post.grade = request.POST['grade']
    update_post.save()

    save_tags(update_post)

    return redirect('main:detail', update_post.id)


def delete(request, post_id):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    delete_post = get_object_or_404(Post, pk=post_id)

    if delete_post.writer != request.user:
        return redirect('main:detail', delete_post.id)

    delete_post.delete()

    return redirect('main:postpage')

