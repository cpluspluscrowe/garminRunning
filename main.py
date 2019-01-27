from fitparse import FitFile
import os
import pandas
from collections import defaultdict
from copy import deepcopy

data = "./data"
for file in os.listdir(data):
    if ".fit" in file:
        path = os.path.join(data,file)
        fit_file = FitFile(path)


def get_distinct_keys(messages):
    message_dict = list(map(lambda x: x.get_values(), messages))
    items = list(map(lambda x: x.items(), message_dict))
    
    filter_none_columns =  list(map(lambda item:list(filter(lambda x: x[1] != None, item)), items))
    
    keys_all = list(map(lambda dict_entry: list(map(lambda x: x[0], dict_entry)), filter_none_columns))
    keys_distinct = set([item for sublist in keys_all for item in sublist])
    filter_out_unknown = list(filter(lambda x: not "unknown_" in x, keys_distinct))
    return filter_out_unknown

def create_row_template(columns):
    d = {}#defaultdict(lambda: None)
    for column in columns:
        d[column] = None
    return d

def fill_row(template, message):
    """
    Mutates row to contain garmin data for the given columns
    """
    row = deepcopy(template)
    as_d = message.get_values()
    for key,value in as_d.items():
        if key in row:
            row[key] = value
    return row

def create_df_from_rows(rows):  
    df = pandas.DataFrame([], columns=row_template.keys())
    for row in rows:
        new_df = pandas.DataFrame([list(row.values())], columns = list(row.keys()))
        df = df.append(new_df)
    return df

messages = list(fit_file.get_messages())
keys = get_distinct_keys(messages)
row_template = create_row_template(keys)
rows = list(map(lambda message: fill_row(row_template, message), messages))
df = create_df_from_rows(rows)




#df = pandas.DataFrame(messages)
#df.to_csv("./{0}.csv".format(file), sep=',',index=False)