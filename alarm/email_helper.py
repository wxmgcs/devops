# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import time

SMTP_SERVER="smtp.exmail.qq.com"
SMTP_PORT=465
class MyEmail:

    def __init__(self):
        self.user = None
        self.passwd = None
        self.to_list = []
        self.cc_list = []
        self.tag = None
        self.doc = None


    def send(self):
        try:
            server = smtplib.SMTP_SSL(SMTP_SERVER, port=SMTP_PORT)
            server.login(self.user, self.passwd)
            server.sendmail("<%s>" % self.user, self.to_list, self.get_attach())
            server.close()
            print "send email successful"
            return True
        except Exception, e:
            print "send email failed %s", e
            return False

    def get_attach(self):
        attach = MIMEMultipart()
        if self.tag is not None:
            # 主题,最上面的一行
            attach["Subject"] = self.tag.encode("gbk")
        if self.user is not None:
            # 显示在发件人
            attach["From"] = self.user

        if self.doc is not None:
            name = self.doc.encode("gbk")
            attach.set_payload(name)
            # attach= MIMEText(name,)

        if self.to_list:
            # 收件人列表
            attach["To"] = ";".join(self.to_list)
        if self.cc_list:
            # 抄送列表
            attach["Cc"] = ";".join(self.cc_list)

        # if self.doc:
        # #估计任何文件都可以用base64，比如rar等
        #     #文件名汉字用gbk编码代替
        #     name = os.path.basename(self.doc).encode("gbk")
        #     f = open(self.doc,"rb")
        #     doc = MIMEText(f.read(), "base64", "gb2312")
        #     doc["Content-Type"] = 'application/octet-stream'
        #     doc["Content-Disposition"] = 'attachment; filename="'+name+'"'
        #     attach.attach(doc)
        #     f.close()

        return attach.as_string()


def send(user, password, peer, tag, content):
    email = MyEmail()
    email.user = user
    email.passwd = password
    email.to_list = peer
    email.cc_list = ["", ]
    email.tag = tag
    email.doc = content
    email.send()

EMAIL_USER_NAME="ctujk@800617.com"
EMAIL_PASSWORD="ctu800617"
EMAIL_PEER=["wangxiaomin@800617.com",]


def send_mail(title,server):
    content = format_content(server)
    return send(EMAIL_USER_NAME,
         EMAIL_PASSWORD,
         EMAIL_PEER,
         title,
         content)

def format_content(server):
    print server
    return "\r\n".join(server.split(","))

def main():
    try:
        argv = sys.argv
        content = argv[1]
        content = "please check server :\r\n" + content
        send_mail("TEST",content)
    except Exception,ex:
        print ex

        #main()