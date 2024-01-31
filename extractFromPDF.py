import pdfplumber

def read_croatian_pdfs():
    text = []
    sum = 0
    for i in range(1, 15):
        n = str(i)

        try:
            with pdfplumber.open(f'Manuals/{i}_C.pdf') as pdf:
                text = ''
                for page_num in range(len(pdf.pages)):
                    page = pdf.pages[page_num]
                    text += page.extract_text()
        except:
            print(f"couldn't find a {i}_C.pdf file")

        with open(f"Manuals/txt/{i}_C.txt", 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)

def read_english_pdfs():
    text = []
    sum = 0
    for i in range(10, 11):
        n = str(i)

        try:
            with pdfplumber.open(f'Manuals/{i}_E.pdf') as pdf:
                text = ''
                for page_num in range(len(pdf.pages)):
                    page = pdf.pages[page_num]
                    text += page.extract_text()
        except:
            print(f"couldn't find a {i}_E.pdf file")

        with open(f"Manuals/txt/{i}_E.txt", 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)


read_croatian_pdfs()
read_english_pdfs()