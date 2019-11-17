import webbrowser, time, random

searches = ["why does my poo float", "how does one tie their shoes", "how much kombucha does it take to get drunk"]

for search in searches:
    time.sleep(random.randint(0, 10))
    webbrowser.open_new_tab("https://google.com/search?q=" + "+".join(search.split()))