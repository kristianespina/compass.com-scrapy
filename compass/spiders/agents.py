# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from selenium import webdriver


class AgentsSpider(scrapy.Spider):
    name = 'agents'
    allowed_domains = ['compass.com']
    start_urls = ['http://compass.com/agents']

    def parse(self, response):
        AGENTS_SELECTOR = '/html/body/main/div/div/a/@href'
        for agents in response.xpath(AGENTS_SELECTOR):
            #agents_link.append(agents.xpath('./@href').text())
            yield Request('http://compass.com'+agents.extract(), callback=self.visit_location)

    def visit_location(self, response):
        LOCATION_SELECTOR = '/html/body/main/section/div[1]/span[2]'
        AGENTS_SELECTOR = '/html/body/main/div/div'#+/div/a
        for agent in response.xpath(AGENTS_SELECTOR):
            for link in agent.xpath('./div/a/@href').extract():
                profile_url = 'http://compass.com'+link
                profile = Request(profile_url, callback=self.visit_profile, meta=dict(url=profile_url))
                yield profile
    
    def visit_profile(self, response):
        return {
            'link': response.meta['url'],
            'name': response.xpath('normalize-space(/html/body/main/div[1]/div/div[3]/a/h1/text())').extract_first(),
            'phone': response.xpath('normalize-space(/html/body/main/div[1]/div/div[3]/div[3]/a/text())').extract_first(),
            'email': response.xpath('normalize-space(/html/body/main/div[1]/div/div[3]/div[2]/a/text())').extract_first(),
            'location': response.xpath('normalize-space(/html/body/main/div[1]/div/div[1]/a[2])').extract_first()
        }
