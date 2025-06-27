import webbrowser
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

urllist = [
    "https://www.google.com/",
    "https://www.naver.com/"
    ]
for url in urllist:
    webbrowser.get(chrome_path).open(url)
