import aiohttp
import asyncio
import json
from bs4 import BeautifulSoup


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def get_exchange_rate():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = await fetch(url)
    soup = BeautifulSoup(response, 'xml')
    currency_element = soup.find('CharCode', string='USD')
    rate_element = currency_element.find_next_sibling('Value')
    exchange_rate = rate_element.text.replace(',', '.')
    return float(exchange_rate)


def parse_company_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    company_info = []
    company_elements = soup.find_all('tr', class_='table__row')
    for element in company_elements:
        name_element = element.find('a', class_='table__link')
        name = name_element.text.strip()
        code = name_element.find_next_sibling('span').text.strip()
        price = element.find('span', class_='priceText__1853e8a5').text.strip()
        pe_ratio = element.find('span', class_='ratio__dcfda0ef').text.strip()
        growth = element.find('span', class_='percent-change__5e66a71a').text.strip()
        profit_element = element.find('div', class_='text-color-neutral--$label-3__b3e4a577')
        if profit_element is None:
            potential_profit = 'N/A'
        else:
            potential_profit = profit_element.text.strip()
        # Извлечение цен на акции 52 Week Low и 52 Week High
        price_low = element.find_all('td', class_='table__cell--fixed align-right')[0].text.strip()
        price_high = element.find_all('td', class_='table__cell--fixed align-right')[1].text.strip()
        company_data = {
            'code': code,
            'name': name,
            'price': price,
            'P/E': pe_ratio,
            'growth': growth,
            '52 Week Low': price_low,
            '52 Week High': price_high,
            'potential profit': potential_profit
        }
        company_info.append(company_data)
    return company_info


def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


async def get_company_info():
    url = 'https://markets.businessinsider.com/index/components/s&p_500'
    html = await fetch(url)
    company_info = parse_company_info(html)
    return company_info


async def main():
    exchange_rate = await get_exchange_rate()
    company_info = await get_company_info()
    for company in company_info:
        price = company['price']
        price_rub = float(price.replace('$', '')) * exchange_rate
        company['price'] = round(price_rub, 2)
        profit = company['potential profit']
        if profit != 'N/A':
            profit_percent = float(profit.strip('%'))
            low = company['52 Week Low']
            high = company['52 Week High']
            low_price = float(low.replace('$', ''))
            high_price = float(high.replace('$', ''))
            potential_profit = (high_price - low_price) / low_price * 100
            company['potential profit'] = round(potential_profit, 2)
    top_10_expensive = sorted(company_info, key=lambda x: x['price'], reverse=True)[:10]
    top_10_pe = sorted(company_info, key=lambda x: float(x['P/E']) if x['P/E'] != 'N/A' else 0)[:10]
    top_10_growth = sorted(company_info, key=lambda x: float(x['growth'].strip('%')), reverse=True)[:10]
    top_10_profit = sorted(company_info, key=lambda x: x['potential profit'], reverse=True)[:10]
    save_to_json(top_10_expensive, 'data/top_10_expensive.json')
    save_to_json(top_10_pe, 'data/top_10_pe.json')
    save_to_json(top_10_growth, 'data/top_10_growth.json')
    save_to_json(top_10_profit, 'data/top_10_profit.json')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
