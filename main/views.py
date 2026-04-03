from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'main/mainpage.html')

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