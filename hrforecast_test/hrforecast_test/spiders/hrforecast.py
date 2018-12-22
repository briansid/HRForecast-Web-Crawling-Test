# -*- coding: utf-8 -*-
import scrapy, datetime
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from hrforecast_test.items import HrforecastItem


class HrforecastSpider(CrawlSpider):
    name = 'hrforecast'
    allowed_domains = ['hrforecast.de']
    start_urls = ['https://www.hrforecast.de/career/']

    rules = (
        Rule(LinkExtractor(restrict_css='[class*=grid-sort-container]'), callback='parse_item'),
    )

    def parse_item(self, response):
        i = HrforecastItem()
        titles = response.css('[itemprop="mainContentOfPage"] [class="avia_textblock  "] strong::text').getall()
        text = response.css('[itemprop="mainContentOfPage"] [class="avia_textblock  "] ::text').getall()
        text = [t.strip() for t in text if t.strip()][1:]
        
        i['job_title'] = titles.pop(0)
        i['employment_type'] = text.pop(0)
        i['company_name'] = 'HRForecast'
        for title in titles[:-1]:
            new_title = title.lower().replace(' ', '_')
            i[new_title] = text[text.index(title)+1 : text.index(titles[titles.index(title)+1])-1]

        i['location'] = titles.pop(-1).split()[-1]
        i['job_url'] = response.url
        i['crawled_date'] = datetime.datetime.now()

        return i
