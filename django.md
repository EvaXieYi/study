cmd创建django项目管理文件夹
django-admin startproject  项目名
查询win系统命令位置
where 
django创建web应用程序
python manager.py startapp  应用名称
运行django项目
python manager.py runserver  


django中文件 db.sqlite3默认的本地小型数据库文件，在app里面用到
manage.py项目的管理文件
项目中文件：
asgi.py 异步服务器网关接口，基于wsgi开发的应用。多了异步，websocket
wsgi.py web服务器网关接口
settings.py 项目的配置文件，配置上传文件夹路径，应用，第三方应用
urls.py 路由文件，根据浏览器函数进行关联的配置文件


models.py 数据库模型文件[是和数据库表关联的]
migrations 缓存文件夹
views  试图逻辑文件，将数据调用模板去渲染到浏览器


sqlitestudio 进行访问python创建的sqlit文件


生成django中自带的数据表
python manage.py migrate   

创建登录python页面/admin的登录用户名和密码以及邮箱
python manage.py createsuperuser

清空
python manage.py flush