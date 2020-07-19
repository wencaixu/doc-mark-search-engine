import re

from setting.StopWordsSetting import STOP_WORDS

QUERY_RE = re.compile("[+-]?[a-z']{2,}")


class GrammarParser:
    """
      搜索关键语法处理:
       当单词前用-号修饰时，排除该单词
       当单词前用+号修饰时，意为同义词
    """

    @staticmethod
    def __get_prefix(word, all_words):
        prefix = word[:1]
        if prefix in "+-":
            # 获取+-号之后的数字
            w = word[1:]
        else:
            w = word
        if prefix == '-':
            all_words.add(w)
        return all_words

    @staticmethod
    def is_empty(query_string):
        return query_string is None \
               or query_string == "" \
               or len(str(query_string).strip()) == 0

    def parser(self, query_string):
        if self.is_empty(query_string):
            return [], set()
        words = QUERY_RE.findall(str(query_string).lower())
        all_words = set()
        for word in words:
            if len(word) < 2 or word in STOP_WORDS:
                continue
            self.__get_prefix(word, all_words)
        return all_words


