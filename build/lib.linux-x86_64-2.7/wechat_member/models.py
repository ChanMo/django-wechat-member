from django.utils.translation import ugettext_lazy as _
from django.db import models

class Member(models.Model):
    name = models.CharField(_('name'), max_length=200)
    avatar = models.CharField(_('avatar'), max_length=200)
    openid = models.CharField(_('openid'), max_length=200)
    city = models.CharField(_('city'), max_length=200)
    created = models.DateTimeField(_('created time'), auto_now_add=True)
    updated = models.DateTimeField(_('updated time'), auto_now=True)

    def __unicode__(self):
        return self.name

    def avatar_url(self):
        return '<a href="%s" target="_blank"><img src="%s" height="50"></a>' % (self.avatar, self.avatar)

    class Meta(object):
        verbose_name = _('wechat member')
        verbose_name_plural = _('wechat member')

    avatar_url.allow_tags = True
    avatar_url.verbose_name= _('avatar')
