import socket
import getpass
import webbrowser

def subscribe():
    webbrowser.open("https://www.youtube.com/channel/UCnJYex8gca2Q6lVQAjVOLNg/?sub_confirmation=1")

def watchlastestvideo():
    webbrowser.open("https://code-it-ytb.github.io/shorten_urls/lastest_video/")

def openprojecturl(projectname):
    url = "https://github.com/code-it-ytb/" + projectname + "/archive/refs/heads/main.zip"
    webbrowser.open(url)
    
def downloadapp(appname):
    url = "https://code-it-ytb.github.io/download_app/" + appname
    webbrowser.open(url)

print("Langage de programmation de Code It (CILP)")
print("Tapez 'help' pour de l'aide")

running = True

while running:
    codeline = input(getpass.getuser() + "@" + socket.gethostname() + ":~$")
    if "getproject " in codeline:
        projectname = codeline.replace('getproject ', '')
        openprojecturl(projectname)
    elif codeline == "watch_lastest_video":
        watchlastestvideo()
    elif codeline == "subscribe":
        subscribe()
    elif "download_app" in codeline:
        atd = codeline.replace('download_app', '')
        downloadapp(atd)
    elif codeline == "exit":
        exit()
    elif codeline == "help":
        print("""Fonctions :

    -getproject :
    
        permet de téléharger les fichiers sources d'un projet
        
        utilisation : getproject 'nom_du_projet_ici'
    
    -watch_lastest_video :
        
        permet de visionner la dernière vidéo
        
        utilisation : watch_lastest_video
        
    -subscribe:
        
        permet de s'abonner
        
        utilisation : subscribe
        
    -download_app
        
        télécharge une appli nessésaire au projet
        
        utilisation: download_app 'nom_de_l_appli_a_telecharger.exe'
        
    -help 
    
        affiche l'aide
        
        utilisation : help
    
    -exit
    
        eteint CILP
        
        utilisation : exit""")
        
