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


# 配置 saltstack netapi
开始前也需要安装salt的api

yum install -y salt-api cherrypy salt-master salt-minion
证书生成：

创建saltapi用户
useradd -M -s /sbin/nologin saltapi
passwd saltapi

创建验证文件
cd /etc/pki/tls/certs/
make testcert 
一路回车

cd /etc/pki/tls/private/
openssl rsa -in localhost.key -out localhost_nopass.key
note: 如果不用localhost_nopass.key,每次启动salt-api都需要输入密码


vim /etc/salt/master
rest_cherrypy:
  port: 8000
  host: 0.0.0.0
  debug: True
  ssl_crt: /etc/pki/tls/certs/localhost.crt
  ssl_key: /etc/pki/tls/private/localhost_nopass.key

external_auth:
  pam:
    saltapi:
      - '*'
      - '@wheel'
      - '@runner'



如果不安装 salt-minion就找不到salt-call命令,就无法执行
salt-call tls.create_self_signed_cert

启动salt-api
salt-api  > /var/log/salt-api.log 2>&1 &

参考:http://blog.csdn.net/hnhuangyiyang/article/details/50667000


测试授权是否有效
salt -T -a pam '*' test.ping


可以使用salt.client 或者rest_api的方式
如果web服务是不是在salt-master上,使用salt.client就可以了,如果是远程调用,需要在salt-master上提供rest-api(http://salt-api.readthedocs.io/en/latest/#)


安装pydev
http://pydev.org/updates

curl -ik https://localhost:8000/ -H "Accept: application/json" -H "X-Auth-Token:f65948d2ea5edc7ce0177872c28cd00dac346b02" -d client='local' -d tgt='*' -d fun="test.ping"






结果
[root@iZ25lx34hhyZ certs]# curl -k https://localhost:8000/login -H "Accept: application/json"  -d username='saltapi' -d password='Ctu800617Ctu' -d eauth=pam
{"return": [{"perms": ["*", "@wheel", "@runner"], "start": 1502781759.7395561, "token": "5a2cdf946679355e6a31f470589671a6b7329858", "expire": 1502824959.7395561, "user": "saltapi", "eauth": "pam"}]}[root@iZ25lx34hhyZ certs]# 
[root@iZ25lx34hhyZ certs]# curl -ik https://localhost:8000/ -H "Accept: application/json" -H "X-Auth-Token:f65948d2ea5edc7ce0177872c28cd00dac346b02" -d client='local' -d tgt='*' -d fun="test.ping"
HTTP/1.1 200 OK
Content-Length: 37
Access-Control-Expose-Headers: GET, POST
Access-Control-Allow-Credentials: true
Vary: Accept-Encoding
Server: CherryPy/3.2.2
Allow: GET, HEAD, POST
Cache-Control: private
Date: Tue, 15 Aug 2017 07:22:52 GMT
Access-Control-Allow-Origin: *
Content-Type: application/json
Set-Cookie: session_id=f65948d2ea5edc7ce0177872c28cd00dac346b02; expires=Tue, 15 Aug 2017 17:22:52 GMT; Path=/

{"return": [{"test1.51du.cn": true}]}[root@iZ25lx34hhyZ certs]# 

### 怎样从不同的操作系统的不同目录查询到实时日志


调试 salt-master salt-minion
salt-master --log-level=debug
salt-minion --log-level=debug


执行sls命令
master上执行
```
salt my_testserver state.apply
```
类似于在my_testserver上执行
```
salt-call state.apply
```
minion 测试执行,并不会有效果
```
salt-call state.apply --local
```


查看日志
 cat /var/log/salt/master
 
 
external_auth:
   pam:
 thatch:
 - '@wheel' # to allow access to all wheel modules
 - '@runner' # to allow access to all runner modules
 - '@jobs' # to allow access to the jobs runner and/or wheel module


spm 包管理

pillar 保存的key: value
eg:


重启minion
salt -G kernel:Windows cmd.run_bg 'C:\salt\salt-call.bat --local service.restart salt-  →minion'











The cp.get_file function can be used on the minion to download a file from the master, the syntax looks like this:
# salt '*' cp.get_file salt://vimrc /etc/vimrc