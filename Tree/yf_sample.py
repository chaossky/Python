import yfinance as yf

ticker=yf.Ticker("AAPL")

hist=ticker.history(period="1y")
print(hist.head())

data=ticker.history(start="2023-01-01",end="2023-01-31")

info=ticker.info
print(info['sector'])
print(info['dividendYield'])

news=ticker.news
# print(news[0]['title'])
for item in news[:3]: # 첫 3개 뉴스만 확인 
    print("링크:", item.get("link")) 
    print("발행자:", item.get("publisher")) 
    print("발행시간:", item.get("providerPublishTime")) 
    print("제목:", item.get("title", "제목 없음")) 
    print("-" * 40)

options=ticker.options

opt=ticker.option_chain('2023-12-15')
print(opt.calls)
print(opt.puts)