# -*- coding: utf-8 -*-
import scrapy


class FortniteSpider(scrapy.Spider):
    name = 'fortnite'
    allowed_domains = ['masterfortnite.com']
    start_urls = ['https://masterfortnite.com/leaderboards/pc/overall/wins']

    def parse(self, response):
        self.log('Just visited : ' +response.url)
        name = response.xpath('//div[@class="col-5 col-md-3 ld-username"]/text()').extract()
        namee = [x.strip() for x in name]
        while '' in namee:
            namee.remove('')
        

        wins = response.xpath('//span[@class="LD_STAT ld-heading-tag ld-tag-green"]/text()').extract()

        winrate = response.xpath('//span[@class="ld-pb-outer"]/text()').extract()

        kd = response.xpath('//div[@class="col-1 d-none d-lg-block"]/text()').extract()
        kd.pop(0)

        games = response.xpath('//div[@class="col-3 col-md-2 d-none d-md-block"]/text()').extract()

        item = dict({'Name':namee, 'Wins':wins, 'Winrate': winrate, 'k/d': kd, 'Games':games})

        yield item

        next_page_url = response.css('div.ld-pagination > a::attr(href)').extract_first()
        
        if int(next_page_url[35:]) <= 200:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url = next_page_url, callback = self.parse)

