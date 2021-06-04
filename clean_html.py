from lxml.html.clean import Cleaner
import lxml

def sanitize_html(unsecure_html_content : bytes)->str:
    cleaner = Cleaner(inline_style=True, scripts=True, javascript=True,safe_attrs_only=True,safe_attrs=[])
    try:
        secure_html_content = lxml.html.tostring(cleaner.clean_html(lxml.html.fromstring(unsecure_html_content)), method="html")
    except Exception as e:
        print(e)
        secure_html_content = b''
    
    return secure_html_content.decode()

html_doc = "<html><body><table id='id1'>\
            <tr 'style=color:blue;'><td>1</td><td></td></tr>\
            <tr><td></td><td></td></tr>\
            <tr><td>1</td><td>2</td></tr>\
            </table></body></html>"


bytes = html_doc.encode('utf-8')
clean_html_doc = sanitize_html(bytes)

print(f'html_doc\n{html_doc}')
print(f'clean_html_doc\n{clean_html_doc}') # all attributes are removed
assert(clean_html_doc != html_doc)