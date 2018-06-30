# -*- coding: utf-8 -*-
import scrapy


class PlayerDataSpider(scrapy.Spider):
    name = 'player_data'
    allowed_domains = ['masterfortnite.com']
    start_urls = ['https://masterfortnite.com/leaderboards/pc/overall/wins']

    def parse(self, response):
        #Calling parse details to get player specoific details
        urls = response.css('div.ld-body > div > a::attr(href)').extract()
        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url = url, callback = self.parse_details)



        next_page_url = response.css('div.ld-pagination > a::attr(href)').extract_first()
        
        if int(next_page_url[35:]) <= 200:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url = next_page_url, callback = self.parse)

    #scraping player specific details
    def parse_details(self, response):
        name  = response.xpath('//div[@class="pl-main-headings"]/h1/text()').extract_first()

        #solo
        solo_games = response.xpath('//div[@class="module-heading-secondary text-muted"]//text()').extract()[1]
        solo_wr = response.xpath('//div[@class="chip-value"]//text()').extract()[5]
        solo_kd = response.xpath('//div[@class="chip-value"]//text()').extract()[6]
        solo_score = response.xpath('//div[@class="chip-value"]//text()').extract()[7]
        solo_kills = response.xpath('//div[@class="chip-value"]//text()').extract()[8]
        solo_wins = response.xpath('//div[@class="chip-value"]//text()').extract()[9]
        solo_top10 = response.xpath('//div[@class="chip-value"]//text()').extract()[11]
        solo_top25 = response.xpath('//div[@class="chip-value"]//text()').extract()[12]
        solo_kpm = response.xpath('//div[@class="chip-value"]//text()').extract()[14]


        #duos
        duo_games = response.xpath('//div[@class="module-heading-secondary text-muted"]//text()').extract()[2]
        duo_wr = response.xpath('//div[@class="chip-value"]//text()').extract()[15]
        duo_kd = response.xpath('//div[@class="chip-value"]//text()').extract()[16]
        duo_score = response.xpath('//div[@class="chip-value"]//text()').extract()[17]
        duo_kills = response.xpath('//div[@class="chip-value"]//text()').extract()[18]
        duo_wins = response.xpath('//div[@class="chip-value"]//text()').extract()[19]
        duo_top10 = response.xpath('//div[@class="chip-value"]//text()').extract()[21]
        duo_top25 = response.xpath('//div[@class="chip-value"]//text()').extract()[22]
        duo_kpm = response.xpath('//div[@class="chip-value"]//text()').extract()[24]


        #squads
        squad_games = response.xpath('//div[@class="module-heading-secondary text-muted"]//text()').extract()[3]
        squad_wr = response.xpath('//div[@class="chip-value"]//text()').extract()[25]
        squad_kd = response.xpath('//div[@class="chip-value"]//text()').extract()[26]
        squad_score = response.xpath('//div[@class="chip-value"]//text()').extract()[27]
        squad_kills = response.xpath('//div[@class="chip-value"]//text()').extract()[28]
        squad_wins = response.xpath('//div[@class="chip-value"]//text()').extract()[29]
        squad_top10 = response.xpath('//div[@class="chip-value"]//text()').extract()[31]
        squad_top25 = response.xpath('//div[@class="chip-value"]//text()').extract()[32]
        squad_kpm = response.xpath('//div[@class="chip-value"]//text()').extract()[34]




        yield {
        	'Name': name,
        	'Solo Games': solo_games,
        	'Solo Winrate': solo_wr,
        	'Solo K/D': solo_kd,
        	'Solo Score': solo_score,
        	'Solo Kills': solo_kills,
        	'Solo Wins': solo_wins,
        	'Solo Top 10': solo_top10,
        	'Solo Top 25': solo_top25,
        	'Solo Kills Per Minute': solo_kpm,
        	'Duos Games': duo_games,
        	'Duos Winrate': duo_wr,
        	'Duos K/D': duo_kd,
        	'Duos Score': duo_score,
        	'Duos Kills': duo_kills,
        	'Duos Wins': duo_wins,
        	'Duos Top 10': duo_top10,
        	'Duos Top 25': duo_top25,
        	'Duos Kills Per Minute': duo_kpm,
        	'Squads Games': squad_games,
        	'Squads Winrate': squad_wr,
        	'Squads K/D': squad_kd,
        	'Squads Score': squad_score,
        	'Squads Kills': squad_kills,
        	'Squads Wins': squad_wins,
        	'Squads Top 10': squad_top10,
        	'Squads Top 25': squad_top25,
        	'Squads Kills Per Minute': squad_kpm,
        }
