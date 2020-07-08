from urllib.request import urlopen

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO

import sys
import importlib

importlib.reload(sys)


class TextReader:
    def read(self):
        with open(self, 'r') as foe:
            print(foe.read(1))


