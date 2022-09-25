import fitz

with fitz.open("data/students.pdf") as pdf:
    text = ''

    for page in pdf:
        text += page.get_text()

print(text)
