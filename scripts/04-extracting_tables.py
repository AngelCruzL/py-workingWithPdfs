import os

import tabula

OUTPUT_DIR = 'output'


def check_dir():
    if (not os.path.exists(OUTPUT_DIR)):
        os.mkdir(OUTPUT_DIR)


table = tabula.read_pdf("data/weather.pdf", pages=1)
check_dir()
table[0].to_csv("output/weather.csv", index=None)
