from setting.stop_words_setting import STOP_WORDS, DOCUMENT_WORDS


def tokenize(content):
    words = set(DOCUMENT_WORDS.lower().split(" "))
    return words - STOP_WORDS
