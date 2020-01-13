import scrapy
import json

class BrickSetSpider(scrapy.Spider):
	name="templatescraper"
	def parse(self, response):
		#SET_SELECTOR = '.venue__title'
		SET_SELECTOR = '.venue-card'
		#BrickSetSpider.start_urls.append('https://weddingz.in/banquet-halls/delhi/all')
		for brickset in response.css(SET_SELECTOR):
			yield {
			'name': brickset.css('h2 ::text').extract_first(),	#name of the hall
			'address': brickset.css('div.venue-address ::text').extract_first(),	#price
			'desc': brickset.css('div.venue-desc ::text').extract_first(),
			'price': brickset.css('div.price price ::text').extract_first(),
			#'image': brickset.css('div.lazy[data-original]').attrib['data-original'],
			#'stars': brickset.css('div.value').attrib['style'],
			}
