from setting.StopWordsSetting import STOP_WORDS, DOCUMENT_WORDS


def tokenize():
    words = set(DOCUMENT_WORDS.lower().split(" "))
    return words - STOP_WORDS
