"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import List, Union, Iterator


def merge_sorted_files(file_list: List[Union[Path, str], ]) -> Iterator:
    file_handles = [open(file, 'r') if isinstance(file, str) else file.open('r') for file in file_list]
    lines = [file.readline().strip() for file in file_handles]

    while any(lines):
        min_value = min(int(line) for line in lines if line)
        yield min_value

        for i, line in enumerate(lines):
            if line and int(line) == min_value:
                lines[i] = file_handles[i].readline().strip()

    for file_handle in file_handles:
        file_handle.close()
if __name__ == '__main__':
    file_list = ["file1.txt", "file2.txt"]
    result = list(merge_sorted_files(file_list))
    print(result)
