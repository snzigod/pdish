# -*- coding:UTF-8 -*-
import time
import requests
import json
import logging


class BaseClass(object):
    # 定义 API域名
    baseurl = 'http://172.168.254.12:8557/'
    # 定认 headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Content-Type': 'application/json',
        'UserId': '2234234',  # 用户id
        'AccessToken': 'w1dotkwik4STbWR0dCJAQSsTp7puPncLb'  # 用户口令牌
    }

    def __Req(self, type, url, data, timeout=10, showheader=True):
        start = time.time()
        print('请求：' + url)
        try:
            if type == 'post':
                response = requests.post(url, timeout=timeout, headers=self.headers,
                                         data=json.dumps(data))
            else:
                response = requests.get(url, timeout=timeout, headers=self.headers)
            if (showheader):
                print('Response Header:{0}'.format(response.headers))
                print('Response Body:')
            if 'application/json' in response.headers['Content-Type']:
                result = json.loads(response.content.decode('utf-8'))
                # print(result)
                self.PrintJson(result)
                end = time.time()
                print('耗时：%f 秒' % (end - start))
                return result
            elif 'application/octet-stream' in response.headers['Content-Type']:
                print("响应内容为：文件流，流长度 %d" % len(response.content))
            else:
                print("Content-Type：%s" % str(response.headers['Content-Type']))
                print(response.content.decode('utf-8'))
        except requests.exceptions.Timeout:
            print('错误：请求超时')
        except Exception as e:
            logging.exception(e)
        end = time.time()
        print('耗时：%f 秒' % (end - start))

    def ApiPost(self, url, data, timeout=10, showheader=True):
        return self.__Req('post', url, data, timeout=timeout, showheader=showheader)

    def ApiGet(self, url, timeout=10, showheader=True):
        return self.__Req('get', url, '', timeout=timeout, showheader=showheader)

    def __PrintDict(self, dit, level=0):
        for i, e in enumerate(dit):
            t = '\t' * level
            fstr = t
            if type(dit[e]) == type({'p1': 'v1'}):
                fstr += '"{0}":{{'
                print(fstr.format(e))
                self.__PrintDict(dit[e], level + 1)
                t += '}'
                if i < len(dit) - 1:
                    t += ','
                print(t)
            elif type(dit[e]) == type([{'p1': 'v1'}]):
                # 列表数据为空
                if len(dit[e]) == 0:
                    fstr += '"{0}":[]'
                    if i < len(dit) - 1:
                        fstr += ','
                    print(fstr.format(e))
                    continue
                fstr += '"{0}":[{{'
                print(fstr.format(e))
                self.__PrintList(dit[e], level + 1)
                t += '}]'
                if i < len(dit) - 1:
                    t += ','
                print(t)
            elif dit[e] == True or dit[e] == False:
                t += '"{0}":{1}'
                if i < len(dit) - 1:
                    t += ','
                print(t.format(e, str(dit[e]).lower()))
            elif type(dit[e]) == type('abc'):
                t += '"{0}":"{1}"'
                if i < len(dit) - 1:
                    t += ','
                print(t.format(e, dit[e]))
            else:
                t += '"{0}":{1}'
                if i < len(dit) - 1:
                    t += ','
                print(t.format(e, dit[e]))

    def __PrintList(self, list, level=0):
        if level > 0:
            level -= 1
        t = '\t' * level
        for i, e in enumerate(list):
            if i > 0:
                print(t + '},{')
            self.__PrintDict(e, level + 1)

    def PrintJson(self, data):
        if type(data) == type({'p1': 'v1'}):
            print('{')
            self.__PrintDict(data, level=1)
            print('}')
        else:
            print('[')
            self.__PrintList(data, level=1)
            print(']')


if __name__ == "__main__":
    b = BaseClass()
    b.ApiGet("http://www.iflytek.com")
