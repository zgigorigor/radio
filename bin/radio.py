##########################################
# Title:                           Radio
# 
#                Created: 2018-12-08
#                 Author: Bistrovic Igor
#
#                Version: 3.0.0
# 
# About: Pokretanje odabranih internet 
#        radija
# 
# Update: 
# 18-12-08 - implementacija radio.ini datoteke
#
##########################################

import configparser
import logging


logging.basicConfig(level=logging.DEBUG,
                    datefmt='%Y-%m-%d %a %H:%M:%S', 
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    filename='D:/dev/logs/radio_log.txt',
                    )
#logging.info('info')
#logging.debug('radnje')
#logging.warning('upozorenja')

# [ POCETAK PROGRAMA ]
logging.info('Radio_v3 started.')

config.read('radio.ini')


# [ KRAJ PROGRAMA ]
input ("\nPress Enter to continue...")
logging.info('Radio_v3 closed.')