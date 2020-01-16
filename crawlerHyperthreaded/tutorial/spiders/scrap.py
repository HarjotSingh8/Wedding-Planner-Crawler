import scrapy
import json

class BrickSetSpider(scrapy.Spider):
	name="banquetscraperold"
	start_urls=[]
	def __init__(self, start_url):
		self.start_urls.append(start_url);
		#with open('cities.json') as json_file:
			#data = json.load(json_file)
			#for p in data:
				#print('city: ' + p['city'])
				#BrickSetSpider.start_urls.append('https://weddingz.in/banquet-halls/' + p['city'] + '/all')
				#break
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
			'image': brickset.css('div.image-box[data-original]').attrib['data-original'],
			#'stars': brickset.css('div.value').attrib['style'],
			}
