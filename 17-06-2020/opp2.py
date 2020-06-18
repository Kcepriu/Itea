class Phone:

    def __init__(self, model, imei):
        self.model = model
        self.imei = imei


    def call(self, number):
        print('Calling to %s' % number)

    def send_message(self, number):
        print('sending mesage to', number)

class Smartphone(Phone):

    def call(self, number):
        print('Connecting to ', number)
        Phone.call(self, number)

    def download_application(self, application_name):
        print('Downloading application from pley market ', application_name)

    def play_music(self, track_name):
        print('playing ', track_name)

phone = Phone('Nokia', '31256565566')

smartphone = Smartphone('Xiaomi', '123456789')

phone.call('445566')

print('smart')
smartphone.call('556677')

smartphone.play_music('mp3')