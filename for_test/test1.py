import smtplib
from email.mime.text import MIMEText
from email.header import Header
from common.configfileparser import ConfigFileParser


class SendEmail:
    def __init__(self, mailcfg, smtpserv, sender_id, sender_pwd, receiver):
        self.cfg = mailcfg
        self.smtpserver = smtpserv
        self.sender = sender_id
        self.sender_pwd = sender_pwd
        self.receiver = receiver

    def set_email_content(self, mail_title):
        # 读取html文件内容，且展示在email正文
        with open(r'D:\PycharmProjects\interfaceTest\reports\2018-06-20-13_32_48_result.html', encoding='utf-8',
                  mode='r') as f:
            mail_body = f.read()

        # 邮件内容, 格式, 编码
        content = MIMEText(mail_body, 'html', 'utf-8')
        content['From'] = self.sender
        content['To'] = ",".join(self.receiver)
        content['Subject'] = Header(mail_title, 'utf-8')
        return content

    def send_email(self, message):
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtpserver)
            smtp.login(self.sender, self.sender_pwd)
            smtp.sendmail(self.sender, self.receiver, message.as_string())
            print("发送邮件成功！！！")
            smtp.quit()
        except smtplib.SMTPException:
            print("发送邮件失败！！！")


if __name__ == '__main__':
    # 获取email服务器配置参数
    m = ConfigFileParser(filename='D:\PycharmProjects\interfaceTest\conf\mail.cfg')
    # ip = m.get_value('mail_server', 'host')
    # port = m.get_value('mail_server', 'port')
    smtpserv = m.get_value('mail_server', 'smtpserver')
    sender = m.get_value('sender', 'mail')
    sender_pwd = m.get_value('sender', 'pwd')
    receivers = m.get_all_values('receiver')

    # 初始化email服务器配置参数
    mail_title = '主题：接口自动化测试报告'
    cf = SendEmail(m, smtpserv, sender, sender_pwd, receivers)
    content = cf.set_email_content(mail_title)
    cf.send_email(content)
