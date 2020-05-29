from mycroft import MycroftSkill, intent_file_handler


class BbcRadio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('radio.bbc.intent')
    def handle_radio_bbc(self, message):
        self.speak_dialog('radio.bbc')


def create_skill():
    return BbcRadio()

