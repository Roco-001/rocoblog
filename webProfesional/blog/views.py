from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post, Comment, Category, Reply
from django.views.generic.list import ListView
from django.db.models import Q
from .forms import EmailPostForm, CommentForm, SearchForm, ReplyCommentPostForm
from django.core.mail import send_mail
from django.contrib import messages
from django.db.models import Count
from django.views.generic.detail import DetailView
from django.views.generic.list import MultipleObjectMixin
from taggit.models import Tag
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from contact.models import Contact
# Create your views here.


#Muestra el Post detallado
def post_detail(request, post_id, post_slug):
    post = get_object_or_404(Post, slug=post_slug,
                             id=post_id)

    # Visitas
    post.visit = post.visit + 1
    post.save()

    mas_visitados = Post.published.order_by('-visit')[:5]

    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
        # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()

    else:
        comment_form = CommentForm()


    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]





    contex={
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'similar_posts': similar_posts,
        'mas_visitados': mas_visitados,

    }
    return render(request,'blog/detail_adaptado.html', contex)

#Comparte el post desde un formulario
def post_share(request, post_id, post_slug):
    post = get_object_or_404(Post, id=post_id, slug=post_slug, status='published')
    sent = False
    form = EmailPostForm()
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            # ... send email
            post_url = request.build_absolute_uri(
                post.get_absolute_url())
            subject = f"{cd['name']} te recomienda leer " \
                      f"{post.title}"
            message = f"Desde  mi Blog te enviamos  {post.title} at {post_url}\n\n" \
                      f"De parte de :{cd['name']}\n\n Y mis comentarios son: {cd['comments']}"
            send_mail(subject, message, 'rocoweb@outlook.com',
                      [cd['to']])
            sent = True
            Contact.objects.create(
                name='Shared ' + cd['name'],
                email=cd['email'],
                subject=cd['to'],
                content=cd['comments'])

            #messages.success(request, "Mensaje enviado Correctamente.")
        else:
            form = EmailPostForm()
    return render(request, 'blog/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent,
                                                    },)

#Tampoco funcional
def post_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', weight='A') + SearchVector('body', weight='B')
            search_query = SearchQuery(query)
            results = Post.published.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query)
            ).filter(rank__gte=0.3).order_by('-rank')

    return render(request,'blog/search.html',{'form': form,
                                                       'query': query,
                                                       'results': results})

#vista los post list por categoria
def category(request, category_id, post_slug, tag_slug=None):
    category = get_object_or_404(Category, id=category_id, slug=post_slug)
    object_list = Post.published.filter(categories__id=category_id)
    mas_visitados = Post.published.order_by('-visit')[:5]
    # Show most common tags
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    common_tags = Post.tags.most_common()[:15]
    paginator = Paginator(object_list, 5)  # 3 posts in each page



    page_num  = request.GET.get('page',1)
    try:
        page_obj = paginator.page(page_num )
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        page_obj = paginator.page(paginator.num_pages)

    queryset = request.GET.get('search')
    if queryset:
        page_obj = Post.published.filter(categories__id=category_id).filter(
            Q(title__icontains=queryset) |
            Q(body__icontains=queryset)
        ).distinct()

    return render(request, "blog/category.html", {'category':category,
                                                  'object_list':object_list,
                                                  'page_obj': page_obj,
                                                  'mas_visitados': mas_visitados,
                                                  'common_tags': common_tags,
                                                  'tag': tag,
                                                  })

#Muestra los post list genericos
def post_list(request ,tag_slug=None):
    object_list = Post.published.all()
    common_tags = Post.tags.most_common()[:20]
    mas_visitados = Post.published.order_by('-visit')[:5]



    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])


    paginator = Paginator(object_list, 5)  # 3 posts in each page

    page_num = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        page_obj = paginator.page(paginator.num_pages)

    queryset = request.GET.get('search')
    if queryset:
        page_obj = Post.published.filter(
            Q(title__icontains=queryset) |
            Q(body__icontains=queryset)
        ).distinct()

    return render(request, "blog/blog_list.html", {
                                                    'object_list': object_list,
                                                    'page_obj': page_obj,
                                                    'common_tags': common_tags,
                                                    'mas_visitados': mas_visitados,
                                                    'tag': tag,
                                                  })

#Comparte el post desde un formulario
def commet_reply(request, comment_id):
    comment = get_object_or_404(Comment,id=comment_id)
    reply = None


    if request.method == 'POST':
        reply_form = ReplyCommentPostForm(data=request.POST)
        if reply_form.is_valid():
            cd = reply_form.cleaned_data
            reply = Reply.objects.create(
                name=cd['name'],
                email=cd['email'],
                body=cd['body'],
                comment_id =comment_id)
            return redirect(reverse('blog:post_list') + "?ok")
    else:
        reply_form = ReplyCommentPostForm()

    context = {
        'reply': reply,
        'reply_form': reply_form,

    }
    return render(request, 'blog/reply_comment.html', context)