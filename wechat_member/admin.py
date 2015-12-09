from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'avatar', 'openid', 'created')
    readonly_fields = ('openid',)

admin.site.register(Member, MemberAdmin)
