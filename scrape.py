from requests_html import HTMLSession

session = HTMLSession()
res = session.get('https://health.google/health-research/imaging-and-diagnostics/?fbclid=IwAR3JE5J3b5gsbVXgV_UyoOPm780yCUCcNigDDmBnDSTz4eTCzFcKEk6DNnU')

articles = res.html.find('.glue-grid')
print(articles)

for article in articles:
    try:
        headline = article.find('.glue-headline', first=True).text
        summary = article.find('.g-h-content-block__text p', first=True).text

    except Exception as e:
        headline = None
        summary = None

    print(headline)
    print(summary)