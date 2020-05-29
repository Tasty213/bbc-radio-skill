from mycroft import MycroftSkill, intent_file_handler


class BbcRadio(MycroftSkill):
    def __init__(self):
        # Create a new instance of the VLC player
        self.instance = vlc.Instance()

        # Create a list containing the URLs of all the radio stations .m3u8 files
        self.urls = ['http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_one.m3u8',
        'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_1xtra.m3u8',
        'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_two.m3u8',
        'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_three.m3u8',
        'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_fourfm.m3u8',
        'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_fourlw.m3u8',
        'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_four_extra.m3u8',
        'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_five_live.m3u8',
        'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_radio_five_live_sports_extra.m3u8',
        'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_6music.m3u8',
        'http://a.files.bbci.co.uk/media/live/manifesto/audio/simulcast/hls/uk/sbr_high/ak/bbc_asian_network.m3u8']

        # Create a new instance of the VLC media player
        self.player = vlc.MediaPlayer()

        # Initialise the Skills library
        MycroftSkill.__init__(self)

    @intent_file_handler('radio.bbc.intent')
    def handle_radio_bbc(self, message):
        self.speak_dialog('radio.bbc')

    def radioOne(self):
        media = self.instance.media_new(self.urls[0])

        self.player.set_media(media)

        self.player.play()

    def radioOneX(self):
        media = self.instance.media_new(self.urls[1])

        self.player.set_media(media)

        self.player.play()

    def radioTwo(self):
        media = self.instance.media_new(self.urls[2])

        self.player.set_media(media)

        self.player.play()

    def radioThree(self):
        media = self.instance.media_new(self.urls[3])

        self.player.set_media(media)

        self.player.play()

    def radioFourFM(self):
        media = self.instance.media_new(self.urls[4])

        self.player.set_media(media)

        self.player.play()

    def radioFourLW(self):
        media = self.instance.media_new(self.urls[5])

        self.player.set_media(media)

        self.player.play()

    def radioFourX(self):
        media = self.instance.media_new(self.urls[6])

        self.player.set_media(media)

        self.player.play()

    def radioFiveLive(self):
        media = self.instance.media_new(self.urls[7])

        self.player.set_media(media)

        self.player.play()

    def radioFiveLiveSportsExtra(self):
        media = self.instance.media_new(self.urls[8])

        self.player.set_media(media)

        self.player.play()

    def radioSixMusic(self):
        media = self.instance.media_new(self.urls[9])

        self.player.set_media(media)

        self.player.play()

    def radioAsianNetwork(self):
        media = self.instance.media_new(self.urls[10])

        self.player.set_media(media)

        self.player.play()

    def pause(self):
        self.player.stop()

    def play(self):
        self.player.play()



def create_skill():
    return BbcRadio()
