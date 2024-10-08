from django.contrib import admin
from blog.models import Post,Category,Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','counted_views', 'status','published_date','login_require')
    list_filter = ('status',)
    ordering = ['-created_date']
    search_fields = ['title','content']
   


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name','post', 'approved','created_date',)
    list_filter = ('approved','post')
    search_fields = ['name','post']



admin.site.register(Comment,CommentAdmin)
admin.site.register(Post,PostAdmin)

admin.site.register(Category)