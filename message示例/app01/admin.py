from django.contrib import admin
from app01.models import Message
# Register your models here.
#�Զ���ģ�͹�����
##
class MessageAdmin(admin.ModelAdmin):
    list_display =['id','title','username','content','publish']
#ע��ģ����
admin.site.register(Message,MessageAdmin)
