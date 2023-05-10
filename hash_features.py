import pandas as pd
import re

#show data in csv
def display():
    pd.set_option('display.max_columns', None)

    csv_file_path = 'Hashed_active_feature.csv'

    df = pd.read_csv(csv_file_path)

    print(df.head(1))

#delete a selected column
def delete_column(input,column_name):
    df = pd.read_csv(input)
    df = df.drop(columns=[column_name])

    df.to_csv('output.csv', index=False)

#built a filter to delete selected char
def contains_special_chars(column_name):
    return re.match(r'[\u0000-\u001F\u007F-\u009F\s]+|None', column_name)

#read file and delete special char
def check_state():
    df = pd.read_csv('registrar_hash.csv')
    column_names = df.columns
    filtered_column_names = [col for index, col in enumerate(column_names) if contains_special_chars(col) and index != 0]

    return filtered_column_names

delete_list = check_state()
#buile a filter that change the state
def clear_state(delete_list):
    df = pd.read_csv('output.csv')


    df = df[~df['state'].isin(delete_list)]

    df.to_csv('output_1.csv', index=False)


#delete some unsatisfied states
def clear_state_file(delete_list):
    
    df = pd.read_csv('state_hash.csv')

    cols_to_delete = [col for col in df.columns if any(df[col].isin(delete_list))]

    df = df.drop(columns=cols_to_delete)
    df.to_csv('output_state_hash.csv', index=False)

#build a hash map that change the state
def build_new_state():
    df = pd.read_csv('output_state_hash.csv')

    map = {}
    for index, row in df.iloc[:, :].iterrows():
        sorted_indices = row.argsort()
        sorted_row = pd.Series(range(1, len(row) + 1), index=sorted_indices.index)
        
        for old_value, new_value in zip(row, sorted_row):
            map[new_value] = old_value

    df.to_csv('output_state_hash_after.csv', index=False)
    return map

map_state = build_new_state()


#change state name in the data file
def build_final_state(map_state):
    df = pd.read_csv('output_1.csv')
    column_name = 'state'

    for index, row in df.iterrows():
        old_value = row[column_name]
        
        new_value = old_value
        for key, value in map_state.items():
            if value == old_value:
                new_value = key
                break
        
        df.at[index, column_name] = new_value

    df.to_csv('output_2.csv', index=False)

#build a hash map that change the label name
def label():
    df = pd.read_csv('output_3.csv')
    mapping_dict = {'defacement': 1, 'benign': 2, 'malware': 3, 'phishing': 4}
    map_true = {'TRUE': 1,'FALSE': 0}
    print(df['emptyHTML'])
    df['emptyHTML'] = df['emptyHTML'].astype(int)
    df['javascript'] = df['javascript'].astype(int)
    df.to_csv('output_4.csv', index=False)
label()