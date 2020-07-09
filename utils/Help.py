import uuid

import redis


class Help:
    @staticmethod
    def set_common(c, method, names, ttl=30, execute=True):
        uid = str(uuid.uuid4())
        ids = ['idx:' + name for name in names]
        for idx in ids:
            getattr(c, method)(uid, idx)
            # 设置过期时间
            c.expire(uid, ttl)
        return uid

    @staticmethod
    def union(c, method, items, ttl, execute=True):
        pass


if __name__ == "__main__":
    r = redis.Redis(host="", port=6379, password="aaa")
    print(Help.set_common(r, 2, ["file", "name"], 4, False))
