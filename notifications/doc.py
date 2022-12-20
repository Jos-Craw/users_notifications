from docx import Document
from docxcompose.composer import Composer

files = ["1268.docx", "1700.docx"]
composed = "composed.docx"

result = Document(files[0])
result.add_page_break()
composer = Composer(result)

for i in range(1, len(files)):
    doc = Document(files[i])

    if i != len(files) - 1:
        doc.add_page_break()

    composer.append(doc)

composer.save(composed)