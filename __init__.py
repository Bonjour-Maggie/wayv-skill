from mycroft import MycroftSkill, intent_file_handler


class Wayv(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('wayv.intent')
    def handle_wayv(self, message):
        self.speak_dialog('wayv')


def create_skill():
    return Wayv()

