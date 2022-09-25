import os

import pandas as pd
from fpdf import FPDF

OUTPUT_DIR = 'pdfs'


def check_dir():
    if (not os.path.exists(OUTPUT_DIR)):
        os.mkdir(OUTPUT_DIR)


df = pd.read_excel('data/data.xlsx')

for index, row in df.iterrows():
    pdf = FPDF(orientation='P', unit='pt', format='A4')
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=24)
    pdf.cell(w=0, h=50, txt=row['name'], align='C', ln=1)

    for column in df.columns[1:]:
        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt=f"{column.title()}:")

        pdf.set_font(family='Times', style='I', size=14)
        pdf.cell(w=0, h=25, txt=row[column], ln=1)

    check_dir()
    pdf.output(f'pdfs/{row["name"]}.pdf')
