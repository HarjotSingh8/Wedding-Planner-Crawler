import scrapy
import json

class BrickSetSpider(scrapy.Spider):
	name="banquetscraper"
	start_urls=[]
	prev = ""
	pgno=1
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
		if self.prev!=response.css('h2 ::text').extract_first():
			#print("name = "+response.css('h2 ::text').extract_first())
			self.prev=response.css('h2 ::text').extract_first()
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
			self.pgno+=1
			yield scrapy.Request(
			response.urljoin(self.start_urls[0]+'?category%5B%5D=banquet-halls&min_price=0&max_price=6000&page={}'.format(self.pgno)),
			callback=self.parse
			)
