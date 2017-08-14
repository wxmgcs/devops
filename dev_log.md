# 修改soms 为devops

#修改 templates/base.html 中


# 安装 halite
1, git clone https://github.com/saltstack/halite.git
2, cd halite
3, python setup.py install
4, pip install paste
5, pip install gevent
6, cd halite/halite
server_bottle.py
$ ./server_bottle.py -d -C -l debug -s cherrypy
$ ./server_bottle.py -d -C -l debug -s paste
$ ./server_bottle.py -d -C -l debug -s gevent

test
http://localhost:8080/app


开始前也需要安装salt的api
yum install -y salt-api python-cherrypy

证书生成：
useradd -M -s /sbin/nologin saltapi
passwd saltapi
cd /etc/pki/tls/certs/
make testcert
一路回车
cd /etc/pki/tls/private/
openssl rsa -in localhost.key -out localhost_nopass.key


可以使用salt.client 或者rest_api的方式
如果web服务是不是在salt-master上,使用salt.client就可以了,如果是远程调用,需要在salt-master上提供rest-api(http://salt-api.readthedocs.io/en/latest/#)


安装pydev
http://pydev.org/updates
