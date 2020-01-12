import scrapy
class BrickSetSpider(scrapy.Spider):
	name="brickset_spider"
	start_urls=['https://weddingz.in/chandigarh']
	def parse(self, response):
		#SET_SELECTOR = '.venue__title'
		SET_SELECTOR = '.venue_card_data'
		for brickset in response.css(SET_SELECTOR):
			yield {
			'name': brickset.css('h4 ::text').extract_first(),	#name of the hall
			'price': brickset.css('price ::text').extract_first(),	#price
			'price_text': brickset.css('span.price_text ::text').extract_first(),
			'image': brickset.css('div.lazy[data-original]').attrib['data-original'],
			'stars': brickset.css('div.value').attrib['style'],
			}
