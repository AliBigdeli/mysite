from django import template
from blog.models import Post,Comment
from blog.models import Category
from django.utils.html import strip_spaces_between_tags, strip_tags
from django.utils.text import Truncator

register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='comments_count')
def function(pid):
    return Comment.objects.filter(post=pid,approved=True).count()
    

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value,arg=20):
    return value[:arg] + "..."

@register.inclusion_tag('blog/blog-popular-posts.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}

@register.filter(name='excerpt')
def excerpt_with_ptag_spacing(value, arg):
    try:
        limit = int(arg)
    except ValueError:
        return 'Invalid literal for int().'

    # remove spaces between tags
    value = strip_spaces_between_tags(value)

    # add space before each P end tag (</p>)
    value = value.replace("</p>"," </p>")
    value = value.replace("&quot","  ")
    # strip HTML tags
    value = strip_tags(value)

    # other usage: return Truncator(value).words(length, html=True, truncate=' see more')
    return Truncator(value).words(limit)

@register.inclusion_tag('blog/blog-index-latestposts.html')
def index_latestposts(arg=6):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts':posts}
