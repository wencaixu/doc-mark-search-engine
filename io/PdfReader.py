from urllib.request import urlopen

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO

import sys
import importlib

importlib.reload(sys)


class PDFReader:

    def __init__(self):
        print("构造函数")

    """
      PDF读取器
    """

    def read(self):

        resource = PDFResourceManager()
        string_io = StringIO()
        la = LAParams()
        device = TextConverter(resource, string_io, laparams=la)
        process_pdf(resource, device, self)
        device.close()

        content = string_io.getvalue()
        string_io.close()

        return content


if __name__ == "__main__":
    pdf = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
    print(PDFReader.read(pdf))
    pdf.close()
