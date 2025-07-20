import subprocess
import webbrowser


url = 'https://www.notion.so/20a8ae1342ae80ddac46e847306ff5b2?v=20a8ae1342ae809c9d57000c16b06dad'
url2 = 'https://github.com/compress4j/compress4j'
webbrowser.get(using='google-chrome')
webbrowser.open_new(url=url)
webbrowser.open(url=url2)

command = ["/home/renas/.local/share/JetBrains/Toolbox/scripts/idea1", "/home/renas/workspace/compress4j"]

subprocess.run(command, check=True)



