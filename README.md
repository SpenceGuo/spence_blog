# 实例：spence_blog
 Django 项目实例
 
 # 命令行创建项目
 django-admin startproject 项目名称
 
 # 项目目录介绍
 <p><img src="https://www.runoob.com/wp-content/uploads/2015/01/Django-env6.png"></p>
 |---mysite # 项目的根目录 <br />
  &nbsp;|---mysite # 项目名称<br />
  &nbsp;&nbsp;    |---__init__.py <br />
  &nbsp;&nbsp;    |---settings.py # 配置文件 <br />
  &nbsp;&nbsp;    |---urls.py # 路由系统 ===> url与视图的对应关系 <br />
  &nbsp;&nbsp;    |---wsgi.py # runserver命令就使用wsgiref模块做简单的web server <br />
|---manage.py # 管理文件
