## Django项目初始化  

	pip install Django  //安装
	django-admin startproject 项目名称  //初始化项目
	python manage.py startapp 应用名称  // 初始化应用  
	INSTALLED_APPS = [ '应用名称',	]  //每一个应用都需要在settings文件中注册
	
	//可以进行时区和语言设置
	LANGUAGE_CODE = 'zh-hans'
	TIME_ZONE = 'Asia/Shanghai'  

#### 目录介绍  
> manage.py ： Django项目里面的工具，通过它可以调用django shell和数 据库等。
> 
> （项目名称同名文件夹）/
> 
> settings.py ： 包含了项目的默认设置，包括数据库信息，调试标志以及其他一些工作的变量。
>  urls.py ： 负责把URL模式映射到应用程序。
>  wsgi.py :  用于项目部署。  
>  
>（应用名称同名文件夹） /
> 
> admin.py  :  django 自带admin后面管理，将models.py 中表映射到后台。
> 
>  apps.py :  blog 应用的相关配置。
> 
>  models.py  : Django 自带的ORM，用于设计数据库表。
> 
>  tests.py  :  用于编写Django单元测试。
> 
>  veiws.py ：视图文件，用于编写功能的主要处理逻辑。  

	python manage.py migrate  //初始化数据库

	python manage.py createsuperuser  //创建超级管理员账号，通过http://localhost:8000/admin访问

## 路由和视图