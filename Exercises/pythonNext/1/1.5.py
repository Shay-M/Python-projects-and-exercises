# --1.5.1---------------------------------------------------
print('-- 1.5.1')

file_object = open("names.txt", 'r')
print(max([name for name in file_object], key=len))  # Valdimir

# --1.5.2---------------------------------------------------
print('-- 1.5.2')

file_object = open("names.txt", 'r')
names_list = file_object.read().splitlines()
print(sum([len(name) for name in names_list]))  # 38

# --1.5.3---------------------------------------------------
print('-- 1.5.3')
file_object = open("names.txt", 'r')
names_list = file_object.read().splitlines()
names_list.sort(key=len)

print('\n'.join([name for name in names_list if len(name) == len(names_list[0])]))

# --1.5.4---------------------------------------------------
print('-- 1.5.4')

file_object = open("names.txt", 'r')
names_list = file_object.read().splitlines()
print([len(name) for name in names_list])
