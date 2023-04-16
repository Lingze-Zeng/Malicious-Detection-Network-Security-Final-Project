import pandas as pd

df = pd.read_csv('malicious_phish.csv', nrows = 10)
print(df['url'])

def getnumsymb(symb, url):
    count = 0
    for i in url:
        if i == symb:
            count += 1
    return count

def geturlength(url):
    return len(url)

def getdigitnum(url):
    count = 0
    for i in url:
        if i.isdigit():
            count += 1
    return count

temp = []
symb_add = ['-', '@', '~', '_', '%', '?', '&', '#']


for item in df['url']:
    num_sym = getnumsymb('-', item)
    temp.append(num_sym)
df['-'] = temp
print(df)