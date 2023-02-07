from pytube import YouTube
import time
from colorama import Fore, Back, Style
import colorama

def downloadVideo():
  colorama.init(autoreset=True)

  border = f'{Fore.LIGHTRED_EX}-------------------------------------------------------------'

  # app view
  print(f'''{Fore.LIGHTYELLOW_EX}
  ██─██─████─█─█─███─█─█─████──███────████──████─█───█─█──█─█───████─████─████──███─████
  ─███──█──█─█─█──█──█─█─█──██─█──────█──██─█──█─█───█─██─█─█───█──█─█──█─█──██─█───█──█
  ──█───█──█─█─█──█──█─█─████──███────█──██─█──█─█─█─█─█─██─█───█──█─████─█──██─███─████
  ──█───█──█─█─█──█──█─█─█──██─█──────█──██─█──█─█████─█──█─█───█──█─█──█─█──██─█───█─█─
  ──█───████─███──█──███─████──███────████──████──█─█──█──█─███─████─█──█─████──███─█─█─
  ''')
  print(border)
  print(f'{Fore.LIGHTBLUE_EX}{time.ctime()}')
  print(border)

  # user input link and place
  link  = input(f'{Fore.YELLOW}link      : ') 
  place = input(f'{Fore.YELLOW}direktori : ') 
  print(border)

  # get video from link
  yt = YouTube(link)

  # show information contained in the video
  print(f'{Fore.GREEN}Title  : {yt.title}')
  print(f'{Fore.GREEN}Views  : {yt.views}')
  print(f'{Fore.GREEN}Author : {yt.author}')
  print(border)

  # get highest resolution and donwload it
  yt_dwnld = yt.streams.get_highest_resolution()
  yt_dwnld.download(place)

  # show if your downloading is done
  print(f'{Fore.LIGHTBLUE_EX}DONE!!!')
  print(border)

if __name__ == '__main__':
  downloadVideo()
  
