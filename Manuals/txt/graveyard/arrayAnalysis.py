import ast


def find_biggest_diff(croatian_file_path, english_file_path, i):
    with open(croatian_file_path, 'r', encoding='utf-8') as file:
        croatian = file.read()
    with open(english_file_path, 'r', encoding='utf-8') as file:
        english = file.read()
    croatian_out = ast.literal_eval(croatian)
    english_out = ast.literal_eval(english)
    diff = len(croatian_out) - len(english_out)
    print(f"{i}_Carr has {len(croatian_out)} sentences")
    print(f"{i}_Earr has {len(english_out)} sentences")
    if (diff < 0):
        smaller = len(croatian_out)
    elif (diff > 0):
        smaller = len(english_out)
    else:
        smaller = len(english_out)

    biggest_diff = 0
    last_diff = 0
    ctrl = 0
    for j in range(smaller):
        ctrlNum = j - ctrl
        print(f"length of {i}_Carr {ctrlNum} element: {len(croatian_out[ctrlNum])}")
        print(f"length of {i}_Earr {ctrlNum} element: {len(english_out[ctrlNum])}")
        # croatian_res = croatian_out[ctrlNum]
        # english_res = english_out[ctrlNum]
        # if (len(croatian_res.split()) < 2 or len(croatian_res.split()) > 50):
        #     croatian_out.pop(ctrlNum)
        #     ctrl += 1
        # if (len(english_res.split()) < 2 or len(english_res.split()) > 50):
        #     english_out.pop(ctrlNum)
        #     ctrl += 1
        if(abs(len(croatian_out[ctrlNum]) - len(english_out[ctrlNum])) > last_diff):
            biggest_diff = ctrlNum
            last_diff = abs(len(croatian_out[ctrlNum]) - len(english_out[ctrlNum]))
    print(f"biggest diff in {biggest_diff} element: {last_diff}")

def remove_biggest_diff(croatian_file_path, english_file_path, i):
    with open(croatian_file_path, 'r', encoding='utf-8') as file:
        croatian = file.read()
    with open(english_file_path, 'r', encoding='utf-8') as file:
        english = file.read()
    croatian_out = ast.literal_eval(croatian)
    english_out = ast.literal_eval(english)
    diff = len(croatian_out) - len(english_out)
    if (diff < 0):
        smaller = len(croatian_out)
    elif (diff > 0):
        smaller = len(english_out)
    else:
        smaller = len(english_out)
    # croatian_out.pop()
    croatian_out.pop(1241)
    print(f"{i}_Carr has {len(croatian_out)} sentences")
    print(f"{i}_Earr has {len(english_out)} sentences")
    ctrl = 0
    for j in range(smaller):
        ctrlNum = j - ctrl
        croatian_res = croatian_out[ctrlNum]
        english_res = english_out[ctrlNum]
        if (len(croatian_res.split()) < 2 or len(croatian_res.split()) > 50 or len(croatian_res) > 250):
            croatian_out.pop(ctrlNum)
            ctrl += 1
        if (len(english_res.split()) < 2 or len(english_res.split()) > 50 or len(english_res) > 250):
            english_out.pop(ctrlNum)
            ctrl += 1


    with open(croatian_file_path, 'w', encoding='utf-8') as file:
        file.write(str(croatian_out))
    with open(english_file_path, 'w', encoding='utf-8') as file:
        file.write(str(english_out))




for i in range(8,9):
    croatian_file_path = f'Manuals/txt/{i}_CArr'
    english_file_path = f'Manuals/txt/{i}_EArr'

    remove_biggest_diff(croatian_file_path, english_file_path, i)
    find_biggest_diff(croatian_file_path, english_file_path, i)
