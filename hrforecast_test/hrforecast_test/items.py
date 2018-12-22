# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class HrforecastItem(scrapy.Item):
    job_title = scrapy.Field()
    employment_type = scrapy.Field()
    company_name = scrapy.Field()
    crawled_date = scrapy.Field()
    tasks = scrapy.Field()
    your_profile = scrapy.Field()
    location = scrapy.Field()
    job_url = scrapy.Field()
    nice_to_have = scrapy.Field()

class GazpromItem(scrapy.Item):
    job_title = scrapy.Field()
    company_name = scrapy.Field()
    crawled_date = scrapy.Field()
    posted_date = scrapy.Field()
    location = scrapy.Field()
    region = scrapy.Field()
    employment_type = scrapy.Field()
    job_id = scrapy.Field()
    job_duties = scrapy.Field()
    job_requirements = scrapy.Field()
    job_url = scrapy.Field()
