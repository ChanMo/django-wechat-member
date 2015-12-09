from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings

from wechat import api
from .models import WechatMember

class CheckLogin(object):
    def process_request(self, request):
        current_site = get_current_site(request)
        domain = current_site.domain
        current = request.path
        if WECHAT_MEMBER_CHECK_URLS in current:
            try:
                member_id = request.session['wechat_member_id']
            except KeyError:
                return_uri = u'http:///%s/api/get_member/' % domain
                wx = api.Member()
                url = wx.get_code_url(return_uri, current)
                return HttpResponseRedirect(url)

