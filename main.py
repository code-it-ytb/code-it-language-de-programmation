import socket
import getpass
import webbrowser

def watchlastestvideo():
  webbrowser.open("bit.ly/code-it-lastest-video")

def openprojecturl(projectname):
  url = "https://github.com/code-it-ytb/" + projectname + "/archive/refs/heads/main.zip"
  webbrowser.open(url)

print("Language de programmation Code It")

running = True

while running:
  codeline = input(getpass.getuser() + "@" + socket.gethostname() + ":~$")
  if "getproject " in codeline:
    projectname = codeline.replace('getproject ', '')
    openprojecturl(projectname)
  if codeline == "watch_lastest_video":
    watchlastestvideo()
