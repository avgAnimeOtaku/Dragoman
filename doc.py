import aspose.words as aw

# create document object
doc = aw.Document()

# create a document builder object
builder = aw.DocumentBuilder(doc)

# add text to the document
builder.write("Hello \n world!")

# save document
doc.save("out.docx")