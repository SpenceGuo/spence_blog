# 实例：spence_blog
 Django 项目实例
 
 # 命令行创建项目
 django-admin startproject 项目名称
 
 # 项目目录介绍
 |---mysite # 项目的根目录 
  |---mysite # 项目名称
      |---__init__.py 
      |---settings.py # 配置文件 
      |---urls.py # 路由系统 ===> url与视图的对应关系 
      |---wsgi.py # runserver命令就使用wsgiref模块做简单的web server 
|---manage.py # 管理文件
