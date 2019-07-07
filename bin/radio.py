####################################################################################
#   Title:       Radio                   ###########################################   
############################################      Version:    2.0.4                #
##################################################   Author:     Igor Bistrovic ####
##############################################################   Date: 2018-01-20  #
#   About:       Pokretanje odabranih internet radija                              #
####################################################################################
#   UpdateNotes: 19-07-07 provjeren                                                #
#                         izmjena konvencija                                       #
#                         rename app                                               #
####################################################################################

import subprocess
import os
import sys

#linkovi:
antena = 'http://streaming.antenazagreb.hr/stream/player.html'
enter = 'http://streaming.enterzagreb.hr/main/popup.html'
otvoreni_web = 'http://www.otvoreni.hr/player/'
otvoreni_tunein = 'https://tunein.com/radio/Otvoreni-Radio-926-s18415/'
sljeme = 'http://radio.hrt.hr/stream/10/'
yammat = 'http://yammat.fm/'
good_life_radio = 'https://www.youtube.com/watch?v=ftJYyevC6Us'
the_best_of_mozart = 'https://www.youtube.com/watch?v=Rb0UmrCXxVA'
one_love_hip_hop_radio = 'https://tunein.com/radio/One-Love-Hip-Hop-Radio-s125403/?locale=zh-CN&z=654864307'
the_rap_mixx = 'https://tunein.com/radio/The-Rap-MIXX-s190580/'

start_app = input("Run radio_v2.0.2? (y/n) ")
if start_app=="y":
    print('  |      Radio           | Info ') 
    print('1 | Antena Zagreb        |  ')
    print('2 | Ent3r                |  ')
    print('3 | OneLove HipHop Radio | tunein ')
    print('4 | Otvoreni Radio       |  ')
    print('5 | Radio Sljeme         |  ')
    print('6 | The Best of Mozart   | youtube ')
    print('7 | The Rap MIXX         | tunein ')
    print('8 | Yammat fm            |  ')

    selection = input ("\nSelect number: ")

    if selection=="1":
        url = antena
        input ("Antena Zagreb selected. Press Enter to continue...")
    elif selection=="2":
        url = enter
        input ("Ent3r Zagreb selected. Press Enter to continue...")
    elif selection=="3":
        url = one_love_hip_hop_radio
        input ("OneLove HipHop Radio selected. Press Enter to continue...")
    elif selection=="4":
        print('1 | Otvoreni Radio     | web page ')
        print('2 | Otvoreni Radio     | tunein ')
        selection2 = input ("\nSelect number: ")
        if selection2=="1":
            url = otvoreni_web
            input ("Otvoreni radio selected. Press Enter to continue...")
        elif selection2=="2":
            url = otvoreni_tunein
            input ("Otvoreni radio selected. Press Enter to continue...")
        else:
            input ("\nWrong input!\n\nPress the enter key to exit.")
    elif selection=="5":
        url = sljeme
        input ("Radio Sljeme selected. Press Enter to continue...")
    elif selection=="8":
        url = yammat
        input ("yammat.fm selected.\nNote!!! You need to click play once webpage opens.\n\nPress Enter to continue...")
    elif selection=="6":
        url = the_best_of_mozart
        input ("The Best of Mozart selected. Press Enter to continue...")
    elif selection=="7":
        url = the_rap_mixx
        input ("The Rap MIXX selected. Press Enter to continue...")
    else:
        input ("\nWrong input!\n\nPress the enter key to exit.")
else:
    input("\nPress Enter to exit.")

if sys.platform=='win32':
    os.startfile(url)
elif sys.platform=='darwin':
    subprocess.Popen(['open', url])
else:
    try:
        subprocess.Popen(['xdg-open', url])
    except OSError:
        #print 'Please open a browser on: '+url
        print ("bokbok")


# notes:

#-napraviti izbornik domace/youtube/strano?
#-ispraviti prikaz greske na kraju kad nema izbora (kad ne dobije url)

#youtube:
#mozart
#8 Hours The Best of Mozart: Mozart's Greatest Works, Classical Music Playlist, Instrumental Music | https://www.youtube.com/watch?v=lspBFo0tKwI&t=9s
#Classical Music for Studying and Concentration | Mozart Music Study, Relaxation, Reading | https://www.youtube.com/watch?v=vwIUJbIU57s
#6 Hours Mozart for Studying, Concentration, Relaxation | https://www.youtube.com/watch?v=shoVsQhou-8
#
#Best English Songs 2017-2018 Hits | Live Stream 24/7 | New Hits | Best Acoustic Mix Covers 2018 | https://www.youtube.com/watch?v=nd-sP_sjT1A
#24/7 Lofi Hiphop Radio - Beats to Study/Game/Relax *NEW* | https://www.youtube.com/watch?v=NofKmH-H76I
# |


# za copy-paste
#print('n | xxxxxxxxxxxx      | xxxxxxx ')
#if selection=="n":
#    url = xx
#    input ("xx selected. Press Enter to continue...")