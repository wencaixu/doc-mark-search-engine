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
    def __get_prefix(word, un_want):
        prefix = word[:1]
        if prefix in "+-":
            # 获取+-号之后的数字
            w = word[1:]
        else:
            w = word
        if prefix == '-':
            un_want.append(w)
        print(w)

    def parser(self, query_string):
        if query_string is None or query_string == "" or len(str(query_string).strip()) == 0:
            return [], set()
        words = QUERY_RE.findall(str(query_string).lower())
        un_want = []
        all_words = ()
        for word in words:
            if len(word) < 2 or word in STOP_WORDS:
                continue
            self.__get_prefix(word, un_want)
        return un_want, all_words


if __name__ == "__main__":
    GrammarParser().parser("+word-hello")
    pass
