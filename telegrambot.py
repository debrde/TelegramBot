#coder :- Salman Faris

import sys
import time
import telepot
import RPi.GPIO as GPIO

#LED
def on(pin):
        GPIO.output(pin,GPIO.HIGH)
        return
def off(pin):
        GPIO.output(pin,GPIO.LOW)
        return
# use Raspberry Pi board pin numbers (GPIO.BOARD) or gpio pin numbers (GPIO.BCM)
GPIO.setmode(GPIO.BOARD)

# set up GPIO output channel
GPIO.setup(3, GPIO.OUT)
print('setup')
time.sleep(2)
GPIO.output(3, GPIO.HIGH)
print('set output GPIO.high')
time.sleep(5)
GPIO.output(3, GPIO.LOW)
print('set output GPIO.low')
print('...')
time.sleep(2)
print('continuing..')

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    if command == 'On':
       bot.sendMessage(chat_id, on(3))
    elif command =='Off':
       bot.sendMessage(chat_id, off(3))

bot = telepot.Bot('581393215:AAHSzS924XDDXITa2s2k9Aqq-FJpPrnVfoM')
bot.message_loop(handle)
print('I am listening...')

while 1:
    try:
        time.sleep(10)
    
    except KeyboardInterrupt:
        print('\n Program interrupted')
        GPIO.cleanup()
        exit()
    
    except:
        print('Other error or exception occured!')
        GPIO.cleanup()
