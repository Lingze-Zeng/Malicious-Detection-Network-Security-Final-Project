import pandas as pd
import numpy as np



def duration(date):
    return 2023 - int(date[:4])



def main():
    df = pd.read_csv('ProcessedData_html_whois.csv', nrows = 2)
    date = []
    state_set = set()
    state_map = pd.DataFrame()
    state_count = 0
    registrar_set = set()
    registrar_map = pd.DataFrame()
    registrar_count = 0

    #get duration time
    for i in df['regist_date']:
        date.append(duration(i))
    df.drop('regist_date', axis=1, inplace=True)
    df['duration'] = date

    for index, row in df.iterrows():
        # hash table for states
        if pd.isna(row['state']) and 'None' not in state_set:
            state_set.add('None')
            state_map['None'] = [state_count]
            state_count += 1
        elif row['state'] not in state_set:
            state_set.add(row['state'])
            state_map[row['state']] = [state_count]
            state_count += 1

        if row['state'] in state_set:
            df.at[index, 'state'] = state_map[row['state']].values[0]
        elif pd.isna(row['state']) and 'None' in state_set:
            df.at[index, 'state'] = state_map['None'].values[0]
        #hash table for registrar
        if pd.isna(row['registrar']) and 'None' not in registrar_set:
            registrar_set.add('None')
            registrar_map['None'] = [registrar_count]
            registrar_count += 1
        elif row['registrar'] not in registrar_set:
            registrar_set.add(row['registrar'])
            registrar_map[row['registrar']] = [registrar_count]
            registrar_count += 1

        if row['registrar'] in registrar_set:
            df.at[index, 'registrar'] = registrar_map[row['registrar']].values[0]
        elif pd.isna(row['registrar']) and 'None' in registrar_set:
            df.at[index, 'registrar'] = registrar_map['registrar'].values[0]
    
    state_map.to_csv('state_hash.csv')
    registrar_map.to_csv('registrar_hash.csv')
    df.to_csv('out.csv')
    #print(date)
main()