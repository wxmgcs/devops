# devops

安装依赖
pip install -r requirements.txt

同步数据库
python manage.py makemigrations
python manage.py migrate

创建管理员
python manage.py createsuperuser

检查是否正常
python manage.py check

启动服务
python manage.py runserver 0.0.0.0:9992

参考资料:
http://css.cleanc.cn/
