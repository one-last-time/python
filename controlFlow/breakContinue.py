headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here

for st in headlines:
    if(len(news_ticker)+len(st)>140):
        break
    news_ticker+=st+" "

news_ticker=news_ticker[:140]

print(news_ticker)