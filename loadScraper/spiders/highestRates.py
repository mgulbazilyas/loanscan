import scrapy
import json
from ..items import LoadScraperItem

currencies = 'usdc,dai,eth,wbtc,btc,renbtc,sbtc,hbtc,uni,comp,crv,yfi,1inch,vsp,zrx,bat,usdt,susd,busd,tusd,pax,gusd,musd,knc,snx,link,mkr,rep,rai,xrp,ltc,eos,hegic,bbtc,frax,ust,alusd,husd,eurs'


class HighestratesSpider(scrapy.Spider):
    name = 'highestRates'
    allowed_domains = ['loanscan.io']
    start_urls = ['https://rates.loanscan.io/api/v0/rates?targetCurrencies=usd&sourceCurrencies=' + currencies]

    def parse(self, response):
        jsonresponse = json.loads(response.text)

        items = []
        for key, value in jsonresponse.items():
            item = LoadScraperItem()
            item['name'] = key
            item['value'] = value.get('usd')
            items.append(item)
        # Sort currencies
        items = sorted(items, key=lambda item: item['value'], reverse=True)

        # yield top 5
        for item in items[:5]:
            yield item
