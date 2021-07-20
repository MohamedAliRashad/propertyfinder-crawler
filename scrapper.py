from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from datetime import datetime
import argparse

if __name__ == '__main__':
    # Default values
    filename = 'propertyfinder_' + datetime.today().strftime('%d-%m-%Y') + '.csv'
    exporters = {"csv": 'scrapy.exporters.CsvItemExporter', "json": 'scrapy.exporters.JsonItemExporter'}

    # Make the script flexible
    parser = argparse.ArgumentParser(description='Scrap PropertyFinder website.')
    parser.add_argument('-t', '--type', type=str, default='json', choices=["json", "csv"], help='type of output file')
    parser.add_argument('-f', '--file_name', type=str, default=filename, help='name of output file')
    args = parser.parse_args()
    
    # Alter project settings
    settings = get_project_settings()
    settings['FEED_URI'] = args.file_name
    settings['FEED_FORMAT'] = args.type
    settings['FEED_EXPORTERS'] = {args.type: exporters[args.type]}
    settings['FEED_EXPORT_ENCODING'] = 'utf-8'

    # Initialize crawling process
    process = CrawlerProcess(settings)
    
    # Crawl data and hold on until finish
    process.crawl('properties')
    process.start()