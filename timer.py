import os
from colorama import Fore
from colorama import Style
from time import sleep
from pydub import AudioSegment
from pydub.playback import play
os.system('clear')

try :
    jam = int(input("Masukkan jamnya      : "))
    menit = int(input("Masukkan menitnya    : "))
    detik = int(input("Masukkan detiknya    : "))

except :
    print(Fore.RED + Style.BRIGHT + "\nInvalid input. Pastikan input yang kamu masukkan sudah benar!" + Style.RESET_ALL)

if (menit > 60) or (detik > 60) or (menit < 0) or (jam < 0) or (detik < 0) :
    print(Fore.RED + Style.BRIGHT + "\nInvalid input. Pastikan input yang kamu masukkan sudah benar!" + Style.RESET_ALL)

else :
    while True :
        if (detik < 0) and (menit != 0) :
            detik = 59
            menit = menit - 1
        
        if (detik < 0) and (menit >= 0) and (jam != 0) :
            detik = 59
            menit = 59
            jam = jam - 1

        if (detik == 0) and (menit == 0) and (jam == 0) :
            break

        os.system("clear")
        print(str(jam) + ":" + str(menit) + ":" + str(detik))
        sleep(1)
        os.system("clear")

        detik = detik - 1

    os.system("notify-send Gtimer \"Time's up.\"")
    print("Tekan Ctrl+c untuk mematikan timer.")
    # os.system("mpg123 ~/projects/python/timer-py/sound.mp3 && clear")
    try :
        play(AudioSegment.from_mp3("sound.mp3"))
    except :
        os.system("clear")
        print(Fore.YELLOW + Style.BRIGHT + "----------------------------------------------------------" + Style.RESET_ALL)
        print(Fore.GREEN + Style.BRIGHT + "     -->" + Style.RESET_ALL, "Quitting...")
    print(Fore.YELLOW + Style.BRIGHT + "----------------------------------------------------------" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "     -->" + Style.RESET_ALL, "Terima kasih telah menggunakan.")
    print(Fore.YELLOW + Style.BRIGHT + "----------------------------------------------------------" + Style.RESET_ALL)
    print(Fore.GREEN + Style.BRIGHT + "     -->" + Style.RESET_ALL, "Made with love by : Gabriel Cesar Hutagalung")
    print(Fore.YELLOW + Style.BRIGHT + "----------------------------------------------------------" + Style.RESET_ALL)
