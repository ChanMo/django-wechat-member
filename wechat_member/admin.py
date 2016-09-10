from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'avatar_url', 'city', 'openid', 'created')
    list_filter = ('created',)
    list_per_page = 12
    search_fields = ['name']
    readonly_fields = ('openid',)

admin.site.register(Member, MemberAdmin)
