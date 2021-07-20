import scrapy

class PropertiesSpider(scrapy.Spider):
    name = "properties"
    
    def start_requests(self):
        urls = [
            "https://www.propertyfinder.eg/en/buy/properties-for-sale.html",
            "https://www.propertyfinder.eg/en/rent/properties-for-rent.html",
            "https://www.propertyfinder.eg/en/commercial-rent/properties-for-rent.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        for property in response.css("div.card-list__item"):
            type, bedroom_numbs, bathroom_numbs, area = property.css(
                "p.card__property-amenity::text"
            ).getall()
            data = {
                "price": property.css("span.card__price-value::text").re_first(
                    "(\d+,\d+)"
                ),
                "title": property.css("h2.card__title::text").get(),
                "location": property.css("span.card__location-text::text").get(),
                "property_type": type,
                "number_of_rooms": bedroom_numbs,
                "number_of_bathrooms": bathroom_numbs,
                "property_area": area,
            }
            yield data

        try:
            next_page = response.css("a.pagination__link--next").attrib["href"]
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
        except:
            pass