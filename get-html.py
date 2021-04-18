from utils import get_html_page

url = 'http://example.com/'
html_text = get_html_page(url).text
print(html_text)

