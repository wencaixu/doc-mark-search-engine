from cache.RedisCache import Cache
from parsing.GrammarParser import GrammarParser

r = Cache().get_redis_cache(0)
if __name__ == "__main__":
    content = input("请输入你要查询的关键字")
    grammar: GrammarParser = GrammarParser()
    all_words = grammar.parser(content)
    for token in all_words:
        r.get("idx:" + token)


