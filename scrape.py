import csv

from requests_html import HTMLSession

csv_file = open('AI_health_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video'])

session = HTMLSession()
res = session.get('https://health.google/health-research/imaging-and-diagnostics/?fbclid=IwAR3JE5J3b5gsbVXgV_UyoOPm780yCUCcNigDDmBnDSTz4eTCzFcKEk6DNnU')

# get all the absolute path for the link in the given page
# for link in res.html.absolute_links:
#     print(link)

articles = res.html.find('.glue-grid')
# print(articles)

for article in articles:
    try:
        headline = article.find('.glue-headline', first=True).text
        summary = article.find('.g-h-content-block__text p', first=True).text
        video = article.find('video source', first=True).attrs['src']

    except Exception as e:
        headline = None
        summary = None
        video = None
    # print(video)
    # print(headline)
    # print(summary)
    # print('--------' * 3)

    csv_writer.writerow([headline, summary, video])
csv_file.close()