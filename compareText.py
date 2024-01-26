import re
import ast

def cluster_text_by_punctuation(croatian_file_path, english_file_path, i):
    with open(croatian_file_path, 'r', encoding='utf-8') as file:
        croatian = file.read()
    with open(english_file_path, 'r', encoding='utf-8') as file:
        english = file.read()

    croatian_out = ast.literal_eval(croatian)
    english_out = ast.literal_eval(english)
    print(f"{i}_Carr has {len(croatian_out)} sentences")
    print(f"{i}_Earr has {len(english_out)} sentences")
    for j in range(len(croatian_out)):
        print(f"{j} sentence diff: {len(croatian_out[j].split())-len(english_out[j].split())}")

for i in range(0,14):
    croatian_file_path = f'Manuals/txt/{i}_CArr'
    english_file_path = f'Manuals/txt/{i}_EArr'

    cluster_text_by_punctuation(croatian_file_path, english_file_path, i)
