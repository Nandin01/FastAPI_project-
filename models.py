from mongoengine import Document, StringField, IntField

class Run_info(Document):

    someID = StringField(max_length=50)
    Fillnumber = StringField()
    phaseShift1 = IntField()
    phaseShift2 = IntField()
    StartTime = IntField()
    StartTimeC = StringField()
    Entries = IntField()
    lumiAtIP1 = IntField()
    lumiAtIP1withSNDLHC = IntField()
    OfflineMonitoring = StringField()
    