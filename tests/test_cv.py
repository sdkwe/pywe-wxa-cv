# -*- coding: utf-8 -*-

from pywe_wxa_cv.pywxacv import CV, cv_aicrop, cv_qrcode, cv_superresolution

from local_wecfg_example import IMAGE_PATH, WECHAT


class TestSecCommands(object):
    def test_cv_aicrop(self):
        appid = WECHAT.get('WXA', {}).get('appID')
        appsecret = WECHAT.get('WXA', {}).get('appsecret')
        media_file = open(IMAGE_PATH, 'rb')
        cv = CV(appid=appid, secret=appsecret)
        data = cv.aicrop(img_file=media_file)
        assert isinstance(data, dict)
        assert data.get('errcode') == 0

        data = cv_aicrop(img_file=None, img_file_path=IMAGE_PATH, appid=appid, secret=appsecret)
        assert isinstance(data, dict)
        assert data.get('errcode') == 0

    def test_cv_qrcode(self):
        appid = WECHAT.get('WXA', {}).get('appID')
        appsecret = WECHAT.get('WXA', {}).get('appsecret')
        media_file = open(IMAGE_PATH, 'rb')
        cv = CV(appid=appid, secret=appsecret)
        data = cv.qrcode(img_file=media_file)
        assert isinstance(data, dict)
        assert data.get('errcode') == 0

        data = cv_qrcode(img_file=None, img_file_path=IMAGE_PATH, appid=appid, secret=appsecret)
        assert isinstance(data, dict)
        assert data.get('errcode') == 0

    def test_cv_superresolution(self):
        appid = WECHAT.get('WXA', {}).get('appID')
        appsecret = WECHAT.get('WXA', {}).get('appsecret')
        media_file = open(IMAGE_PATH, 'rb')
        cv = CV(appid=appid, secret=appsecret)
        data = cv.superresolution(img_file=media_file)
        assert isinstance(data, dict)
        assert data.get('errcode') == 0

        data = cv_superresolution(img_file=None, img_file_path=IMAGE_PATH, appid=appid, secret=appsecret)
        assert isinstance(data, dict)
        assert data.get('errcode') == 0
