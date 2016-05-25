基于django-wechat的会员模块
===========================

基于django和 `微信 <http://github.com/ChanMo/django_wechat/>`_ 的会员模块

快速开始:
---------

添加依赖:

    wechat模块的使用方法查看 `这里 <http://github.com/ChanMo/django_wechat/>`_ 


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

添加数据表:

.. code-block::

    python manage.py migrate

使用 *WxMemberView* 和 *self.wx_member* :

.. code-block::

    from wechat_member.views import WxMemberView

    class TestView(WxMemberView):
        def get_context_data(self, **kwargs):
            member = self.wx_member
            pass
