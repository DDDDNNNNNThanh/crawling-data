# -*- coding: utf-8 -*-
import scrapy
from datetime import date, timedelta
from bs4 import BeautifulSoup
import csv

class DataPriceItem(scrapy.Item):
    area = scrapy.Field()
    address = scrapy.Field()
    description = scrapy.Field()
    floor_number = scrapy.Field()
    bedroom_number = scrapy.Field()
    is_dinning_room = scrapy.Field()
    is_kitchen = scrapy.Field()
    is_terrace = scrapy.Field()
    is_car_pack = scrapy.Field()
    is_owner = scrapy.Field()
    start_date = scrapy.Field()
    end_date = scrapy.Field()
    type = scrapy.Field()
    direction = scrapy.Field()
    street_in_front_of_house = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()
    law = scrapy.Field()
    price = scrapy.Field()

class AlonhadatSpider(scrapy.Spider):
    name = 'alonhadat'
    allowed_domains = ['alonhadat.com.vn']
    start_urls = ['http://alonhadat.com.vn/']

    def start_requests(self):
        pages = []
        for i in range(1, 10):
            domain_chothue = 'https://alonhadat.com.vn/nha-dat/cho-thue/trang--{}.html'.format(i)
            domain_canban = 'https://alonhadat.com.vn/nha-dat/can-ban/trang--{}.html'.format(i)
            pages.append((domain_chothue, 'chothue'))
            pages.append((domain_canban, 'canban'))

        for page, category in pages:
            yield scrapy.Request(url=page, callback=self.parse_link, meta={'category': category})

    def parse_link(self, response):
        for i in range(1, 21):
            link_selector = '#left > div.content-items > div:nth-child({}) > div:nth-child(1) > div.ct_title > a::attr(href)'.format(i)
            link = response.css(link_selector).extract_first()
            link = 'https://alonhadat.com.vn/' + link
            yield scrapy.Request(url=link, callback=self.parse, meta={'category': response.meta['category']})

    def parse(self, response):
        item = DataPriceItem()
        item['price'] = self.extract(response, '#left > div.property > div.moreinfor > span.price > span.value')
        item['description'] = self.extract(response, '#left > div.property > div.detail.text-content')
        item['address'] = self.extract(response, '#left > div.property > div.address > span.value')
        item['area'] = self.extract(response, '#left > div.property > div.moreinfor > span.square > span.value')
        item['start_date'] = self.extract(response, '#left > div.property > div.title > span', 'start_date')
        item['end_date'] = None

        result_table = self.extract_table(response.css('table').get())
        item['floor_number'] = result_table[0]
        item['bedroom_number'] = result_table[1]
        item['is_dinning_room'] = result_table[2]
        item['is_kitchen'] = result_table[3]
        item['is_terrace'] = result_table[4]
        item['is_car_pack'] = result_table[5]
        item['is_owner'] = result_table[6]
        item['type'] = result_table[7]
        item['direction'] = result_table[8]
        item['street_in_front_of_house'] = result_table[9]
        item['width'] = result_table[10]
        item['height'] = result_table[11]
        item['law'] = result_table[12]

        if response.meta['category'] == 'chothue':
            with open('cho_thue.csv', 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=item.fields.keys())
                writer.writerow(item)
        elif response.meta['category'] == 'canban':
            with open('can_ban.csv', 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=item.fields.keys())
                writer.writerow(item)

    def extract(self, response, query, para=None):
        query += "::text"
        model = response.css(query).extract_first()

        if model is not None:
            if para == 'start_date' or para == 'end_date':
                now = date.today().strftime("%d/%m/%Y")
                pre = (date.today() - timedelta(1)).strftime("%d/%m/%Y")
                return model.replace("Hôm qua", pre).replace("Hôm nay", now)

        return model

    def extract_table(self, data):
        soup = BeautifulSoup(data, 'lxml')
        result = soup.findAll('td')

        floor_number = result[21].text
        bedroom_number = result[27].text

        is_dinning_room = result[5].text
        if is_dinning_room == "---":
            is_dinning_room = False
        else:
            is_dinning_room = True

        is_kitchen = result[11].text
        if is_kitchen == "---":
            is_kitchen = False
        else:
            is_kitchen = True

        is_terrace = result[17].text
        if is_terrace == "---":
            is_terrace = False
        else:
            is_terrace = True

        is_car_pack = result[23].text
        if is_car_pack == "---":
            is_car_pack = False
        else:
            is_car_pack = True

        is_owner = result[29].text
        if is_owner == "---":
            is_owner = False
        else:
            is_owner = True

        type = result[13].text
        direction = result[3].text
        street_in_front_of_house = result[9].text
        width = result[19].text
        height = result[25].text
        law = result[15].text

        return [floor_number, bedroom_number, is_dinning_room, is_kitchen, is_terrace, is_car_pack,
                is_owner, type, direction, street_in_front_of_house, width, height, law]
