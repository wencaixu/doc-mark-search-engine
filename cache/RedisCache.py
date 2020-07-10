import redis

from setting.ApplicationContext import REDIS_HOST, MASTER_NODE_PORT, REDIS_PASSWORD


def singleton(cls):
    """
    单例装饰器
    :param cls:
    :return:
    """
    _instance = {}

    def inner(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return inner


@singleton
class Cache:
    """  单例缓存
        建立Redis缓存链接池,不同的服务放置到不同的数据库下,共16个，

   """
    __redisCache = redis.Redis(host=REDIS_HOST, port=MASTER_NODE_PORT, password=REDIS_PASSWORD)

    @classmethod
    def get_redis_cache(cls, dbx):
        if dbx == 0:
            return cls.__redisCache
        return cls.redis.Redis(host=REDIS_HOST, port=MASTER_NODE_PORT, password=REDIS_PASSWORD, db=dbx)

