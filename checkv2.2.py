import requests
import re
import time
import os

your_name = os.environ["YOUR_NAME"]    #学号
your_pwd = os.environ["YOUR_PWD"]      #密码
wechat_key = os.environ["WECHAT_KEY"]  #server酱
token = os.environ["TOKEN"]            #
telechan_key = os.environ["TELE_KEY"]  #telechan
# 放假
form_data_1 = os.environ["FORM_JIA"]
# 在校
form_data_2 = os.environ["FORM"]
def bot_post(text):
    if wechat_key != "":
        url1 = 'https://sctapi.ftqq.com/' + wechat_key + '.send?title=check_ok' + '&desp='+text+time.strftime("%m-%d", time.localtime())
        requests.get(url1)
    if token  != "":
        print('okk'+token)
        url2 = 'https://telechan8.vercel.app/api/send?sendkey='+telechan_key+'&text='+text+time.strftime("%m-%d", time.localtime())
        requests.get(url2)


def buaaLogin(user_name, password):
    print("统一认证登录")

    postUrl = "https://app.buaa.edu.cn/uc/wap/login/check"
    postData = {
        "username": user_name,
        "password": password,
    }
    responseRes = requests.post(postUrl, data=postData)
    print(f"text = {responseRes.text}")
    return responseRes


def fillForm(res):
    s = requests.session()
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://app.buaa.edu.cn/site/buaaStudentNcov/index',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': res.headers['set-cookie']
    }
    r = s.post('https://app.buaa.edu.cn/buaaxsncov/wap/default/save', data=form_data_2, headers=headers)
    return r


def main():
    result = fillForm(buaaLogin(your_name, your_pwd))
    bot_post(result.text)
    return("DONE")
main()
