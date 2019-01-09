## centOS7部署Django
因为centOS默认安装的是python2.7，以用来支撑yum等系统命令的运行，但是因为安装Django和自己比较习惯，所以需要另外装python3

	//首先是python3的安装
	yum install  -y zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel  //先安装依赖，里边libffi-devel 是python3.7以上才需要
	wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz  //下载python安装包，可以修改版本号下载更高版本
	tar -xvJf  Python-3.6.2.tar.xz  //解压压缩包
	cd Python-3.6.2  //进入到解压出来的文件中
	./configure prefix=/usr/local/python3  //编译源码，后面的路径名就是安装路径
	make && make install  //执行安装，这一步如果报错说缺少什么依赖，比如libffi-devel，可以直接安装完依赖回来继续make & make install
	ln -s /usr/local/python3/bin/python3  /usr/bin/python3  //设置软连接，相当于win下的配环境，后面路径改为/usr/bin/python则后续使用python命令进行调用时会直接调用python3，为了将2和3区分开，我们这里单独用python3，后续也使用python3进行调用
	
	//然后是setuptools和pip的安装（这个是为了安装pip3，自带的pip也是不支持python3）
	wget https://files.pythonhosted.org/packages/37/1b/b25507861991beeade31473868463dad0e58b1978c209de27384ae541b0b/setuptools-40.6.3.zip  //后面的http链接可以通过https://pypi.org/project/获取最新的安装包，
	unzip setuptools-40.6.3.zip   //解压，可能需要yum install unzip
	cd setuptools-40.6.3.zip
	python3 setup.py build
	python3 setup.py install  //注意用我们刚刚装好的python3来执行
	ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3  //设置软连接时同样与原来的pip区分开

	//最后安装Django
	pip3 install django 

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
## 启动服务  

	python manage.py runserver