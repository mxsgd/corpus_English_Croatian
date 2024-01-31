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
    english = re.sub(r'⁇', '', english)
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
        smaller = len(english_out)
    try:

        while (len(croatian_out) - len(english_out) != 0):

            ctrl = 0
            for j in range(smaller-1):
                ctrlNum = j - ctrl
                print(f"length of {i}_Carr {ctrlNum} element: {len(croatian_out[j])}")
                print(f"length of {i}_Earr {ctrlNum} element: {len(english_out[j])}")
                if (abs(len(croatian_out[ctrlNum]) - len(english_out[ctrlNum])) > 100):
                    if (abs(len(croatian_out[ctrlNum]) - len(english_out[ctrlNum+1])) < abs(len(english_out[ctrlNum]) - len(croatian_out[ctrlNum+1]))):
                        english_out.pop(ctrlNum)
                        ctrl += 1
                    else:
                        croatian_out.pop(ctrlNum)
                        ctrl +=1

                # print(j - ctrl)
                # print(j - ctrl)
                # ctrlNum = j - ctrl
                # croatian_res = croatian_out[ctrlNum].split()
                # english_res = english_out[ctrlNum].split()
                # print(str(croatian_res[0]))
                # print(english_res[0])
                #
                # diff = len(croatian_out) - len(english_out)
                #
                # if (diff == 0):
                #     diff_counter += 1
                #
                # elif (diff != 0):
                #     diff_counter = 0
                #
                # if (diff_counter < 4):
                #     croatian_trans = translate_croatian_to_english(str(croatian_out[ctrlNum]))
                #     print(croatian_trans)
                #     croatian_trans_split = croatian_trans.split()
                #     print(croatian_trans_split[0])
                #
                # if (len(english_res) > 1):
                #     if (croatian_trans_split[0] != english_res[1] and croatian_trans != english_res[0] + ' ' + english_res[1]):
                #         secondCompare = True
                #     else:
                #         secondCompare = False
                # else:
                #     secondCompare = True
                #
                # print(secondCompare)
                #
                # if (diff_counter < 4 and croatian_trans_split[0] != english_res[0] and secondCompare):
                #     if(diff <= 0):
                #         english_out.pop(ctrlNum)
                #         ctrl += 1
                #         print(f"{i}_Carr has {len(croatian_out)} sentences")
                #         print(f"{i}_Earr has {len(english_out)} sentences")
                #     elif(diff > 0 ):
                #         croatian_out.pop(ctrlNum)
                #         ctrl += 1
                #         print(f"{i}_Carr has {len(croatian_out)} sentences")
                #         print(f"{i}_Earr has {len(english_out)} sentences")
                # print(len(english_out))
                # if(len(english_res) < 2):
                #     english_out.pop(ctrlNum)
                #     ctrl += 1
                #     print(f"FINAL {i}_Earr has {len(english_out)} sentences")
                # if (len(croatian_res) < 2):
                #     croatian_out.pop(ctrlNum)
                #     ctrl += 1
                #     print(f"FINAL {i}_Carr has {len(croatian_out)} sentences")
    except Exception as e:
        print(f"error: {e}")
        print(sys.exc_info())
    with open(croatian_file_path, 'w', encoding='utf-8') as file:
        file.write(str(croatian_out))
    with open(english_file_path, 'w', encoding='utf-8') as file:
        file.write(str(english_out))




for i in range(5,6):
    croatian_file_path = f'Manuals/txt/{i}_CArr'
    english_file_path = f'Manuals/txt/{i}_EArr'

    cluster_text_by_punctuation(croatian_file_path, english_file_path, i)
