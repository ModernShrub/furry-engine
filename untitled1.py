from tkinter import*
import json as j
import requests as r

root = Tk()
root.title("News App")
root.overrideredirect(True)
root.geometry("500x400")

title = Label(root, text="BBC News", font=("Arial",20,"bold"), fg ="firebrick1")
title.pack()

news1 = Label(root, wraplength=500, justify=LEFT, font=("Arial",10,"bold"))
news1.pack()
desc1 = Label(root, wraplength=500, justify=LEFT, font=("Arial",8))
desc1.pack()

news2 = Label(root, wraplength=500, justify=LEFT, font=("Arial",10,"bold"))
news2.pack()
desc2 = Label(root, wraplength=500, justify=LEFT, font=("Arial",8))
desc2.pack()

news3 = Label(root, wraplength=500, justify=LEFT, font=("Arial",10,"bold"))
news3.pack()
desc3 = Label(root, wraplength=500, justify=LEFT, font=("Arial",8))
desc3.pack()

news4 = Label(root, wraplength=500, justify=LEFT, font=("Arial",10,"bold"))
news4.pack()
desc4 = Label(root, wraplength=500, justify=LEFT, font=("Arial",8))
desc4.pack()

news5 = Label(root, wraplength=500, justify=LEFT, font=("Arial",10,"bold"))
news5.pack()
desc5 = Label(root, wraplength=500, justify=LEFT, font=("Arial",8))
desc5.pack()

def getnews():
    apir = r.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=d49274990f6b415a980e15a5e4f5630a")
    bbcpg = j.loads(apir.content)
    
    news1['text'] ="1."+ str(bbcpg["articles"][0]["title"])
    desc1['text'] = str(bbcpg["articles"][0]["description"])
    
    news2['text'] ="2."+ str(bbcpg["articles"][1]["title"])
    desc2['text'] = str(bbcpg["articles"][1]["description"])
    
    news3['text'] ="3."+ str(bbcpg["articles"][2]["title"])
    desc3['text'] = str(bbcpg["articles"][2]["description"])
    
    news4['text'] ="4."+ str(bbcpg["articles"][3]["title"])
    desc4['text'] = str(bbcpg["articles"][3]["description"])
    
    news5['text'] ="5."+ str(bbcpg["articles"][4]["title"])
    desc5['text'] = str(bbcpg["articles"][4]["description"])
    
getnews()

root.mainloop()