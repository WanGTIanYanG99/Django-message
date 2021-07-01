from django.contrib import admin
from app01.models import Message
# Register your models here.
#自定义模型管理类
##
class MessageAdmin(admin.ModelAdmin):
    list_display =['id','title','username','content','publish']
#注册模型类
admin.site.register(Message,MessageAdmin)
