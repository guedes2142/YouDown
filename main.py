from pytube import YouTube
from colorama import Fore, Style
import os
from time import sleep
import platform

def clear_screen():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def print_title():

    print(Fore.RED + '██╗   ██╗ ██████╗ ██╗   ██╗██████╗  ██████╗ ██╗    ██╗███╗   ██╗' + Style.RESET_ALL)
    print(Fore.RED + '╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗██╔═══██╗██║    ██║████╗  ██║' + Style.RESET_ALL)
    print(Fore.RED + ' ╚████╔╝ ██║   ██║██║   ██║██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║' + Style.RESET_ALL)
    print(Fore.CYAN + '  ╚██╔╝  ██║   ██║██║   ██║██║  ██║██║   ██║██║███╗██║██║╚██╗██║' + Style.RESET_ALL)
    print(Fore.CYAN + '   ██║   ╚██████╔╝╚██████╔╝██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║' + Style.RESET_ALL)
    print(Fore.WHITE + '   ╚═╝    ╚═════╝  ╚═════╝ ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝' + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT +'                      By.Rafael Guedes')
    print(Fore.YELLOW + Style.BRIGHT +'                     Github: /guedes2142' + Style.RESET_ALL)

def print_menu():
    print()
    print(Fore.RED + Style.BRIGHT + '-----------------------Choose an option----------------------')
    print()
    print(Fore.GREEN + Style.BRIGHT + '1: DOWNLOAD\n'
          '2: Exit' + Style.RESET_ALL)

def download_video():
    clear_screen()
    valid_link = 'https://www.youtube.com/watch'
    
    link_video  = input('Video link: ')

    if link_video.startswith(valid_link):
        print('Choose a resolution\n'
                           '1: 1080p\n'
                           '2: 720p\n'
                           '3: 360')
        resolution = input('> ')

        if resolution == '1':
            yt = YouTube(f'{link_video}')
            streams = yt.streams.get_by_itag(137)
            try:
                print('Downloading...')
                streams.download()
                if streams:
                    print(Fore.GREEN + 'Download Complete' + Style.RESET_ALL)
                    print(Fore.YELLOW + 'Consider following me on GitHub if this app was useful to you, and give it a star.'+ Style.RESET_ALL)
                    sleep(2)
                return True
            except:
                print('Error')
                return False
        elif resolution == '2':
            yt = YouTube(f'{link_video}')
            streams = yt.streams.get_by_itag(22)
            try:
                print('Downloading...')
                streams.download()
                if streams:
                    print(Fore.GREEN + 'Download Complete' + Style.RESET_ALL)
                    print(Fore.YELLOW + 'Consider following me on GitHub if this app was useful to you, and give it a star.'+ Style.RESET_ALL)
                    sleep(2)
                return True
            except:
                print('Error')
                return False
        elif resolution == '3':
            yt = YouTube(f'{link_video}')
            streams = yt.streams.get_by_itag(18)
            try:
                print('Downloading...')
                streams.download()
                if streams:
                    print(Fore.GREEN + 'Download Complete' + Style.RESET_ALL)
                    print(Fore.YELLOW + 'Consider following me on GitHub if this app was useful to you, and give it a star.'+ Style.RESET_ALL)
                    sleep(2)
                return True
            except:
                print('Error')
                return False
        else:
            print('Invalid resolution')
            return False
    else:
        print('Invalid link')
        return False

def main():
    clear_screen()
    print_title()

    while True:
        print_menu()
        options = input('> ')
        if options != '1' and options != '2':
            print('Invalid option')
            continue

        if options == '1':
            if download_video():
                break

        if options == '2':
            break

if __name__ == '__main__':
    main()
