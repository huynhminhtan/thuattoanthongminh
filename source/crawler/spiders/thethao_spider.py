# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
import glob
import os

class VnexpressThethaoSpider(scrapy.Spider):
	name = 'vnexpress_thethao'
	allowed_domains = ['vnexpress.net']
	start_urls = ['https://vnexpress.net/category/day/page/1.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/2.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/3.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/4.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/5.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/6.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/7.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/8.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/9.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/10.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/11.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/12.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/13.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/14.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/15.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/16.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/17.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/18.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/19.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/20.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/21.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/22.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/23.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/24.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/25.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/26.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/27.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/28.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/29.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/30.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/31.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||',
	'https://vnexpress.net/category/day/page/32.html?cateid=1002565&fromdate=1556643600&todate=1559752560&allcate=1002565||'
	]
	
	def parse(self, response):
		list_of_files = glob.glob('C:/Users/pupper/newscrawler/thethao/*.txt')
		latest_file = max(list_of_files, key=os.path.getctime)			
		fileName = latest_file[36:]		
		fileName = fileName.replace("thethao","")
		fileName = fileName.replace(".txt","")		
		number=int(fileName)		
		
		print("procesing:"+response.url)
		#Extract data using css selectors		
		descriptions=response.css('.description::text').extract()                      
		
		row_data=zip(descriptions)

        #Making extracted data row wise
		for item in row_data:
            #create a dictionary to store the scraped info
			filename='./thethao/thethao'
			filename+=str(number)
			filename+='.txt'
			with open(filename, 'a') as f:				
				f.write(item[0].encode('utf-8').strip())
			number+=1

class ThanhnienThethaoSpider(scrapy.Spider):
    name = 'thanhnien_thoisu'
    allowed_domains = ['thanhnien.vn']
    start_urls = ['https://thethao.thanhnien.vn/toan-canh-the-thao/',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-2.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-3.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-4.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-5.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-6.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-7.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-8.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-9.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-10.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-11.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-12.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-13.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-14.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-15.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-16.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-17.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-18.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-19.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-20.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-21.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-22.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-23.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-24.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-25.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-26.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-27.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-28.html',
	'https://thethao.thanhnien.vn/toan-canh-the-thao/trang-29.html',
	]

    def parse(self, response):
		list_of_files = glob.glob('C:/Users/pupper/newscrawler/thethao/*.txt')
		latest_file = max(list_of_files, key=os.path.getctime)			
		fileName = latest_file[36:]		
		fileName = fileName.replace("thethao","")
		fileName = fileName.replace(".txt","")		
		number=int(fileName)		
		
		print("procesing:"+response.url)
		#Extract data using css selectors		
		descriptions=response.css('.summary div::text').extract()                      
		
		row_data=zip(descriptions)

        #Making extracted data row wise
		for item in row_data:
            #create a dictionary to store the scraped info
			filename='./thethao/thethao'
			filename+=str(number)
			filename+='.txt'
			if len(item[0])>5:
				with open(filename, 'a') as f:				
					f.write(item[0].encode('utf-8').strip())
				number+=1

class NLDThethaoSpider(scrapy.Spider):
    name = 'nld_thethao'
    allowed_domains = ['nld.com.vn']
    start_urls = ['https://nld.com.vn/the-thao/xem-theo-ngay-01-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-01-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-01-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-02-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-02-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-02-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-03-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-03-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-03-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-04-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-04-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-05-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-05-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-05-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-06-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-06-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-06-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-07-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-07-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-07-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-08-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-08-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-08-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-09-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-09-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-09-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-10-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-10-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-10-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-11-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-11-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-11-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-12-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-12-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-13-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-13-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-14-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-14-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-14-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-15-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-15-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-15-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-16-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-16-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-16-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-17-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-17-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-18-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-19-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-19-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-20-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-20-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-20-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-21-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-21-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-21-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-22-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-22-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-22-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-23-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-23-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-23-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-24-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-24-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-24-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-25-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-25-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-25-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-26-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-26-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-27-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-27-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-27-05-2019/trang-3.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-28-05-2019.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-28-05-2019/trang-2.htm',
	'https://nld.com.vn/the-thao/xem-theo-ngay-28-05-2019/trang-3.htm'
	]

    def parse(self, response):
		list_of_files = glob.glob('C:/Users/pupper/newscrawler/thethao/*.txt')
		latest_file = max(list_of_files, key=os.path.getctime)			
		fileName = latest_file[36:]		
		fileName = fileName.replace("thethao","")
		fileName = fileName.replace(".txt","")		
		number=int(fileName)		
		
		print("procesing:"+response.url)
		#Extract data using css selectors		
		descriptions=response.css('.threaditem-btl p::text').extract()                      
		
		row_data=zip(descriptions)

        #Making extracted data row wise
		for item in row_data:
            #create a dictionary to store the scraped info
			filename='./thethao/thethao'
			filename+=str(number)
			filename+='.txt'
			if len(item[0])>5:
				with open(filename, 'a') as f:				
					f.write(item[0].encode('utf-8').strip())
				number+=1
				
process = CrawlerProcess()
process.crawl(NLDThethaoSpider)
process.crawl(VnexpressThethaoSpider)
process.crawl(ThanhnienThethaoSpider)
process.start()