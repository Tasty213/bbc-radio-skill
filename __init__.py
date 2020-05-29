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

    # This is the function that loads and plays RadioOne. It is nearly identical
    # to the other functions bellow prefixed by 'radio', as such it will be the
    # only doccumented one
    @intent_handler('radio1.intent')
    def radioOne(self):
        # Create a new media instancem usinf the relevant URL as the source
        media = self.instance.media_new(self.urls[0])

        # Set the new media for the player
        self.player.set_media(media)

        # Ensure the player is playing
        self.player.play()

        # Tell the user that the radio is playing
        self.speak_dialog("radio1")

    @intent_handler('radio1X.intent')
    def radioOneX(self):
        media = self.instance.media_new(self.urls[1])

        self.player.set_media(media)

        self.player.play()

        self.speak_dialog("radio1X")

    @intent_handler('radio2.intent')
    def radioTwo(self):
        media = self.instance.media_new(self.urls[2])

        self.player.set_media(media)

        self.player.play()

        self.speak_dialog("radio2")

    @intent_handler('radio3.intent')
    def radioThree(self):
        media = self.instance.media_new(self.urls[3])

        self.player.set_media(media)

        self.player.play()

        self.speak_dialog("radio3")

    @intent_handler('radio4FM.intent')
    def radioFourFM(self):
        media = self.instance.media_new(self.urls[4])

        self.player.set_media(media)

        self.player.play()

        self.speak_dialog("radio4FM")

    @intent_handler('radio4LW.intent')
    def radioFourLW(self):
        media = self.instance.media_new(self.urls[5])

        self.player.set_media(media)

        self.player.play()

        self.speak_dialog("radio4LW")

    @intent_handler('radio4X.intent')
    def radioFourX(self):
        media = self.instance.media_new(self.urls[6])

        self.player.set_media(media)

        self.player.play()

        self.speak_dialog("radio4X")

    @intent_handler('radio5Live.intent')
    def radioFiveLive(self):
        media = self.instance.media_new(self.urls[7])

        self.player.set_media(media)

        self.player.play()

        self.speak_dialog("radio5Live")

    @intent_handler('radio5LiveSportsExtra.intent')
    def radioFiveLiveSportsExtra(self):
        media = self.instance.media_new(self.urls[8])

        self.player.set_media(media)

        self.player.play()

        self.speak_dialog("radio5LiveSportsExtra")

    @intent_handler('radio6Music.intent')
    def radioSixMusic(self):
        media = self.instance.media_new(self.urls[9])

        self.player.set_media(media)

        self.player.play()

        self.speak_dialog("radio6Music")

    @intent_handler('radioAsianNetwork.intent')
    def radioAsianNetwork(self):
        media = self.instance.media_new(self.urls[10])

        self.player.set_media(media)

        self.player.play()

        self.speak_dialog("radioAsianNetwork")

    # this function pauses the player, note that player.pause() did not work,
    # will submit and issue to python-vlc
    def pause(self):
        self.player.stop()

    # Resume playing the player
    def play(self):
        self.player.play()

    # Stop the player from playing before quitting
    def stop(self):
        self.player.stop()


def create_skill():
    return BbcRadio()
