import scrapy


class BookscraperSpider(scrapy.Spider):
    name = "bookscraper"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css("article.product_pod")        
        for i in range(len(books)):
            title, link, price = self.parse_books(books[i])
            print(f"Book Title: {title}, Book Price: {price} and Book Link: {link}")

        pass

    def parse_books(self, book):

        title = book.css('h3 a').attrib["title"]
        link = book.css('h3 a').attrib["href"]
        price = book.css('.product_price .price_color::text').get()
        
        return title, link, price