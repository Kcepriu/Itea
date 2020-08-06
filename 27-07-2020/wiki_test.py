import wikipedia

wikipedia.set_lang("uk")
ttt = wikipedia.search("Мена")
print(ttt)
rr = wikipedia.page("Мена (місто)")
print(rr.content)