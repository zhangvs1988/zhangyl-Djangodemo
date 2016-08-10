from django.contrib import  admin

from  .models import  Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("block","title","content","status","creat_timestamp","last_update_timestamp")#此处需要注意的是在双引号中内容不能有空格

admin.site.register(Article,ArticleAdmin)