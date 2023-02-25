import os, fnmatch

def get_list_of_files(folder_name, type_file):
    list_of_files = os.listdir(folder_name)
    pattern = type_file
    result = []
    for entry in list_of_files:  
        if fnmatch.fnmatch(entry, pattern):
                result.append(entry)
    return result
            
def get_full_path(folder_name, fales_name):
    root_path = os.getcwd()
    full_path = os.path.join(root_path, folder_name, fales_name)
    return full_path

def get_read_file(full_path):
    with open(full_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def sort_file(unsorted_file):
    sorted_file = dict(sorted(unsorted_file.items(), key=lambda item: item[1]))
    return sorted_file

def create_file_result(sorted_file):
    with open('result.txt', 'w', encoding='utf-8') as file:
        for name_file, lines in sorted_file.items():
            file.write(f'{name_file} \n')
            file.write(f'{lines[0]} \n')
            for line in lines[1]:
                file.write(f'{line} \n')
    
def get_sorted_file(folder_name, type_file):
    fales_list = get_list_of_files(folder_name, type_file)
    unsorted_file = {}
    for file in fales_list:
        full_path = get_full_path(folder_name, file)
        lines = get_read_file(full_path)
        unsorted_file[file] =[len(lines), lines]
    sorted_file = sort_file(unsorted_file)
    result = create_file_result(sorted_file)
    return result

get_sorted_file("sorted", "*.txt")