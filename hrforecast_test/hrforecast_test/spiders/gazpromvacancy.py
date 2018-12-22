# -*- coding: utf-8 -*-
import scrapy, unicodedata
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from datetime import datetime
from hrforecast_test.items import GazpromItem



class GazpromvacancySpider(CrawlSpider):
    name = 'gazpromvacancy'
    allowed_domains = ['gazpromvacancy.ru']
    start_urls = ['https://www.gazpromvacancy.ru/jobs/']

    rules = (
        Rule(LinkExtractor(restrict_css='.pages'), follow=True),
        Rule(LinkExtractor(restrict_css='.job-list-item h3 a'), callback='parse_item'),
    )

    def parse_item(self, response):
        i = GazpromItem()
        titles = response.css('[class="job-params inline"] dt::text').getall()
        text = [t.strip() for t in response.css('[class="job-params inline"] dd ::text').getall() if t.strip()]

        def get_info(title):
            try:
                return text[titles.index(title)]
            except:
                return None

        def normalize_list(data):
            new_data = []
            for s in data:
                if s.strip():
                    s = s.strip().replace('\t', '')
                    s = unicodedata.normalize("NFKD", s)
                    new_data.append(s)
            return new_data

        i['job_title'] = response.css('h1::text').get()
        i['company_name'] = get_info('Работодатель')
        posted_date = response.css('time::attr(datetime)').get()
        i['posted_date'] = datetime.strptime(posted_date, '%Y-%m-%d')
        i['location'] = get_info('Дислокация')
        i['region'] = get_info('Регион')
        i['employment_type'] = get_info('Режим работы')
        i['job_id'] = get_info('ID вакансии')
        job_duties = response.xpath('//*[text()="Обязанности"]/../*').css('::text').getall()
        i['job_duties'] = normalize_list(job_duties)[1:]
        job_requirements = response.xpath('//*[text()="Требования"]/../*').css('::text').getall()
        i['job_requirements'] = normalize_list(job_requirements)[1:]
        i['job_url'] = response.url
        i['crawled_date'] = datetime.now()

        return i
