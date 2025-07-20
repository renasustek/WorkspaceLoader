import os
import subprocess
import webbrowser


new = 2 # open in a new tab, if possible

# open a public URL, in this case, the webbrowser docs
url = "http://docs.python.org/library/webbrowser.html"
webbrowser.get(using='google-chrome').open(url,new=new)

command = ["/home/renas/.local/share/JetBrains/Toolbox/scripts/idea1", "/home/renas/workspace/compress4j"]

os.run(command, check=True)

url = 'http://docs.python.org/'


