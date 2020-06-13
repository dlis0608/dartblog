from django.shortcuts import render


def index(request):
    current_path = request.path
    return render(request, 'blog/index.html', {'current_path': current_path})


def get_category(request, slug):
    return render(request, 'blog/category.html')
