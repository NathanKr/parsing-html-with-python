from lxml import etree

# head start tag is missing
bad_html_doc = "<html><title>test</head><body><h1>טקסט בעברית</h3></html>"
to_string_encoding = 'unicode' #using utf-8 is good here

html = etree.HTML(bad_html_doc) # head problem is fixed
print(f'type(html) : {type(html)}')
result = etree.tostring(html, pretty_print=True, method="html", encoding=to_string_encoding)
print(f'type(result) : {type(result)}')
# print(result)


