# -*- coding: utf-8 -*-
import os
from libpycommon.common import misc
from libpycommon.libpycommonkey.me import *
from libpycommon.common import mylog
import smtplib
from email.mime.text import MIMEText

class Email_sender():
    def __init__(self,package_key_res_path):
        self.package_key_res_path=package_key_res_path
        self.mail_host=misc.get_env('SMTP_SMARTHOST') or None
        self.mail_port=misc.get_env('SMTP_SMARTPORT') or None
        self.mail_user=misc.get_env_encrypted('SMTP_AUTH_USERNAME', self.package_key_res_path)
        self.mail_pass=misc.get_env_encrypted('SMTP_AUTH_PASSWORD', self.package_key_res_path)
        self.sender=misc.get_env_encrypted('SMTP_FROM', self.package_key_res_path)
        self.receivers=misc.get_env_encrypted('SMTP_RECEIVERS', self.package_key_res_path).split(',')
    def do_send(self,text,content):
        message = MIMEText(content, 'plain', 'utf-8')
        message['Subject'] = text
        message['From'] = self.sender
        message['To'] = self.receivers[0]
        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host,self.mail_port)
            smtpObj.set_debuglevel(1)
            # smtpObj.ehlo(mail_host)
            # 登录到服务器
            smtpObj.login(self.mail_user, self.mail_pass)
            # 发送
            smtpObj.sendmail(
                self.sender, self.receivers, message.as_string())
            # 退出
            smtpObj.quit()
            mylog.logger.info('email sent success')
        except smtplib.SMTPException as e:
            mylog.logger.info(f'email sent error:{e}')  # 打印错误
