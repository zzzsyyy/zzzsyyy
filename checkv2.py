import requests
import re
import time

###########用户需要更改的部分###############
your_name = '20241011'
your_pwd = 'bh963852@a'
#wechat_key = 'SCT24079TFOE3gZgTWPjQN0STrzWHhCDk'
token = '1769355677:AAGyLWt4Dxn4ebz5sTDY_vPMd_I_RIdvC1E'
chat_id = '1377469440'
form_data = 'sfzs=1&bzxyy=&bzxyy_other=&brsfzc=1&tw=&sfcxzz=&zdjg=&zdjg_other=&sfgl=&gldd=&gldd_other=&glyy=&glyy_other=&gl_start=&gl_end=&sfmqjc=&sfzc_14=1&sfqw_14=0&sfqw_14_remark=&sfzgfx=0&sfzgfx_remark=&sfjc_14=0&sfjc_14_remark=&sfjcqz_14=0&sfjcqz_14_remark=&sfgtjz_14=0&sfgtjz_14_remark=&szsqqz=0&sfyqk=&szdd=1&area=%E5%8C%97%E4%BA%AC%E5%B8%82%20%E6%B5%B7%E6%B7%80%E5%8C%BA&city=%E5%8C%97%E4%BA%AC%E5%B8%82&province=%E5%8C%97%E4%BA%AC%E5%B8%82&address=%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B5%B7%E6%B7%80%E5%8C%BA%E8%8A%B1%E5%9B%AD%E8%B7%AF%E8%A1%97%E9%81%93%E5%8C%97%E4%BA%AC%E8%88%AA%E7%A9%BA%E8%88%AA%E5%A4%A9%E5%A4%A7%E5%AD%A6%E5%8C%97%E4%BA%AC%E8%88%AA%E7%A9%BA%E8%88%AA%E5%A4%A9%E5%A4%A7%E5%AD%A6%E5%AD%A6%E9%99%A2%E8%B7%AF%E6%A0%A1%E5%8C%BA&geo_api_info=%7B%22type%22%3A%22complete%22%2C%22position%22%3A%7B%22Q%22%3A39.983490939671%2C%22R%22%3A116.34865939670203%2C%22lng%22%3A116.348659%2C%22lat%22%3A39.983491%7D%2C%22location_type%22%3A%22html5%22%2C%22message%22%3A%22Get%20ipLocation%20failed.Get%20geolocation%20success.Convert%20Success.Get%20address%20success.%22%2C%22accuracy%22%3A178%2C%22isConverted%22%3Atrue%2C%22status%22%3A1%2C%22addressComponent%22%3A%7B%22citycode%22%3A%22010%22%2C%22adcode%22%3A%22110108%22%2C%22businessAreas%22%3A%5B%7B%22name%22%3A%22%E4%BA%94%E9%81%93%E5%8F%A3%22%2C%22id%22%3A%22110108%22%2C%22location%22%3A%7B%22Q%22%3A39.99118%2C%22R%22%3A116.34157800000003%2C%22lng%22%3A116.341578%2C%22lat%22%3A39.99118%7D%7D%5D%2C%22neighborhoodType%22%3A%22%E7%94%9F%E6%B4%BB%E6%9C%8D%E5%8A%A1%3B%E7%94%9F%E6%B4%BB%E6%9C%8D%E5%8A%A1%E5%9C%BA%E6%89%80%3B%E7%94%9F%E6%B4%BB%E6%9C%8D%E5%8A%A1%E5%9C%BA%E6%89%80%22%2C%22neighborhood%22%3A%22%E5%8C%97%E4%BA%AC%E8%88%AA%E7%A9%BA%E8%88%AA%E5%A4%A9%E5%A4%A7%E5%AD%A6%22%2C%22building%22%3A%22%22%2C%22buildingType%22%3A%22%22%2C%22street%22%3A%22%E5%8C%97%E5%9B%9B%E7%8E%AF%E4%B8%AD%E8%B7%AF%22%2C%22streetNumber%22%3A%22238%E5%8F%B7%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22province%22%3A%22%E5%8C%97%E4%BA%AC%E5%B8%82%22%2C%22city%22%3A%22%22%2C%22district%22%3A%22%E6%B5%B7%E6%B7%80%E5%8C%BA%22%2C%22township%22%3A%22%E8%8A%B1%E5%9B%AD%E8%B7%AF%E8%A1%97%E9%81%93%22%7D%2C%22formattedAddress%22%3A%22%E5%8C%97%E4%BA%AC%E5%B8%82%E6%B5%B7%E6%B7%80%E5%8C%BA%E8%8A%B1%E5%9B%AD%E8%B7%AF%E8%A1%97%E9%81%93%E5%8C%97%E4%BA%AC%E8%88%AA%E7%A9%BA%E8%88%AA%E5%A4%A9%E5%A4%A7%E5%AD%A6%E5%8C%97%E4%BA%AC%E8%88%AA%E7%A9%BA%E8%88%AA%E5%A4%A9%E5%A4%A7%E5%AD%A6%E5%AD%A6%E9%99%A2%E8%B7%AF%E6%A0%A1%E5%8C%BA%22%2C%22roads%22%3A%5B%5D%2C%22crosses%22%3A%5B%5D%2C%22pois%22%3A%5B%5D%2C%22info%22%3A%22SUCCESS%22%7D&gwdz=&is_move=0&move_reason=&move_remark=&realname=%E5%BC%A0%E5%96%84%E8%8B%B1&number=20241011&uid=408994&created=1616750992&date=20210326&id=706077&gwszdd='
###########用户需要更改的部分###############

def bot_post(text):
    #url = 'https://sctapi.ftqq.com/' + wechat_key + '.send?title=check_ok' + '&desp='+text+time.strftime("%m-%d", time.localtime())
    url = 'https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+chat_id+'&text='+text+time.strftime("%m-%d", time.localtime())
    requests.get(url)


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
    r = s.post('https://app.buaa.edu.cn/buaaxsncov/wap/default/save', data=form_data, headers=headers)
    return r


def main(event, context):
    result = fillForm(buaaLogin(your_name, your_pwd))
    bot_post(result.text)
    return("DONE")
