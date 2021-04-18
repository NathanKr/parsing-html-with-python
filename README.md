<h2>Motivation</h2>
Play with html in python


<table>
  <tr>
    <th>File</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>consume-simple-html.py</td>
    <td>
    <ul>
    <li>use lxml to consume and write html file</li>
    <li>lxml.html is not used thus parsing of html structure is not done. This e.g. missing closing tag will not cause any error</li>
    </ul>
    </td>
  </tr>
  
</table>


<h2>Points of interest</h2>
<ul>
<li>parsing the html was used with lxml - no specific html code needed</li>
<li>encoding in parse-simple-html.py was strange - i had to use unicode for the etree.tostring and utf-8 for open</li>
</ul>

