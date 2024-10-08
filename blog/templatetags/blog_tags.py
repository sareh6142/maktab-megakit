from django import template
from blog.models import Post,Category
from django.utils import timezone


register = template.Library()

@register.inclusion_tag('blog/blog_latest_post.html')
def latestposts(args):
    posts = Post.objects.filter(status=1).order_by('published_date')[:args]
    return {'posts':posts}

@register.inclusion_tag('blog/blog_categories.html')
def postcategories():
    posts = Post.objects.filter(status = 1,published_date__lte = timezone.now())
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]= posts.filter(category = name).count()
    return{'categories':cat_dict}