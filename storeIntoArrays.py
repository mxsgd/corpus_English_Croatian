import re

import re

def cluster_text_by_punctuation(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    array = re.findall(r'[^.]*\.', text)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(str(array))

for i in range(0,14):
    input_file_path = f'Manuals/txt/{i}_C.txt'
    output_file_path = f'Manuals/txt/{i}_CArr'

    cluster_text_by_punctuation(input_file_path, output_file_path)

for i in range(0,14):
    input_file_path = f'Manuals/txt/{i}_E.txt'
    output_file_path = f'Manuals/txt/{i}_EArr'

    cluster_text_by_punctuation(input_file_path, output_file_path)