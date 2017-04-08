
import os

def read_file(file_path):
    fp = open(file_path)

    content = fp.read()

    fp.close()

    fcontent = content.split("\n")

    return fcontent

def write_file(fcontent, file_path):
    fp = open(file_path, 'w')

    content = '\n'.join(fcontent)

    fp.write(content)

    fp.close()

def insert_line(line_num, line_str, file_path):
    content = read_file(file_path)

    content.insert(line_num, line_str, file_path)

    write_file(content, file_path)

def set_line(line_num, line_str, file_path):
    content = read_file(file_path)

    content[line_num-1] = line_str

    write_file(content, file_path)

def append_line(line_str, file_path):
    content = read_file(file_path)

    content.append(line_str)

    write_file(content, file_path)

def replace(old, new, file_path):
    content = read_file(file_path)
    rcontent = []
    
    for line in content:
        rline = line.replace(old, new)
        rcontent.append(rline)

    write_file(rcontent, file_path)

if __name__ == "__main__":
    file_path = "../test/test.txt"

    append_line("Hello", file_path)

