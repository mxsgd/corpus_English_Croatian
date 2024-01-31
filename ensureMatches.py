from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
from googletrans import Translator

def find_best_matches(sentences_cr, sentences_en, nlp2):
    cr_matches = []
    en_matches = []
    translator = Translator()

    min_len = min(len(sentences_cr), len(sentences_en))
    best_match_index = []
    cr_index = []
    ctrl = 0

    for i in range(min_len):
        matched = 0
        similarities = []
        try:
            cr = nlp2(translator.translate(sentences_cr[i], dest='en').text).vector.reshape(1, -1)
            ctrlNum = i - ctrl
            step = 0
            top_range = i+ctrlNum+1

            if(top_range > min_len):
                top_range = len(sentences_en)

            for j in range(ctrlNum,top_range):
                en = nlp2(sentences_en[j]).vector.reshape(1, -1)
                similarities.append(cosine_similarity(cr, en)[0, 0])
                if (similarities[step]>0.95):
                    print(f"got match in {i} sentence")
                    best_match_index.append(j)
                    cr_index.append(i)
                    matched = 1
                    break
                step+= 1

            if (matched == 0):
                ctrl += 1
        except Exception as e:
            print(e)
    return best_match_index, cr_index


def cluster_sentences_hr_en(input_file_path_cr, input_file_path_en):
    with open(input_file_path_cr, 'r', encoding='utf-8') as file:
        cr_text = file.read()
    with open(input_file_path_en, 'r', encoding='utf-8') as file:
        en_text = file.read()

    nlp_cr = spacy.load('hr_core_news_lg')
    nlp_cr.add_pipe('sentencizer')
    doc_cr = nlp_cr(cr_text)

    nlp_en = spacy.load("en_core_web_lg")
    nlp_en.add_pipe('sentencizer')
    doc_en = nlp_en(en_text)

    sentences_cr = [sent.text for sent in doc_cr.sents]
    sentences_en = [sent.text for sent in doc_en.sents]

    best_match_index, cr_index = find_best_matches(sentences_cr, sentences_en, nlp_en)
    min_len = min(len(doc_cr), len(doc_en))
    cr_matches = []
    en_matches = []
    for index in cr_index:
        cr_matches.append(sentences_cr[index])
    for index in best_match_index:
        en_matches.append(sentences_en[index])



    return cr_matches, en_matches
# Example usage
for i in range(5, 6):
    cr_file_path = f'Manuals/txt/{i}_C.txt'
    en_file_path = f'Manuals/txt/{i}_E.txt'
    cr_matches, en_matches = cluster_sentences_hr_en(cr_file_path, en_file_path)
    with open(f'Manuals/txt/{i}_cMatches', 'w', encoding='utf-8') as file:
        file.write(str(cr_matches))
    with open(f'Manuals/txt/{i}_eMatches', 'w', encoding='utf-8') as file:
        file.write(str(en_matches))
