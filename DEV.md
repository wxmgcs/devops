功能列表
#### 程序列表
    1. 程序编号,状态,程序类型,VPN编号,IP地址,系统类型,操作
    2. 操作
        1,程序管理,日志管理,修改信息,监控,远程命令
#### 日志管理


#### 权限管理
    1. 忘记密码?
    2. 

#### Profile

可以使用原型工具,帮助生成页面的框架
   
   

模块部署之模块管理：
新增模块支持.zip .tar.gz .tar.bz2压缩格式的模块包
模块名称：任意取名
调用模块：格式为 '目录名称.' + 'sls文件名' [eg: nrpe_ins.nrpe]

 

新增模块范例：

部署nrpe模块
模块包 nrpe_ins.zip
nrpe_ins目录树
- icinga.tar.bz2 ## nrpe插件包
- nrpe.sls
编写 nrpe.sls
nrpe.sls:
/tmp/icinga.tar.bz2: ## 上传nrpe插件包到远程机器临时目录
file:
- managed
- source: SALTSRC/icinga.tar.bz2 ## SALTSRC为固定格式
- backup: minion
cmd.run:
- name: useradd icinga -s /sbin/nologin;tar jxvf /tmp/icinga.tar.bz2 -C /usr/local/ && chown -R icinga:icinga /usr/local/icinga && echo "/usr/local/icinga/bin/nrpe -c /usr/local/icinga/etc/nrpe.cfg -d" >> /etc/rc.local;/usr/local/icinga/bin/nrpe -c /usr/local/icinga/etc/nrpe.cfg -d && rm -rf /tmp/icinga.tar.bz2 ## 具体执行的命令

模块名称：在这里取名为 Nrpe_Install
调用模块：nrpe_ins.nrpe