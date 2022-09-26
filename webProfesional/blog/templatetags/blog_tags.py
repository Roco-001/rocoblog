from django import template
from ..models import Post, Comment, Category
from django.db.models import Count
from taggit.models import Tag

register = template.Library()
@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/tags/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.inclusion_tag('blog/tags/most_commented_posts.html')
def show_most_commented_posts(count=5):
    most_commented =  Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]
    return {'most_commented': most_commented}


@register.filter(name='total_comentarios')
def total_comentarios(id):
    return Comment.objects.filter(post__id=id).count()


@register.simple_tag
def tags_unicos():
    tag_names = [tag.name for tag in Tag.objects.all()]
    unique_list = list(dict.fromkeys(tag_names))
    return unique_list


@register.filter(name='total_category')
def total_category(id):
    return Post.objects.filter(categories__id=id).count()

#@register.simple_tag
#def categories():
 #   return Category.objects.all()


@register.simple_tag
def show_latest_posts_categories(inicio=0, count=5, id=1):
    return Post.published.filter(categories__id=id).order_by('-publish')[inicio:count]


@register.simple_tag
def show_latest_posts_footer(inicio=0, count=5):
    return Post.published.order_by('-publish')[inicio:count]


@register.inclusion_tag('blog/tags/mas_comentadas_categorias_portada.html')
def comentadas_posts_categories(inicio = 0, count=5, id=1):
    comentadas_posts_categories= Post.published.filter(categories__id=id).annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[inicio:count]
    return {'comentadas_posts_categories': comentadas_posts_categories}



@register.simple_tag
def trending(inicio= 0, count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
        ).order_by('-total_comments')[inicio:count]



@register.inclusion_tag('blog/tags/portada.html')
def portada_latest_posts(inicio= 0, count=5):
    portada_latest_posts = Post.published.order_by('-publish')[inicio:count]
    return {'portada_latest_posts': portada_latest_posts}


@register.inclusion_tag('blog/tags/most_commented_posts_categorias.html')
def show_most_commented_posts_categorias(count=5 , id=1):
    show_most_commented_posts_categorias = Post.published.filter(categories__id=id).annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]
    return {'show_most_commented_posts_categorias': show_most_commented_posts_categorias}


@register.inclusion_tag('blog/tags/latest_posts_category.html')
def show_latest_posts_category(count=5, id=1):
    show_latest_posts_category = Post.published.filter(categories__id=id).order_by('-publish')[:count]
    return {'show_latest_posts_category': show_latest_posts_category}