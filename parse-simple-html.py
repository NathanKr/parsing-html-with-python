from lxml import etree
from io import StringIO

html_doc = "<html><head><title>test</head><body><h1>page title</h3></html>"
parser = etree.HTMLParser()
htmlTree   = etree.parse(StringIO(html_doc), parser)
print(f'type(htmlTree) : {type(htmlTree)}')
strHtmlTree = etree.tostring(htmlTree.getroot(), encoding='unicode')
print(f'type(strHtmlTree) : {type(strHtmlTree)}')
print(strHtmlTree)
file_path = 'doc.html'
with open(file_path, 'w') as file: 
    print(file.write(strHtmlTree)) 


