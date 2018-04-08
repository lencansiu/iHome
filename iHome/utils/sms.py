# coding=gbk

# coding=utf-8

# -*- coding: UTF-8 -*-

from iHome.libs.yuntongxun.CCPRestSDK import REST
import ConfigParser

# ���ʺ�
accountSid = '8aaf0708627645a801629f2b6df30933'

# ���ʺ�Token
accountToken = 'a12376c660d749d1b39d49e2011de10d'

# Ӧ��Id
appId = '8aaf0708627645a801629f2b6e50093a'

# �����ַ����ʽ���£�����Ҫдhttp://
serverIP = 'app.cloopen.com'

# ����˿�
serverPort = '8883'

# REST�汾��
softVersion = '2013-12-26'


class CCP(object):
    """�Զ��嵥���࣬���ڷ��Ͷ���"""

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(CCP, cls).__new__(cls, *args, **kwargs)

            # ��ʼ��REST SDK
            cls._instance.rest = REST(serverIP, serverPort, softVersion)
            cls._instance.rest.setAccount(accountSid, accountToken)
            cls._instance.rest.setAppId(appId)

        return cls._instance

    def send_template_sms(self, to, datas, tempId):
        """�������Ͷ��ŵķ���
        ����ֵ�������1,��ʾ��ͨѶ�����Ƿ��Ͷ����ǳɹ��ģ������0����ʾʧ��
        """

        # result : ����ͨ�Ÿ��߿����ߵĽ����Ϣ
        result = self.rest.sendTemplateSMS(to, datas, tempId)

        # return�Ľ��ֵ���ǿ����߸����û������Ƿ��ͳɹ�
        if result.get('statusCode') == '000000':
            return 1
        else:
            return 0


# ����ģ�����
# @param to �ֻ�����
# @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
# @param $tempId ģ��Id
#
#
# def sendTemplateSMS(to, datas, tempId):
#
#
#     # ��ʼ��REST SDK
#     rest = REST(serverIP, serverPort, softVersion)
#     rest.setAccount(accountSid, accountToken)
#     rest.setAppId(appId)
#
#     result = rest.sendTemplateSMS(to, datas, tempId)
#     for k, v in result.iteritems():
#
#         if k == 'templateSMS':
#                 for k, s in v.iteritems():
#                     print '%s:%s' % (k, s)
#         else:
#             print '%s:%s' % (k, v)
#
# # ����1:Ŀ���ֻ�
# # ����2����һ��Ԫ�أ�������֤�룻�ڶ���������������֤�����Ч��
# # ����3�����ŵ�ģ�壬Ĭ���ṩ��ģ���id��1
# sendTemplateSMS('18122554500', ['666666', '5'], '1')