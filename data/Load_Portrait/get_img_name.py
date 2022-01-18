
import os

file_list = []

def file_name(file_dir, file_list):
    for file in os.listdir(file_dir):
        no_ext = file.split('.')[0]
        year, state, city, school, id = no_ext.split("_")
        file_list.append(no_ext.split("_"))


file_name('D:\portraits\M', file_list)

def sort_by_value(d):
    items=d.items()
    backitems=[[v[1],v[0]] for v in items]
    backitems.sort()
    return [backitems[i][1] for i in range(0,len(backitems))]

dict = {}
for key in file_list:
    dict[key[1]] = dict.get(key[1], 0) + 1
    sorted_state_count = sorted(dict.items(), key=lambda x:x[1])



