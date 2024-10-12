from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post
from django import forms
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def blog_view(request,**kwargs):
    posts = Post.objects.filter(published_date__lte = timezone.now()  , status=1)
    if kwargs.get('author_username')!=None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('cat_name')!= None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('tag_name')!=None:
        posts =posts.filter(tag__name__in=[kwargs['tag_name']])
        
        
    posts = Paginator(posts,2)
    try:
        page_number = request.GET.get('page')
        posts =posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    
        
    context ={'posts': posts}
    return render(request,"blog/blog-grid.html",context)
     
    


def blog_single(request,pk):
    
    post = get_object_or_404(Post, id=pk , published_date__lte = timezone.now() , status = 1)
    post_first = Post.objects.filter(published_date__lte = timezone.now() , status = 1).first()
    post_last = Post.objects.filter(published_date__lte = timezone.now() , status = 1).last()


    next_post = Post.objects.filter(published_date__lte = timezone.now()).filter( id__lt=post.id , status= 1).order_by('-id').first()
    prev_post =Post.objects.filter(published_date__lte = timezone.now()).filter( id__gt=post.id, status = 1).order_by('-id').last()
    post.counted_views+=1
    post.save()
    context ={  'post': post,
                'prev':prev_post,
                'next':next_post,
                'post_first':post_first,
                'post_last':post_last,
            }
    return render(request,"blog/blog-single.html",context)


def blog_category(request,cat_name):
    posts = Post.objects.filter(published_date__lte = timezone.now(), status = 1)
    posts = posts.filter(category__name= cat_name)
    context ={'posts': posts}
    return render(request,'blog/blog-grid.html',context)
    
    
    
def blog_search(request):
    posts= Post.objects.filter(published_date__lte = timezone.now(), status=1)
    print(request)
    if request.method == 'GET':
        #print(request)
        if s := request.GET.get('s'):
            print(request)
            posts = posts.filter(content__contains=s)
    context = {'posts':posts}
    return render(request,'blog/blog-grid.html',context)  


def customhandler404(request):
    response = render(request, '404_page.html',)
    response.status_code = 404
    return response