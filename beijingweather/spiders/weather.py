# -*- coding: utf-8 -*-

import scrapy
import smtplib
from email.mime.text import MIMEText


class WeatherSpider(scrapy.Spider):
    name = "weather"
    start_urls = [
        "http://www.weather.com.cn/weather/101010100.shtml",
    ]

    def parse(self, response):
        Tod_Weather_Date = response.xpath(
            '//*[@id="7d"]/ul/li[1]/h1/text()').extract()
        Tod_Weather_Wea = response.xpath(
            '//*[@id="7d"]/ul/li[1]/p[1]/text()').extract()
        Tod_Weather_Win = response.xpath(
            '//*[@id="7d"]/ul/li[1]/p[3]/i/text()').extract()
        Tod_Weather_Tem = response.xpath(
            '//*[@id="7d"]/ul/li[1]/p[2]/i/text()').extract()
        Tom_Weather_Date = response.xpath(
            '//*[@id="7d"]/ul/li[2]/h1/text()').extract()
        Tom_Weather_Wea = response.xpath(
            '//*[@id="7d"]/ul/li[2]/p[1]/text()').extract()
        Tom_Weather_Win = response.xpath(
            '//*[@id="7d"]/ul/li[2]/p[3]/i/text()').extract()
        Tom_Weather_Tem = response.xpath(
            '//*[@id="7d"]/ul/li[2]/p[2]/span/text()').extract()

        lst = ['今天日期:' +
               Tod_Weather_Date[0].encode('utf-8'), '\n', '天气:' +
               Tod_Weather_Wea[0].encode('utf-8'), '\n', '低温:' +
               Tod_Weather_Tem[0].encode('utf-8'), "\n", '风力:' +
               Tod_Weather_Win[0].encode('utf-8'), "\n", "\n", '明天日期:' +
               Tom_Weather_Date[0].encode('utf-8'), "\n", '天气情况:' +
               Tom_Weather_Wea[0].encode('utf-8'), "\n", '低温:' +
               Tom_Weather_Tem[0].encode('utf-8'), "\n", '风力:' +
               Tom_Weather_Win[0].encode('utf-8')]

        _user = "XXXXXXXXXX"
        _pwd = "XXXXXXXXXX"
        _to = "XXXXXXXXXX"

        msg = MIMEText(''.join(lst))
        msg["Subject"] = "Two day's weather"
        msg["From"] = _user
        msg["To"] = _to

        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(_user, _pwd)
        s.sendmail(_user, _to, msg.as_string())
        s.quit()
