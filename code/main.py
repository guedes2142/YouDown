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
    print('|------------------------------------------|\n'
          '|------------------------------------------|')
    print(Fore.GREEN + ' /\_/\___  _   _   /   \_____      ___ __  ')
    print(Fore.RED + " \_ _/ _ \| | | | / /\ / _ \ \ /\ / / '_ \ ")
    print(Fore.CYAN + '  / \ (_) | |_| |/ /_// (_) \ V  V /| | | |')
    print(Fore.YELLOW + "  \_/\___/ \__,_/___,' \___/ \_/\_/ |_| |_|" + Style.RESET_ALL)
    print('|------------------------------------------|\n'
          '|------------------------------------------|')

def print_menu():
    print('|------------Choose an option--------------|')
    print()
    print(Fore.GREEN + '1: Download\n'
          '2: Exit' + Style.RESET_ALL)

def download_video():
    clear_screen()
    link_video = input('Enter a link to download: ')
    valid_link = 'https://www.youtube.com/watch'

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
