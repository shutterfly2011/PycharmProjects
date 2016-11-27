import scrapy
class HARSpider(scrapy.Spider):
    name = 'brickset_spider'

    def start_requests(self):
        start_urls = ['http: // www.har.com / search / dosearch /?page = 8 & search_id = 1357342 & bedroom_min = 3 & for_sale = 1 & listing_price_max = 270000 & listing_price_min = 125000 & property_class_id = 1 & region_id = 1 & school_dist_id = 42 & year_built_min = 2000']
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            addr_selector = 'mf-tab-mf-mapit'
            cityzip_selector = './/dl[dt/text() = "Pieces"]/dd/a/text()'
            marketarea_selector = ''
            price_selector = ''
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'pieces':brickset.xpath(PIECES_SELECTOR).extract_first()
            }

