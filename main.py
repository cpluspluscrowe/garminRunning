from fitparse import FitFile
import os
import pandas
data = "./data"
for file in os.listdir(data):
    if ".fit" in file:
        path = os.path.join(data,file)
        fit_file = FitFile(path)


def get_distinct_keys(fit_file):
    messages = list(fit_file.get_messages())
    message_dict = list(map(lambda x: x.get_values(), messages))
    items = list(map(lambda x: x.items(), message_dict))
    
    filter_none_columns =  list(map(lambda item:list(filter(lambda x: x[1] != None, item)), items))
    
    keys_all = list(map(lambda dict_entry: list(map(lambda x: x[0], dict_entry)), filter_none_columns))
    keys_distinct = set([item for sublist in keys_all for item in sublist])
    filter_out_unknown = list(filter(lambda x: not "unknown_" in x, keys_distinct))
    return filter_out_unknown



keys = get_distinct_keys(fit_file)

print(keys)

#df = pandas.DataFrame(messages)
#df.to_csv("./{0}.csv".format(file), sep=',',index=False)