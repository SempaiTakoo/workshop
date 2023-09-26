import os
from pathlib import Path

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size


def humanized_size(num, suffix='B', si=False):
    if si:
        units = ['','K','M','G','T','P','E','Z']
        last_unit = 'Y'
        div = 1000.0
    else:
        units = ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']
        last_unit = 'Yi'
        div = 1024.0
    for unit in units:
        if abs(num) < div:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= div
    return "%.1f%s%s" % (num, last_unit, suffix)


def get_list_of_dir_sizes(start_path = '.'):
    dir_sizes = dict()
    for directory in os.listdir(start_path):
        dir_path = start_path + '\\' + directory 
        dir_size = get_size(dir_path)
        humanized_dir_size = humanized_size(dir_size)
        dir_sizes[directory] = dir_size
    return dir_sizes
    

def print_dir_sizes(start_path = '.'):
    dir_sizes = get_list_of_dir_sizes(start_path)
    for directory in reversed(sorted(dir_sizes, key=dir_sizes.get)):
        humanized_dir_size = humanized_size(dir_sizes[directory])
        print(f'{humanized_dir_size:<9} {directory}')

if __name__ == '__main__':
    PATH = 'C:\\'
    print_dir_sizes(PATH)