from django.contrib import admin
from hello import models
# Register your models here.

class ControlUser(admin.ModelAdmin):
    '''自定义列表中栏目 添加list_display 属性'''
    # 显示字段
    list_display = ('user_name', 'psw', 'mail')   # 设置显示的字段
    search_fields = ('user_name',)  # 搜索条件user_name


class ControlArticle(admin.ModelAdmin):
    list_display = ('title', 'body', 'auth', 'create_time', 'update_time')  # 显示的字段
    search_fields = ('title',)  # 搜索条件
    ordering = ('-create_time',)  # 按字段排序 -表示降序

admin.site.register(models.User, ControlUser)
admin.site.register(models.Article, ControlArticle)
admin.site.register(models.Person)
admin.site.site_header = 'xx 项目管理系统'
admin.site.site_title = '登录系统后台'
admin.site.index_title = '后台管理'