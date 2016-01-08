from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from wechat import api
from .models import Member

class WxAuth(View):
    def get(self, request, *args, **kwargs):
        code = request.GET['code']
        state = request.GET['state']
        wx = api.Member()
        info = wx.get_user_info(code)
        try:
            member = Member.objects.get(openid=info['openid'])
        except Member.DoesNotExist:
            member = Member(
                name = info['nickname'],
                openid = info['openid'],
                avatar = info['headimgurl'],
                city = info['city'],
            )
        member.save()
        data = {
            "id": member.id,
            "openid": member.openid,
            "name": member.name,
            "avatar": member.avatar,
        }
        request.session['wx_member'] = data
        return HttpResponseRedirect(state)


class WxMemberView(object):
    def dispatch(self, request, *args, **kwargs):
        super(WxMemberView, self).dispatch(request, *args, **kwargs)
        try:
            member_id = request.session['wx_member']['id']
            wx_member = Member.objects.get(id=member_id)
            return super(WxMemberView, self).dispatch(request, *args, **kwargs)
        except (KeyError, Member.DoesNotExist):
            return_uri = 'http://' + request.get_host() + reverse('wx_member:auth')
            wx = api.Member()
            url = wx.get_code_url(return_uri, request.path)
            return HttpResponseRedirect(url)
