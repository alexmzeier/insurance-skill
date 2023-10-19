from va import MycroftSkill, intent_handler
from va.adapt.intent import IntentBuilder
from va.skills.context import adds_context, removes_context
from va.dataModel import UserSkillMetis


def create_skill(skill_data: UserSkillMetis):
    return Insurance(skill_data)


class Insurance(MycroftSkill):
    def __init__(self, skill_data: UserSkillMetis):
        MycroftSkill.__init__(self, skill_data=skill_data)


    @intent_handler(IntentBuilder("StatusCallHelper").require("status").require("care"))
    def handle_call(self, message, websocket):
        #call_api = skill_api(self.skill_data.identifier, self.skill_data.api_key, message.data["utterance"])
        #print('result call api ' + call_api)
        #print('Message Data Utterance ' + message.data["utterance"])
        self.speak('Deine Pflegeantrag ist noch in der Bearbeitung', websocket=websocket)

    
    @intent_handler(IntentBuilder("CareCallHelper").require("care"))
    def handle_care(self, message, websocket):
        #call_api = skill_api(self.skill_data.identifier, self.skill_data.api_key, message.data["utterance"])
        #print('result call api ' + call_api)
        #print('Message Data Utterance ' + message.data["utterance"])
        self.speak('Hier ist dein Pflegeantrag', websocket=websocket)

