# from abc import ABC

class Band():
    instances = []

    def __init__(self,name,members):
        self.name = name
        self.members = members
        Band.instances.append(self)
        # self.__class__.all_bands.append(self)

    def play_solos(self):
      solos = []
      for member in self.members:
          solos.append(member.play_solo())
      return tuple(solos)

    @classmethod
    def to_list(cls):
      return cls.instances

class Musician(Band):
    def __init__(self,name):
        self.name = name


class Guitarist(Musician):
    def __str__(self):
      return f"My name is {self.name} and I play guitar"
    
    def __repr__(self):
      return f"Guitarist instance. Name = {self.name}"

    @staticmethod
    def play_solo():
      return "face melting guitar solo"
    
    @classmethod
    def get_instrument(cls):
      return "guitar"
    

class Bassist(Musician):
    def __str__(self):
      return f"My name is {self.name} and I play bass"

    def __repr__(self):
      return f"Bassist instance. Name = {self.name}"

    @staticmethod
    def play_solo():
      return "bom bom buh bom"
      
    @classmethod
    def get_instrument(cls):
      return "bass"

class Drummer(Musician):
    def __str__(self):
      return f"My name is {self.name} and I play drums"

    def __repr__(self):
      return f"Drummer instance. Name = {self.name}"
    
    @staticmethod
    def play_solo():
      return "rattle boom crash"
    
    @classmethod
    def get_instrument(cls):
      return "drums"

