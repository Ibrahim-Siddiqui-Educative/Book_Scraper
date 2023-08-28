import scrapy


class BookscraperSpider(scrapy.Spider):
    name = "bookscraper"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.css("article.product_pod")        
        for i in range(len(books)):
            title = books[i].css('h3 a').attrib['title']
            print(f"Book title: {title}")

        pass