import fitz

reader = fitz.open('myresume.pdf')
for page in reader:
    text=page.get_text()
    
print(text)