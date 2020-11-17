import sys
import importlib

importlib.reload(sys)


class TextReader:

    """
      Txt等类型文本读取
    """

    def __init__(self, filename, split):
        # 文件名称
        self.filename = filename
        # 分隔符
        self.split = split
        # 不同的单词集合,创建一个空集合必须使用set()
        # 类内变量
        # self.distinct = set()

    def read(self):
        distinct = set()
        with open(self.filename, 'r') as read_to:
            lines = read_to.readline()
            if lines:
                # 此处使用set(list)将列表转成集合
                split_set = set(lines.split(self.split))
                for s in split_set:
                    distinct.add(s)
        read_to.close()
        return distinct


if __name__ == "__main__":
    text = TextReader("test.txt", " ")
    distinct_set = text.read()
    for s in distinct_set:
        print(s)
