from mycroft import MycroftSkill, intent_file_handler


class Insurance(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('insurance.intent')
    def handle_insurance(self, message):
        self.speak_dialog('insurance')


def create_skill():
    return Insurance()

