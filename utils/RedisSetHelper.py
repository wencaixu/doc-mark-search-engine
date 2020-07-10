import uuid

from cache.RedisCache import Cache

r = Cache().get_redis_cache(0)


class RedisHelper:
    """
        Redis操作控制器
    """
    @staticmethod
    def set_common(r, method, names, ttl=30):
        """
        公共调用函数
        :param r: Redis连接
        :param method: Redis命令方法
        :param names: 文档中的关键字
        :param ttl: 缓存清空时间
        :return:
        """
        uid = str(uuid.uuid4())
        ids = ['idx:' + name for name in names]
        for idx in ids:
            getattr(r, method)(uid, idx)
            # 设置过期时间
            r.expire(uid, ttl)
        return uid

    def union(self, r, items, ttl):
        """
        计算集合并集
        :param r: Redis连接
        :param items: 查询的关键字组
        :param ttl: 缓存清除时间
        :return:
        """
        return self.set_common(r, "sunionstore", items, ttl)

    def diff(self, r, items, ttl):
        """
        计算集合交集
        :param r: Redis连接
        :param items: 查询的关键字组
        :param ttl: 缓存清除时间
        :return:
       """
        return self.set_common(r, "sinterstore", items, ttl)

    def intersect(self, r, items, ttl):
        """
        计算集合差集
        :param r: Redis连接
        :param items: 查询的关键字组
        :param ttl: 缓存清除时间
        :return:
        """
        return self.set_common(r, "sdiffstore", items, ttl)


if __name__ == "__main__":
    print(r.keys("*"))
    uid1 = RedisHelper().diff(r, ["documents"], 30)
    print(r.smembers(uid1))
    pass
