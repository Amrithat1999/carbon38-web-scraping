import scrapy


class Carbon38Spider(scrapy.Spider):
    name = 'carbon38'
    allowed_domains = ['www.carbon38.com']
    start_urls = ['http://www.carbon38.com/']

    def parse(self, response):
        rows = response.xpath('//div')

        for row in rows:
            colour = row.xpath('./span/span/text()').get()
            breadcrumbs = row.xpath('//ol/li/a/text()').get()
            image_url = row.xpath('./div/img/text()').get()
            brand = row.xpath('./div/div/div/span/a/text()').get()
            product_name = row.xpath('./div/h1/text()').get()
            price = row.xpath('./div/div/div/span/text()').get()
            reviews = row.xpath('./div[6]/p/text()').get()

            sizes = row.xpath('./select/option/text()').get()
            description = row.xpath('./div[4]/span/text()').get()
            sku = row.xpath('./div/p[3]/text()').get()
            product_id = row.xpath('./div/p[4]/text()').get()
            yield {
                'colour': colour,
                'breadcrumbs': breadcrumbs,
                'image_url': image_url,
                'brand': brand,
                'product_name': product_name,
                'price': price,
                'reviews': reviews,
                'sizes': sizes,
                'description': description,
                'sku': sku,
                'product_id': product_id,
            }
# [breadcrumbs,image_url,brand ,product_name ,price ,reviews ,colour,sizes,description,
#  sku,product_id]