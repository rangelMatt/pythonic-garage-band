class Band():
    instances = []

    def __init__(self,name,members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
      solos = []
      for member in self.members:
          solos.append(member.play_solo())
      return solos

    @classmethod
    def to_list(cls):
      return cls.instances

    @staticmethod
    def describe():
      return "Plays rock"

      # if you 

class Musician():
    instrument = ""
    title = ""
    solo = ""

    def __init__(self,name):
        self.name = name
        # self.name, is setting an attribute to the instance, so each self attribute, has a name.

    def __str__(self):
      return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
      return f"{self.instrument} instance. Name = {self.name}"

    def get_instrument(self):
      return f"{self.instrument}"

    def play_solo(self):
      return f"{self.solo}"

class Guitarist(Musician):

    @staticmethod
    def play_solo():
      return "face melting guitar solo"

class Bassist(Musician):

    @staticmethod
    def play_solo():
      return "bom bom buh bom"

class Drummer(Musician):
    
    @staticmethod
    def play_solo():
      return "rattle boom crash"
    

