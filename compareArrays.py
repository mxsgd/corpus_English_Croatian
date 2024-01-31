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




for i in range(1,14):
    croatian_file_path = f'Manuals/txt/{i}_cMatches'
    english_file_path = f'Manuals/txt/{i}_eMatches'
    cluster_text_by_punctuation(croatian_file_path, english_file_path, i)
