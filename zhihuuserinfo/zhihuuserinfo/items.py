# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy
#from scrapy import Item ,Field


class zhihuuser(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    gender = scrapy.Field()
    headline = scrapy.Field()
    url_token = scrapy.Field()
    answer_count= scrapy.Field()
    articles_count= scrapy.Field()
    avatar_url= scrapy.Field()
    avatar_url_template= scrapy.Field()
    badge= scrapy.Field()
    follower_count= scrapy.Field()
    is_advertiser= scrapy.Field()
    is_followed= scrapy.Field()
    is_following= scrapy.Field()
    is_org= scrapy.Field()
    type= scrapy.Field()
    url= scrapy.Field()
    user_type= scrapy.Field()






