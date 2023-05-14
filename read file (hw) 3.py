with open("1.txt", "r", encoding='utf8') as f:
    count_1 = 0
    for line in f:
        count_1 += 1
    f_1 = open ("1.txt", "r", encoding='utf8')
    print(count_1)

with open("2.txt", "r", encoding='utf8') as f:
    count_2 = 0
    for line in f:
        count_2 += 1
    f_2 = open ("2.txt", "r", encoding='utf8')
    print(count_2)
  
with open("3.txt", "r", encoding='utf8') as f:
    count_3 = 0
    for line in f:
        count_3 += 1
    f_3 = open ("3.txt", "r", encoding='utf8')
    print(count_3)
  
file_length = [count_1, count_2, count_3]
file_name = ["1.txt", "2.txt", "3.txt"]
file_content = [f_1, f_2, f_3]
zipped_list = list(zip(file_length, file_name, file_content))
zipped_list_sort = zipped_list.sort()

print(zipped_list)
with open('4.txt', 'w', encoding='utf-8') as file:
    for i in zipped_list:
        file.write(str(i[0]))
        file.write("\n")
        file.write(str(i[1]))
        file.write("\n")
        file.writelines(i[2].read())
        file.write("\n")
        