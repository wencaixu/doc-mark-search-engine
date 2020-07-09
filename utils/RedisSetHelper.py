import uuid

import redis


class RedisHelper:
    @staticmethod
    def set_common(connect, method, names, ttl=30):
        uid = str(uuid.uuid4())
        ids = ['idx:' + name for name in names]
        for idx in ids:
            getattr(connect, method)(uid, idx)
            # 设置过期时间
            connect.expire(uid, ttl)
        return uid

    def union(self, connect, items, ttl, execute=True):
        return self.set_common(connect, "sunionstore", items, ttl, execute)

    def diff(self, connect, items, ttl, execute=True):
        return self.set_common(connect, "sinterstore", items, ttl, execute)

    def intersect(self, connect, items, ttl, execute=True):
        return self.set_common(connect, "sdiffstore", items, ttl, execute)


if __name__ == "__main__":
    r = redis.Redis(host="", port=6379, password="aaa")
    print(Help.set_common(r, 2, ["file", "name"], 4))
