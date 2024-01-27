import re
import ast
import sys
from translate import Translator

def translate_croatian_to_english(word):
    translator = Translator(to_lang="en", from_lang="hr")
    translation = translator.translate(word)
    return translation



def cluster_text_by_punctuation(croatian_file_path, english_file_path, i):
    with open(croatian_file_path, 'r', encoding='utf-8') as file:
        croatian = file.read()
    with open(english_file_path, 'r', encoding='utf-8') as file:
        english = file.read()

    croatian_out = ast.literal_eval(croatian)
    english_out = ast.literal_eval(english)

    print(f"{i}_Carr has {len(croatian_out)} sentences")
    print(f"{i}_Earr has {len(english_out)} sentences")

    diff = len(croatian_out) - len(english_out)

    if(diff < 0):
        smaller = len(croatian_out)
    elif(diff > 0):
        smaller = len(english_out)
    else:
        smaller = 0
    try:
        ctrl_cr = 0
        ctrl_en = 0
        diff_counter = 0
        for j in range(smaller):

            croatian_res = croatian_out[j-ctrl_cr].split()
            english_res = english_out[j-ctrl_en].split()
            print(str(croatian_res[0]))
            croatian_trans = translate_croatian_to_english(str(croatian_res[0]))
            print(croatian_trans)
            croatian_trans_split = croatian_trans.split()
            print(croatian_trans_split[0])
            print(english_res[0])

            diff = len(croatian_out) - len(english_out)
            if (diff == 0):
                diff_counter += 1
            elif (diff != 0):
                diff_counter = 0
            if (diff_counter != 2 and croatian_trans_split[0] != english_res[0] and croatian_trans != english_res[1] and croatian_trans != english_res[0] + ' ' + english_res[1]):
                if(diff < 0):
                    english_out.pop(j-ctrl_en)
                    ctrl_en += 1
                    print(f"{i}_Carr has {len(croatian_out)} sentences")
                    print(f"{i}_Earr has {len(english_out)} sentences")
                elif(diff > 0 ):
                    croatian_out.pop(j-ctrl_cr)
                    ctrl_cr += 1
                    print(f"{i}_Carr has {len(croatian_out)} sentences")
                    print(f"{i}_Earr has {len(english_out)} sentences")

        print(f"FINAL {i}_Carr has {len(croatian_out)} sentences")
        print(f"FINAL {i}_Earr has {len(english_out)} sentences")
    except Exception as e:
        print(f"error: {e}")
    with open(croatian_file_path, 'w', encoding='utf-8') as file:
        file.write(str(croatian_out))
    with open(english_file_path, 'w', encoding='utf-8') as file:
        file.write(str(english_out))



for i in range(0,14):
    croatian_file_path = f'Manuals/txt/{i}_CArr'
    english_file_path = f'Manuals/txt/{i}_EArr'

    cluster_text_by_punctuation(croatian_file_path, english_file_path, i)
