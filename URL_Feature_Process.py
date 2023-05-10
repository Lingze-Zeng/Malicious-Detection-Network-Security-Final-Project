import pandas as pd
from urllib.parse import urlsplit, urlparse, parse_qs
from tqdm import tqdm
import whois
df = pd.read_csv('active_feature_extracted.csv')
# get special symbol count
def getnumsymb(symb, url):
    count = 0
    for i in url:
        if i == symb:
            count += 1
    return count

# get URL length
def geturlength(url):
    return len(url)

# get digit number count
def getdigitnum(url):
    count = 0
    for i in url:
        if i.isdigit():
            count += 1
    return count

# get sensitive words count
def getsensitivenum(url):
    count = 0
    for i in sensitive:
        if i in url:
            count += 1
    return count

# get host name length
def gethostnamelength(url):
    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url))
    return len(base_url)

# get length part of query part
def getquerylength(url):
    parse_result = urlparse(url)
    return len(parse_result.query)

# get whois information
def getwhois(url):
    try:
        w = whois.whois(url)
    except:
        pass
    registrar = ''
    domain = ''
    date = ''
    state = ''
    try:
        registrar = w['registrar']
    except:
        pass
    try:
        domain = w['domain_name']
    except:
        pass
    try:
        if type(w['creation_date']) is list:
            date = w['creation_date'][0].year
        else:
         date = w['creation_date'].year
    except:
        pass
    try:
        state = w['state']
    except:
        pass
    return registrar, domain, date, state

# selected special symbols
symb_add = ['-', '@', '~', '_', '%', '?', '&', '#']
# selected sensitive words
sensitive = ['secure', 'account', 'webscr', 'login', 'ebayisapi', 'sign in', 'banking', 'confirm']

def main():
    df_new = df.rename(columns={'0':'url', '1':'label', '2':'response status', '3':'active bool', '4':'html'})
    df_res = pd.DataFrame()
    url = []
    label = []
    respstatus = []
    active = []
    html = []

    for index, row in df_new.iterrows():
        if row['active bool'] == 1:
            url.append(row['url'])
            label.append(row['label'])
            respstatus.append(row['response status'])
            active.append(row['active bool'])
            html.append(row['html'])
    df_res['url'] = url
    df_res['label'] = label
    df_res['response status'] = respstatus
    df_res['active bool'] = active
    df_res['html'] = html


    for symb in tqdm(symb_add):
        temp = []
        for item in df_res['url']:
            num_sym = getnumsymb(symb, item)
            temp.append(num_sym)

        df_res[symb] = temp

    urlength = []
    digitnum = []
    sensitivenum = []
    hostlength = []
    querylength = []
    domainname = []
    creatime = []
    registrar = []
    state_name = []
    for item in tqdm(df['url']):
        urlength.append(geturlength(item))
        digitnum.append(getdigitnum(item))
        sensitivenum.append(getsensitivenum(item))
        hostlength.append(gethostnamelength(item))
        querylength.append(getquerylength(item))
        registrar_name, domain, regist_date, state = getwhois(item)
        domainname.append(domain)
        creatime.append(regist_date)
        registrar.append(registrar_name)
        state_name.append(state)
    df_res['urlength'] = urlength
    df_res['digitnum'] = digitnum
    df_res['sensitivenum'] = sensitivenum
    df_res['hostlength'] = hostlength
    df_res['querylength'] = querylength
    df_res['domain_name'] = domainname
    df['regist_date'] = creatime
    df_res['registrar'] = registrar
    df_res['state'] = state_name
    df.to_csv('out.csv')

main()