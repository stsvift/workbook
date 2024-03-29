from lxml.etree import parse

doc = parse('test.xml')

for item in doc.iterfind('channel/item'):
  title = item.findtext('title')
  date = item.findtext('pubDate')
  link = item.findtext('link')

  print(title)
  print(date)
  print(link)
input()
