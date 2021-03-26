import telepot
import Arduino
import traceback
import time

ATIVA_LEDR = b'2'
DEACTIVATE_LEDR = b'3'
ACTIVATE_LEDG = b'4'
DEACTIVATE_LEDG = b'5'
ACTIVATE_LEDB = b'6'
DEACTIVATE_LEDB = b'7'
TEMP = b'8'
LUZ = b'9'
ACTIVATE_RELE = b'A'
DEACTIVATE_RELE = b'B'

class Telegram(telepot.Bot):
    def __init__(self, token):
        super(Telegram, self).__init__(token)
        self.serial = Arduino.start_communication()

    def handle_message(self, msg):
        if 'text' not in msg:
            return

        if msg['text'].startswith('/'):
            self.handle_command(msg)

    def handle_start(self, msg):
        self.sendMessage(msg['chat']['id'], "Your phone going to format in:")
        time.sleep(1);
        self.sendMessage(msg['chat']['id'], "5 seconds...")
        time.sleep(1);
        self.sendMessage(msg['chat']['id'], "4 seconds...")
        time.sleep(1);
        self.sendMessage(msg['chat']['id'], "3 seconds...")
        time.sleep(1);
        self.sendMessage(msg['chat']['id'], "2 seconds...")
        time.sleep(1);
        self.sendMessage(msg['chat']['id'], "1 seconds...")
        time.sleep(1);
        self.sendMessage(msg['chat']['id'], "Formatting Phone...")
        time.sleep(3);
        self.sendMessage(msg['chat']['id'], "Congratulations\n Your phone is success formatted")
    def handle_help(self, msg):
        self.sendMessage(msg['chat']['id'], "Command List\n /hello\n /hi\n /bye\n /morning\n")
    def handle_ayuda(self, msg):
        self.sendMessage(msg['chat']['id'], "Command List\n /temp\n /luz\n /rele\n /red\n /green\n /blue\n")
    def handle_hello(self, msg):
        self.sendMessage(msg['chat']['id'], "Hello, how are you?")
    def handle_hi(self, msg):
        self.sendMessage(msg['chat']['id'], "Hi, all good here")
    def handle_bye(self, msg):
        self.sendMessage(msg['chat']['id'], "Good bye!")
    def handle_morning(self, msg):
        self.sendMessage(msg['chat']['id'], "Hello, Good Morning :)")
      
    def handle_temp(self, msg):

        self.serial.write(TEMP)

        response = self.serial.readline()

        if not response:
            response = 'No Response'
        else:
            response = 'arduino: ' + response.decode('utf-8')

        self.sendMessage(msg['chat']['id'], response)

    def handle_luz(self, msg):

       self.serial.write(LUZ)

        response = self.serial.readline()

        if not response:
            response = 'No Response'
        else:
            response = 'arduino: ' + response.decode('utf-8')

        self.sendMessage(msg['chat']['id'], response)

    def handle_red(self, msg):
        self.sendMessage(msg['chat']['id'], "RED LED ON")

        self.serial.write(ATIVA_LEDR)

        response = self.serial.readline()

        if not response:
            response = 'No Response'
        else:
            response = 'arduino: ' + response.decode('utf-8')

        self.sendMessage(msg['chat']['id'], response)

    def handle_redoff(self, msg):
        self.sendMessage(msg['chat']['id'], "TURNING OFF RED LED")

        self.serial.write(DEACTIVATE_LEDR)

        response = self.serial.readline()

        if not response:
            response = 'No Response'
        else:
            response = 'arduino: ' + response.decode('utf-8')

        self.sendMessage(msg['chat']['id'], response)


    def handle_green(self, msg):
        self.sendMessage(msg['chat']['id'], "GREEN LED ON")

        self.serial.write(ACTIVATE_LEDG)

        response = self.serial.readline()

        if not response:
            response = 'No responde'
        else:
            response = 'arduino: ' + response.decode('utf-8')

        self.sendMessage(msg['chat']['id'], response)

    def handle_greenoff(self, msg):
        self.sendMessage(msg['chat']['id'], "GREEN LED OFF")

        self.serial.write(DEACTIVATE_LEDG)

        response = self.serial.readline()

        if not response:
            response = 'No Response'
        else:
            response = 'arduino: ' + response.decode('utf-8')

        self.sendMessage(msg['chat']['id'], response)

    def handle_blue(self, msg):
        self.sendMessage(msg['chat']['id'], "BLUE LED ON")

        self.serial.write(ACTIVATE_LEDB)

        response = self.serial.readline()

        if not response:
            response = 'No responde'
        else:
            response = 'arduino: ' + response.decode('utf-8')

        self.sendMessage(msg['chat']['id'], response)

    def handle_blueoff(self, msg):
        self.sendMessage(msg['chat']['id'], "BLUE LED OFF")

        self.serial.write(DEACTIVATE_LEDB)

        response = self.serial.readline()

        if not response:
            response = 'No Response'
        else:
            response = 'arduino: ' + response.decode('utf-8')

        self.sendMessage(msg['chat']['id'], response)

    def handle_rele(self, msg):
        self.sendMessage(msg['chat']['id'], "LIGHTS ON")

        self.serial.write(ACTIVATE_RELE)

        response = self.serial.readline()

        if not response:
            response = 'No Response'
        else:
            response = 'arduino: ' + response.decode('utf-8')

        self.sendMessage(msg['chat']['id'], response)

    def handle_releoff(self, msg):
        self.sendMessage(msg['chat']['id'], "LIGHTS OFF")

        self.serial.write(DEACTIVATE_RELE)

        response = self.serial.readline()

        if not response:
            response = 'No Response'
        else:
            response = 'arduino: ' + response.decode('utf-8')

        self.sendMessage(msg['chat']['id'], response)

    def handle_command(self, msg):

        method = 'handle_' + msg['text'][1:]

        if hasattr(self, method):
            getattr(self, method)(msg)

    def runBot(self):
        last_offset = 0
        print('RUNNING')

        while True:
            try:
                updates = self.getUpdates(timeout=60, offset=last_offset)

                if updates:
                    for u in updates:
                        self.handle_message(u['message'])

                    last_offset = updates[-1]['update_id'] + 1

            except KeyboardInterrupt:
                break
            except:
                traceback.print_exc()

bot = TelegramTutorial('TELEGRAM-API')
bot.runBot()
