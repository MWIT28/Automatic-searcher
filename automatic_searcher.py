import webbrowser
import time
filepath = "test2.txt"
f = open(filepath, "r", encoding="utf-8")
i = 0
while i < 5:

    webbrowser.get('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s').open_new_tab('https://www.google.pl/search?q=' + f.readline())
    i = i + 1
    time.sleep(2)


f.close()



