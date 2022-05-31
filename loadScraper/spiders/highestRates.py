import scrapy
import json
from loadScraper.items import LoadScraperItem

# currencies = 'usdc,dai,eth,wbtc,btc,renbtc,sbtc,hbtc,uni,comp,crv,yfi,1inch,vsp,zrx,bat,usdt,susd,busd,tusd,pax,gusd,musd,knc,snx,link,mkr,rep,rai,xrp,ltc,eos,hegic,bbtc,frax,ust,alusd,husd,eurs'


class HighestratesSpider(scrapy.Spider):
    name = 'highestRates'
    allowed_domains = ['loanscan.io']
    start_urls = ['https://api.loanscan.io/v1/interest-rates']

    def parse(self, response):
        jsonresponse = json.loads(response.text)

        items = []
        for row in jsonresponse:
            item = LoadScraperItem()
            item['name'] = row.get('provider')
            try:
                item['value'] = list(filter(lambda r: r['symbol'] == 'USDT', row.get('supply')))[0]['rate']
            except IndexError:
                continue
            items.append(item)
        # Sort currencies
        items = sorted(items, key=lambda item: item['value'], reverse=True)

        # yield top 5
        for item in items[:5]:
            yield item
