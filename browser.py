#this is the open source codes for the py.browser beta's 0.8 version. you can contact me on "tuna.kurekci@icloud.com"
import webbrowser
print ("welcome to py.browser beta!")

languages=("english","türkçe","deutsch")
language= (input("please choose a language:"))
def geben_sie_keinen_link_ein(zelda):
    try:
        webbrowser.open_new(zelda)
    except:
        print ("es tut uns leid, aber dieser link funktioniert nicht.")
def link_girme(link):
    try:
        webbrowser.open_new(link)
    except:
        print ("üzgünüz ama bu link çalışmıyor")
def entering_a_link(url):
    try:
        webbrowser.open_new(url)
    except:
        print ("sorry but this link doesn't work")
if language == "türkçe":
    link = (input("lütfen ziyaret etmek istediğiniz websitenin linkini yazın"))
    try:
        link_girme(link)
    except:
        link_girme(link)
elif language == "english":
    url = (input("please enter the url of the website you want to visit"))
    try:
        entering_a_link(url)
    except:
        entering_a_link(url)
elif language == "deutsch":
    zelda = (input("bitte geben sie den Link der website ein, die sie besuchen möchten."))
    try:
        geben_sie_keinen_link_ein(zelda)
    except:
        geben_sie_keinen_link_ein(zelda)
else:
    print  ("this language isn't supported yet. please try again")