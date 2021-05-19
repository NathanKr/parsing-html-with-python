from lxml.html import fromstring
import lxml.html as html

def is_empty(text):
    return len(text) == 0

def delete_empty_table_rows(html_doc : str)->str:            
    doc = fromstring(html_doc)
    elements = doc.cssselect('table > tr')
    empty_tr_elements = []
    for tr_elem in elements:
        is_row_all_empty = True
        for td_elem in tr_elem:
            if not is_empty(td_elem.text_content()):
                is_row_all_empty = False
                break
        
        if is_row_all_empty:
            empty_tr_elements.append(tr_elem)

    for empty_tr_element in empty_tr_elements:
        empty_tr_element.drop_tree()

    return html.tostring(doc)

html_doc = "<html><body><table>\
            <tr><td>1</td><td></td></tr>\
            <tr><td></td><td></td></tr>\
            <tr><td>1</td><td>2</td></tr>\
            </table></body></html>"
            
new_html = delete_empty_table_rows(html_doc)
print(new_html)








