import os

file_list_f = []
file_list_m = []

def file_name(file_dir, file_list):
    for file in os.listdir(file_dir):
        no_ext = file.split('.')[0]
        #year, state, city, school, id = no_ext.split("_")
        file_list.append(file)

file_name('D:\portraits\F', file_list_f)
file_name('D:\portraits\M', file_list_m)

f = open('C:/Users/tianyi_liu/Downloads/SENTRY-main/SENTRY/data/Portrait/txt/1951_2000.txt','w')
for i in range(len(file_list_f)):
    img_name = ''.join(file_list_f[i])
    if int(img_name[0:4]) in range(1951, 2001):
        f.write('F/' + img_name + ' 0\n')

for i in range(len(file_list_m)):
    img_name = ''.join(file_list_m[i])
    if int(img_name[0:4]) in range(1951, 2001):
        f.write('M/' + img_name + ' 1\n')


f.close()