import codecs
from qwe import put
f=codecs.open("html.html", 'r')
a=f.read()
search_text ='</body>'
replace_text = f'<div>\
            <embed src=\"{put()}\"width=\"100%" height=\"100%\"/>\
        </div></body> '
with open(r'html.html', 'r') as file:
    data = file.read()
    data = data.replace(search_text, replace_text)
with open(r'newhtml.html', 'w') as file:
    file.write(data)
