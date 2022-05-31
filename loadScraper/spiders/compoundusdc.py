import json
import datetime
import scrapy
from ..items import CompoundItem

class CompoundusdcSpider(scrapy.Spider):
    name = 'compoundusdc'
    allowed_domains = ['loanscan.io']
    start_urls = ['https://api.loanscan.io/v1/interest-rates/historical?provider=CompoundV2&interestRateDomain=Supply&intervaltype=Day&startDateTimestamp=1651449600&tokenSymbol=USDC']

    def parse(self, response):
        jsonresponse = json.loads(response.text)
        for row in jsonresponse:
            item = CompoundItem()
            item['date'] = datetime.datetime.fromisoformat(row.get('date')[:-1])
            item['value'] = row.get('value')
            yield item
