# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
import glob
import os

class VnexpressThoisuSpider(scrapy.Spider):
	name = 'vnexpress_thoisu'
	allowed_domains = ['vnexpress.net']
	start_urls = ['https://vnexpress.net/category/day/page/22.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/21.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/20.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/19.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/18.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/17.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/16.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/15.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/14.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/13.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/12.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/11.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/10.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/9.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/8.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/7.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/6.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/5.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/4.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/3.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/2.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||',
	'https://vnexpress.net/category/day/page/1.html?cateid=1001005&fromdate=1556643600&todate=1559666160&allcate=1001005||'
	]
	
	def parse(self, response):
		list_of_files = glob.glob('C:/Users/pupper/newscrawler/thoisu/*.txt')
		latest_file = max(list_of_files, key=os.path.getctime)			
		fileName = latest_file[35:]		
		fileName = fileName.replace("thoisu","")
		fileName = fileName.replace(".txt","")		
		number=int(fileName)		
		
		print("procesing:"+response.url)
		#Extract data using css selectors		
		descriptions=response.css('.description::text').extract()                      
		
		row_data=zip(descriptions)

        #Making extracted data row wise
		for item in row_data:
            #create a dictionary to store the scraped info
			filename='./thoisu/thoisu'
			filename+=str(number)
			filename+='.txt'
			with open(filename, 'a') as f:				
				f.write(item[0].encode('utf-8').strip())
			number+=1
			
class ThanhnienThoisuSpider(scrapy.Spider):
    name = 'thanhnien_thoisu'
    allowed_domains = ['thanhnien.vn']
    start_urls = ['https://thanhnien.vn/thoi-su/',
	'https://thanhnien.vn/thoi-su/trang-2.html',
	'https://thanhnien.vn/thoi-su/trang-3.html',
	'https://thanhnien.vn/thoi-su/trang-4.html',
	'https://thanhnien.vn/thoi-su/trang-5.html',
	'https://thanhnien.vn/thoi-su/trang-6.html',
	'https://thanhnien.vn/thoi-su/trang-7.html',
	'https://thanhnien.vn/thoi-su/trang-8.html',
	'https://thanhnien.vn/thoi-su/trang-9.html',
	'https://thanhnien.vn/thoi-su/trang-10.html',
	'https://thanhnien.vn/thoi-su/trang-11.html',
	'https://thanhnien.vn/thoi-su/trang-12.html',
	'https://thanhnien.vn/thoi-su/trang-13.html',
	'https://thanhnien.vn/thoi-su/trang-14.html',
	'https://thanhnien.vn/thoi-su/trang-15.html',
	'https://thanhnien.vn/thoi-su/trang-16.html',
	'https://thanhnien.vn/thoi-su/trang-17.html',
	'https://thanhnien.vn/thoi-su/trang-18.html',
	'https://thanhnien.vn/thoi-su/trang-19.html',
	'https://thanhnien.vn/thoi-su/trang-20.html',
	'https://thanhnien.vn/thoi-su/trang-21.html',
	'https://thanhnien.vn/thoi-su/trang-22.html',
	]

    def parse(self, response):
		list_of_files = glob.glob('C:/Users/pupper/newscrawler/thoisu/*.txt')
		latest_file = max(list_of_files, key=os.path.getctime)			
		fileName = latest_file[35:]		
		fileName = fileName.replace("thoisu","")
		fileName = fileName.replace(".txt","")		
		number=int(fileName)		
		
		print("procesing:"+response.url)
		#Extract data using css selectors		
		descriptions=response.css('.summary div::text').extract()                      
		
		row_data=zip(descriptions)

        #Making extracted data row wise
		for item in row_data:
            #create a dictionary to store the scraped info
			filename='./thoisu/thoisu'
			filename+=str(number)
			filename+='.txt'
			if len(item[0])>5:
				with open(filename, 'a') as f:				
					f.write(item[0].encode('utf-8').strip())
				number+=1
				
class NLDThoisuSpider(scrapy.Spider):
    name = 'nld_thoisu'
    allowed_domains = ['nld.com.vn']
    start_urls = ['https://nld.com.vn/thoi-su/xem-theo-ngay-01-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-01-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-01-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-02-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-02-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-02-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-03-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-03-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-03-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-04-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-04-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-05-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-05-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-05-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-06-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-06-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-06-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-07-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-07-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-07-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-08-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-08-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-08-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-09-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-09-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-09-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-10-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-10-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-10-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-11-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-11-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-11-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-12-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-12-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-13-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-13-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-14-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-14-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-14-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-15-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-15-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-15-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-16-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-16-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-16-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-17-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-17-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-18-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-19-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-19-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-20-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-20-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-20-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-21-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-21-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-21-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-22-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-22-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-22-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-23-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-23-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-23-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-24-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-24-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-24-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-25-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-25-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-25-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-26-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-26-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-27-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-27-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-27-05-2019/trang-3.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-28-05-2019.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-28-05-2019/trang-2.htm',
	'https://nld.com.vn/thoi-su/xem-theo-ngay-28-05-2019/trang-3.htm'
	]

    def parse(self, response):
		list_of_files = glob.glob('C:/Users/pupper/newscrawler/thoisu/*.txt')
		latest_file = max(list_of_files, key=os.path.getctime)			
		fileName = latest_file[35:]		
		fileName = fileName.replace("thoisu","")
		fileName = fileName.replace(".txt","")		
		number=int(fileName)		
		
		print("procesing:"+response.url)
		#Extract data using css selectors		
		descriptions=response.css('.threaditem-btl p::text').extract()                      
		
		row_data=zip(descriptions)

        #Making extracted data row wise
		for item in row_data:
            #create a dictionary to store the scraped info
			filename='./thoisu/thoisu'
			filename+=str(number)
			filename+='.txt'
			if len(item[0])>5:
				with open(filename, 'a') as f:				
					f.write(item[0].encode('utf-8').strip())
				number+=1

process = CrawlerProcess()
process.crawl(VnexpressThoisuSpider)
process.crawl(ThanhnienThoisuSpider)
process.crawl(NLDThoisuSpider)
process.start()