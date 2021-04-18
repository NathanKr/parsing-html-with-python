from utils import get_html_page
from lxml.html import fromstring

url = 'http://example.com/'
html = get_html_page(url)
print(f'type(html) : {type(html)}') # class requests.models.Response
doc = fromstring(html.content) 
print(f'type(html.content) : {type(html.content)}') # class bytes 
print(f'type(doc) : {type(doc)}') # class lxml.html.HtmlElement
title_elements = doc.cssselect('title')
print(f'type(title_elements) : {type(title_elements)}') # class list
title_element = title_elements[0]
print(f'type(title_element) : {type(title_element)}') # class lxml.html.HtmlElement
print(title_element.text_content()) # Example Domain


