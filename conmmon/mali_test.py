


import smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
import time

now = time.strftime('%Y%m%d_%H%M%S')

class MailSender(object):
    "发送邮件类,附件为测试报告"

    def __init__(self, smtp_server='smtp.exmail.gmail.com(邮箱类型)', username='yangxiqq5532@gmail.com', password='yangxi@11'):
        "登录SMTP服务器"
        self._username = username
        self.email_client = smtplib.SMTP(smtp_server)
        self.email_client.login(username, password)

    def quit(self):
        # 结束SMTP会话
        self.email_client.quit()

    def send_mail(self, to_addr, cc_addr, subject, content,report):
        """
        发送邮件
        :param to_addr: 收件人
        :param cc_addr: 抄送人
        :param subject: 邮件标题
        :param content: 正文内容
        :param text_type: plain代表纯文本,html代表支持html文本
        """
        msg= MIMEMultipart()
        msg.attach(MIMEText(content,'html', 'utf-8'))
        msg['Subject'] = subject
        msg['From'] = '自动化测试专用<' + self._username + '>'#邮件中显示的发件人别称
        msg['To'] = ','.join(to_addr)
        msg['Cc']=','.join(cc_addr)
        with open(report,'rb') as f:
            mime = MIMEBase('html', 'html', filename=report)# MIMEBase表示附件的对象
            mime.add_header('Content-Disposition', 'attachment', filename=("gbk", "", "%s测试报告.html"%now))# filename是显示附件名字
            mime.set_payload(f.read())# 获取附件内容
            encoders.encode_base64(mime)
            msg.attach(mime)# 作为附件添加到邮件
        try:
            self.email_client.sendmail(self._username,to_addr+cc_addr,msg.as_string())
            self.email_client.quit()
            print("邮件发送成功！")
        except smtplib.SMTPException:
            print("邮件发送失败！")


if __name__ == '__main__':
    html='../reports/202205015_114022测试报告.html'
    # a = MailSender("smtp.exmail.qq.com","test@sun-tech.cn","Hfclj1987")
    cc = ''' 接口自动化测试用例执行完成！
            <ins>这是自动发送的，附件为自动化测试报告请谷歌浏览器打开！</ins>
          '''
    MailSender().send_mail(['green@earncheese.net'],['收件人'],['email'],['email'],'自动化测试报告',cc,html)



