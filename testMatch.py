from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
from googletrans import Translator


def find_best_matches(sentences_cr, sentences_en, nlp2):

    translator = Translator()

    min_len = min(len(sentences_cr), len(sentences_en))
    best_match_index = []


    similarities = []
    cr = nlp2(translator.translate(sentences_cr, dest='en').text).vector.reshape(1, -1)

    en = nlp2(sentences_en).vector.reshape(1, -1)
    similarities.append(cosine_similarity(cr, en)[0, 0])
    print(similarities)

    return similarities


nlp_en = spacy.load("en_core_web_lg")

text_en = 'GT I User Manual www.samsung.comInformation about this manual This device provides high quality mobile communication and entertainment ensured by Samsung s high standards and technological expertise.'
text_cr = 'GT I Korisnički priručnik www.samsung.comInformacije o ovom priručniku Ovaj uređaj osigurava visoku kvalitetu mobilnog komuniciranja i zabave osiguranu Samsungovim visokim standardima i tehnološkog stručnog znanja.'

find_best_matches(text_cr, text_en, nlp_en)