=============
Wechat_Member
=============

Wechat-member is based django-wechat module.
It used for wechat member.
Include nickname, avatar, city, openid

Detailed documentation is in the "docs" directory

Quick start
-----------

1. Add "wechat-member" to your INSTALLED_APPS setting like this::
   INSTALLED_APPS = (
       ...
       'wechat',
       'wechat_member',
   )

2. Include the wechat URLconf in your project urls.py like this::
   url(r'^wechat-member/', include('wechat-member.urls')),

3. Run 'python manage.py migrate' to create the wechat member models.
4. Use WxMemberView in your views::
   from member.views import WxMemberView
   class TestView(WxMemberView):
       pass
5. Use wechat member session in your views::
   self.request.session['wx_member']
