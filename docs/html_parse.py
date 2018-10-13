html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">Hello there mom there is a new way of looking at a file now</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')


print("this is a title:", soup.title)
print("this is the name of what we are calling tags", soup.title.name)
print("this is a title's name:", soup.title.string)
print("this is a title's parent's name:", soup.title.parent.name)
print("this is getting the p tag:", soup.p)
print("this is getting the p class name:", soup.p['class'])
print("this is getting all links",soup.find_all('a'))
#this is getting all the links readable on the page
for link in soup.find_all('a'):
    print(link.get('href'))
#this is getting html_doc

print(soup.prettify())
#this is getting all the texts on the page
print(soup.get_text())


doc = '''Bob reports <a href="http://www.bob.com/">success</a>
with his plasma breeding <a
href="http://www.bob.com/plasma">experiments</a>. <i>Don't get any on
us, Bob!</i>

<br><br>Ever hear of annular fusion? The folks at <a
href="http://www.boogabooga.net/">BoogaBooga</a> sure seem obsessed
with it. Secret project, or <b>WEB MADNESS?</b> You decide!'''

print(doc)
#simple call for the var in id