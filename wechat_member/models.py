from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html
from django.db import models

@python_2_unicode_compatible
class Member(models.Model):
    name = models.CharField(_('name'), max_length=200)
    avatar = models.CharField(_('avatar'), max_length=200)
    openid = models.CharField(_('openid'), max_length=200)
    city = models.CharField(_('city'), max_length=200)
    created = models.DateTimeField(_('created time'), auto_now_add=True)
    updated = models.DateTimeField(_('updated time'), auto_now=True)

    def __str__(self):
        return self.name

    def avatar_url(self):
        return format_html(
            '<a href="#{}"><img src="#{}" height="30"></a>',
            self.avatar,
            self.avatar,
        )


    class Meta(object):
        verbose_name = _('wechat member')
        verbose_name_plural = _('wechat member')

    avatar_url.short_description= _('avatar')
