from bs4 import BeautifulSoup

f = open("hello.html")
html = f.read()
soup = BeautifulSoup(html, 'html.parser')

# This will help us make sense of the document structure
# print(soup.prettify())


# searching by tag
all_list_items = soup.find_all('li')
all_divs = soup.find_all('div')

# searching by class
all_goodbye_elements = soup.find_all(class_='goodbye')

# searching by tag AND class
all_french_list_items = soup.find_all('li', class_='french')

# searching by id
all_hello_elements = soup.find_all(id='hello-list')

print('list items:', all_list_items)
print('------')
print('divs:', all_divs)
print('------')
print('goodbye elements:', all_goodbye_elements)
print('------')
print('french stuff:', all_french_list_items)
print('------')
print('hello id elements:', all_hello_elements)
print('------')

print(type(all_list_items[0]))
print('------')
# Output <class 'bs4.element.Tag'>


print('All list items:')
for li in all_list_items:
  print(li.string)
print('------')


print('Children of hello-list:')
for child in all_hello_elements[0].children:
  print(child.string)
print('------')


print('List items within the hello tag')
hello_list_items = all_hello_elements[0].find_all('li')
print (hello_list_items)
print('------')

# ‘find( )’ always just returns the first matching element,
# so only use it when you know there’s only one (or you know you only want the first one).

print('The hello-list element')
the_hello_element = soup.find(id='hello-list')
print(the_hello_element)
print('------')

img_tag = soup.find('img')
print('The img source:')
print(img_tag['src'])
print('------')

############### Ex #####

#Print out the elements of the “goodbye” list (just the strings, no tags or other junk).
print('the elements of the “goodbye” list')
the_goodbye_element = soup.find(id='goodbye-list')
goodbye_list_items = the_goodbye_element.find_all('li')
for li in goodbye_list_items:
  print(li.string)
print('------')
#Print out the width of the img element.
img_tag = soup.find('img')
print('The width of the img:')
print(img_tag['width'])
print('------')
#Print out the URL that the `<a>` tag points to.
a_tag = soup.find('a')
print('The url of the tag <a>:')
print(a_tag['href'])
print('------')
