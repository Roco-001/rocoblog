from django.shortcuts import render, HttpResponse, get_object_or_404
from blog.models import Post
from django.db.models import Count
from django.db.models import Q



def home(request):
    posts = Post.published.filter(sliders=True)
    queryset = request.GET.get('search')
    if queryset:
        posts = Post.published.filter(
            Q(title__icontains=queryset) |
            Q(body__icontains=queryset)
        ).distinct()
    return render(request, "core/index.html", {'posts': posts})



