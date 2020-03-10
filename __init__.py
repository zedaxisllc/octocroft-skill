from mycroft import MycroftSkill, intent_file_handler


class Octocroft(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('octocroft.intent')
    def handle_octocroft(self, message):
        self.speak_dialog('octocroft')


def create_skill():
    return Octocroft()

