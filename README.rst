微信会员模块
=============

基于django-wechat-base的微信会员模块


快速开始:
---------

安装django-wechat-member:

.. code-block::

    pip install django-wechat-member



修改 *settings.py* 文件:

.. code-block::

    INSTALLED_APPS = (
        ...
        'wechat',
        'wechat_member',
    )


修改 *urls.py* 文件:

.. code-block::

    url(r'^wx_member/', include('wechat_member.urls', namespace='wx_member')),


更新数据库:

.. code-block::

    ./manage.py makemigrations wechat_member
    ./manage.py migrate


使用 *WxMemberView* 和 *self.wx_member* :

.. code-block::

    from wechat_member.views import WxMemberView

    class TestView(WxMemberView):
        def get_context_data(self, **kwargs):
            member = self.wx_member
            ...
