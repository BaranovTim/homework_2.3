i_1 = 0
i_2 = 0
i_3 = 0
max = 0

with open('1.txt', encoding= 'utf-8')as f_1:
    for line in f_1:
        i_1 += 1
    file_name_1 = '1.txt'
    with open(file_name_1, 'r', encoding= 'utf-8')as f_1:
        data_1 = f_1.readlines()

with open('2.txt', encoding= 'utf-8')as f_2:
    for line in f_2:
        i_2 += 1
    file_name_2 = '2.txt'
    with open(file_name_2, 'r', encoding= 'utf-8')as f_2:
        data_2 = f_2.readlines()

with open('3.txt', encoding= 'utf-8')as f_3:
    for line in f_3:
        i_3 += 1
    file_name_3 = '3.txt'
    with open(file_name_3, 'r', encoding= 'utf-8')as f_3:
        data_3 = f_3.readlines()

dict_1 = {'name': file_name_1,'quantity': i_1 , 'data': data_1, }
dict_2 = {'name': file_name_2,'quantity': i_2 , 'data': data_2, }
dict_3 = {'name': file_name_3,'quantity': i_3 , 'data': data_3, }

dict_list = [dict_1, dict_2, dict_3]
sorted_dict_list = sorted(dict_list, key=lambda x: x['quantity'])

print(sorted_dict_list