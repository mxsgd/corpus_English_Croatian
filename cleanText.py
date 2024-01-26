import re

def cluster_text_by_punctuation(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    cleaned_text = re.sub(r'[^.!?a-zčćžđšžA-ZČĆŠŽ]', ' ', text)
    cleaned_text = re.sub(r'\.\.+', ' ', cleaned_text)
    cleaned_text = re.sub(r'\s\s+', ' ', cleaned_text)
    cleaned_text = re.sub(r'\.\s(\.\s)+', ' ', cleaned_text)
    cleaned_text = re.sub(r'\s\.', '.', cleaned_text)
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(cleaned_text)

for i in range(0,14):
    input_file_path = f'Manuals/txt/{i}_C.txt'
    output_file_path = f'Manuals/txt/{i}_C.txt'

    cluster_text_by_punctuation(input_file_path, output_file_path)

for i in range(0,14):
    input_file_path = f'Manuals/txt/{i}_E.txt'
    output_file_path = f'Manuals/txt/{i}_E.txt'

    cluster_text_by_punctuation(input_file_path, output_file_path)