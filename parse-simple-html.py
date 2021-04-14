from lxml import etree
import os
from io import StringIO

# consume html string from lxml
html_doc = "<html><head><title>test</head><body><h1>טקסט בעברית</h3></html>"
to_string_encoding = 'unicode' #using utf-8 was not good here
parser = etree.HTMLParser()
htmlTree   = etree.parse(StringIO(html_doc), parser)
print(f'type(htmlTree) : {type(htmlTree)}')
strHtmlTree = etree.tostring(htmlTree.getroot(), encoding=to_string_encoding)
print(f'type(strHtmlTree) : {type(strHtmlTree)}')
print(strHtmlTree)

# write html string to html file
file_name = 'doc.html'
file_path = os.path.join('.','result',file_name)

file_write_encoding = 'utf-8' #using unicode was not good here
with open(file_path, 'w' , encoding=file_write_encoding) as file: 
    print(file.write(strHtmlTree)) 


