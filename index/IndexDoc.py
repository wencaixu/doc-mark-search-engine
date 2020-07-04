# 建立文档单词反向索引，放入到Redis中
import threading

from setting.stop_words_setting import DOCUMENT_WORDS
import redis

from tokenization.Tokenizator import tokenize

r = redis.Redis(host="39.106.113.6", port=6380, password="Xwcxwj6688")


# 建立并添加反向索引到Redis缓存
def create_reverse_index(connect, token, doc):
    # pipeline = r.pipeline(transaction=False)
    connect.sadd("idx:" + token, doc)


def index_document(connect, doc, content):
    words = tokenize(content)
    for token in words:
        threading.Thread(target=create_reverse_index, args=(connect, token, doc)).start()


index_document(r, doc="doc1", content=DOCUMENT_WORDS)
