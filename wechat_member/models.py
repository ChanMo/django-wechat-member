#!/usr/bin/python
# vim: set fileencoding=utf-8 :

from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=200, verbose_name='姓名')
    avatar = models.CharField(max_length=200, verbose_name='头像')
    mobile = models.CharField(max_length=20, blank=True, null=True,  verbose_name='手机号码')
    openid = models.CharField(max_length=200, verbose_name='微信ID')
    city = models.CharField(max_length=200, verbose_name='城市')
    created = models.DateTimeField(auto_now_add=True, verbose_name='注册时间')
    updated = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    def __unicode__(self):
        return self.name

    def avatar_url(self):
        return '<a href="%s" target="_blank"><img src="%s" height="50"></a>' % (self.avatar, self.avatar)

    class Meta(object):
        verbose_name = '会员'
        verbose_name_plural = '会员'

    avatar_url.allow_tags = True
    avatar_url.verbose_name='头像'
