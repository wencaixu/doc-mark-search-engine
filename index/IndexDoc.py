# 建立文档单词反向索引，放入到Redis中
import threading

from setting.stop_words_setting import DOCUMENT_WORDS
import redis

from tokenization.Tokenizator import tokenize

# 此处填写个人redis服务信息
r = redis.Redis(host="aaa", port=6380, password="aaa")


# 建立并添加反向索引到Redis缓存
def create_reverse_index(connect, token, doc):
    # pipeline = r.pipeline(transaction=False)
    connect.sadd("idx:" + token, doc)


def index_document(connect, doc, content):
    words = tokenize(content)
    for token in words:
        threading.Thread(target=create_reverse_index, args=(connect, token, doc)).start()

