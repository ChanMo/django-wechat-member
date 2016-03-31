基于django-wechat的会员模块
===========================

基于django和`微信<http://github.com/ChanMo/django_wechat/>`的会员模块

快速开始:
---------

添加依赖:

    `wechat模块的使用方法查看这里<http://github.com/ChanMo/django_wechat/>`

安装模块:
.. code-block::

    pip install git+https://github.com/ChanMo/django_wechat_member.git

修改settings.py文件:
.. code-block::

    INSTALLED_APPS = (
        ...
        'wechat',
        'wechat_member',
    )

添加数据表:
.. code-block::

    python manage.py migrate

使用`WxMemberView`和`self.wx_member`:
.. code-block::

    from wechat_member.views import WxMemberView

    class TestView(WxMemberView):
        def get_context_data(self, **kwargs):
            member = self.wx_member
            pass
