# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from hrforecast_test.models import (HRForecastJobs,
                                    HRForecastTasks,
                                    HRForecastProfile,
                                    HRForecastNiceToHave,
                                    GazpromJobs,
                                    GazpromJobDuties,
                                    GazpromJobRequirements,
                                    db_connect,
                                    create_table)

class SQLPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()

        def session_add(item):
            try:
                session.add(item)
                session.commit()
            except:
                session.rollback()
                raise

        # Join all lists with newline for Excel
        def listToExcel(item):
            for i in item:
                if type(item[i]) == list:
                    item[i] = '\n'.join(item[i])
            return item

        new_item = item.copy()
        # Sorry I don't wanna make another project
        if spider.name == 'hrforecast':
            tasks = new_item.pop('tasks')
            profiles = new_item.pop('your_profile')
            new_item.pop('crawled_date')
            try:
                nices = new_item.pop('nice_to_have')
            except:
                nices = None

            jobquote = HRForecastJobs(**new_item)
            session_add(jobquote)

            for task in tasks:
                taskquote = HRForecastTasks()
                taskquote.job_id = jobquote.job_id
                taskquote.job_task = task
                session_add(taskquote)

            for profile in profiles:
                profile_quote = HRForecastProfile()
                profile_quote.job_id = jobquote.job_id
                profile_quote.profile = profile
                session_add(profile_quote)

            if nices:
                for nice in nices:
                    nice_quote = HRForecastNiceToHave()
                    nice_quote.job_id = jobquote.job_id
                    nice_quote.nice = nice
                    session_add(nice_quote)

        elif spider.name == 'gazpromvacancy':
            duties = new_item.pop('job_duties')
            requirements = new_item.pop('job_requirements')
            new_item.pop('crawled_date')

            jobquote = GazpromJobs(**new_item)
            session_add(jobquote)

            for dutie in duties:
                dutiequote = GazpromJobDuties()
                dutiequote.job_id = jobquote.id
                dutiequote.dutie = dutie
                session_add(dutiequote)

            for requirement in requirements:
                requirementquote =  GazpromJobRequirements()
                requirementquote.job_id = jobquote.id
                requirementquote.requirement = requirement
                session_add(requirementquote)

        session.close()

        item = listToExcel(item)
        return item
