import ast
from nltk.translate import AlignedSent, Alignment
import pickle

cr_sentences = []
en_sentences = []

for i in range(1, 8):
    cr_file_path = f'Manuals/txt/{i}_cMatches'
    en_file_path = f'Manuals/txt/{i}_eMatches'
    with open(cr_file_path, 'r', encoding='utf-8') as file:
        cr_text = file.read()
    with open(en_file_path, 'r', encoding='utf-8') as file:
        en_text = file.read()

    croatian_out = ast.literal_eval(cr_text)
    english_out = ast.literal_eval(en_text)

    for sent in croatian_out:
        cr_sentences.append(sent)
    for sent in english_out:
        en_sentences.append(sent)

aligned_sentences = []

for cr_sent, en_sent in zip(cr_sentences, en_sentences):
    alignments = [(i, i) for i in range(min(len(cr_sent), len(en_sent)))]

    aligned_sent = AlignedSent(en_sent, cr_sent, Alignment(alignments))

    aligned_sentences.append(aligned_sent)

corpus = aligned_sentences

with open("corpus.pkl", "wb") as pickle_file:
    pickle.dump(corpus, pickle_file)