from setuptools import setup
from os import path
from codecs import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as readme:
    README = readme.read()


setup(
    name = 'django-wechat-member',
    version = '0.3.5',
    packages = ['wechat_member'],
    install_requires = ['django-wechat-base'],
    include_package_data = True,
    license = 'BSD License',
    description = 'fixed admin avatar error',
    long_description = README,
    url = 'https://github.com/ChanMo/django-wechat-member',
    author = 'ChanMo',
    author_email = 'chen.orange@aliyun.com',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
