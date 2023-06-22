import scrapy


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