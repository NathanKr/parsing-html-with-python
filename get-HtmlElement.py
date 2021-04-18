from lxml.html import fromstring
from utils import get_html_page


url = 'http://example.com/'
html_text = get_html_page(url).text
# print(html_text)
docHtmlElement = fromstring(html_text) # lxml.html.HtmlElement
print(f'type(docHtmlElement) : {type(docHtmlElement)}')



