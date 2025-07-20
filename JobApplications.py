

import webbrowser

url = 'https://www.notion.so/20a8ae1342ae80ddac46e847306ff5b2?v=20a8ae1342ae809c9d57000c16b06dad'
url2 = 'https://www.linkedin.com/feed/'
url3 = 'https://gemini.google.com/app'
one = webbrowser.get(using='google-chrome')
one.open_new(url=url)
one.open(url="https://docs.google.com/spreadsheets/d/1zg-lkPzrbjeEZ730ED-BXQ-xUVIJqBWp0GFH149GyrU/edit?gid=0#gid=0")
one.open(url=url2)
one.open(url=url3)

two = webbrowser.get(using='google-chrome')
two.open_new(url="https://uk.indeed.com/")

