import webbrowser

# webbrowser.open("https://docs.python.org/3.10/library/webbrowser.html", new=2)

help(webbrowser)

browser = webbrowser.get('windows-default')
browser.open_new_tab("https://docs.python.org/3.10/library/webbrowser.html")

# documentation states that : Open url in a new window of the default browser, if possible, otherwise,
# open url in the only browser window - for open_new_tab() method the keyword here is `if possible`
# when came across to poorly written documentation for a module or function only option is searching through internet
