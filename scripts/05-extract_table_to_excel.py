import os

import tabula

OUTPUT_DIR = 'output'


def check_dir():
    if (not os.path.exists(OUTPUT_DIR)):
        os.mkdir(OUTPUT_DIR)


table = tabula.read_pdf('data/table-and-text.pdf', pages=1)
table[0].to_excel('output/table-and-text.xlsx', index=None)
