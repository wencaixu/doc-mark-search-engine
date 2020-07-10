import threading

from cache.RedisCache import Cache

from tokenization.Tokenizator import tokenize

r = Cache().get_redis_cache(0)


def create_reverse_index(r, token, doc):
    """
    建立反向索引并添加到缓存中
    :param r: Redis链接
    :param token: 分割的单词
    :param doc:  文档名称
    :return:
    TODO 修改为pipeline
    """
    r.sadd("idx:" + token, doc)


def index_document(r, doc, content):
    """
    多线程建立文档索引
    :param r:
    :param doc:
    :param content:
    :return:
    TODO 线程个数控制修改
    """
    words = tokenize(content)
    for token in words:
        threading.Thread(target=create_reverse_index, args=(r, token, doc)).start()
