import redis


class Cache:
    redisCache = redis.Redis(host="39.106.113.6", port=6380, password="Xwcxwj6688")


if __name__ == "__main__":
    print(Cache.redisCache)