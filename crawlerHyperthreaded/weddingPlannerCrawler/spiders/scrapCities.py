import scrapy
class CityScrap(scrapy.Spider):
	name="cityscraper"
	start_urls=['https://weddingz.in/']
	def parse(self, response):
		#SET_SELECTOR = '.venue__title'
		SET_SELECTOR = 'ul.dropdown-menu'
		for brickset in response.css(SET_SELECTOR):
			yield {
			'city': brickset.css('a[href]').getall(),	#name of the hall
			#'city': brickset.css('a[href]').re(r'<a href=\s*(.*)')
			#'city': brickset.css('a[href]').re(r'.*"\/(.*)\/')
			'city': brickset.css('a[href]').re(r".*\/(.*)\/")
			#'address': brickset.css('div.venue-address ::text').extract_first(),	#price
			#'desc': brickset.css('div.venue-desc ::text').extract_first(),
			#'price': brickset.css('div.price price ::text').extract_first(),
			#'image': brickset.css('div.lazy[data-original]').attrib['data-original'],
			#'stars': brickset.css('div.value').attrib['style'],
			}
