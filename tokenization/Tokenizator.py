from setting.stop_words_setting import STOP_WORDS, DOCUMENT_WORDS


def tokenize(content):
    WORDS = set(DOCUMENT_WORDS.lower().split(" "))
    return WORDS - STOP_WORDS