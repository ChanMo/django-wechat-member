=============
Wechat-Member
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
       'wechat-member',
   )

2. Add "wechat-member.middleware" to your MIDDLEWARE_CLASSES settings like this::
   MIDDLEWARE_CLASSES = (
       ...
       'wechat-member.middleware.CheckLogin',
   )

3. Add "WECHAT_MEMBER_CHECK_URL" to your settings like this::
   ...
   WECHAT_MEMBER_CHECK_URL = "/m/"

4. Include the wechat URLconf in your project urls.py like this::
   url(r'^wechat-member/', include('wechat-member.urls')),

5. Run 'python manage.py migrate' to create the wechat models.

