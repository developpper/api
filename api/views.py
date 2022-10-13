from django.shortcuts import render
import yaml
# import os

from selectorlib import Extractor
import requests 
import json 
from time import sleep
import yaml
import os

from api.nss.models import AmazonProducts


module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'selectors.yml')
url_path = os.path.join(module_dir, 'urls.txt')
json_path = os.path.join(module_dir, 'output.jsonl')


def scrape(url):
    e = Extractor.from_yaml_file(file_path)
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.ae/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Download the page using requests
    print("Downloading %s"%url)
    r = requests.get(url, headers=headers)
    d = e.extract(r.text)
    # print(d['images'][0])
    
    amazon_item = AmazonProducts.objects.filter(amazon_link = url).first()
    if amazon_item is not None:
        image = d['images'][2:64]
        # listRes = list(ls.split(" "))
        print(image)
        # print(amazon_item.name ,'/', d['name'])
        name = d['name']
        a = str(d['price'])
        a_p = a.replace('AED', '')
        amazon_item.amazon_price = a_p
        if name:
            amazon_item.name = d['name']
        amazon_item.save()
        if image:
            amazon_item.image = image
        amazon_item.save()
    else:
        print('no amazon item')

    # print(d['price'])
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
        return None
    # Pass the HTML of the page and create 
    return e.extract(r.text)


# Create your views here.
# def sc(url):
#     with open(url_path,'r') as urllist, open(json_path,'w') as outfile:
#         for url in urllist.read().splitlines():
#             data = scrape(url) 
#             if data:
#                 json.dump(data,outfile)
#                 outfile.write("\n")
#     return render(url, 'index.html', data)

# Create your views here.
def sc(url):
    # amazon_item = AmazonProducts.objects.filter(amazon_link = url).first()
    for am in AmazonProducts.objects.all():
        # print('-', am.amazon_link)
        scrape(am.amazon_link)
        # compatibles = list(mobile.name.all())
        # if not compatibles:
        #     print('(no compatibility)')
        # else:
        #     comp_list = ', '.join((c.name for c in compatibles))
        #     print(f'-- (same with {comp_list})')
    return render(url, 'index.html')