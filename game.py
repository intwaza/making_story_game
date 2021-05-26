class User:
    def __init__(self,noun,p_noun,noun2,place,adjective,noun3):
        self.noun=noun
        self.p_noun=p_noun
        self.noun2=noun2
        self.place=place
        self.adjective=adjective
        self.noun3=noun3
    def story(self):
        
        print(f"Once upon there was a {self.noun} who was big ,clear and {self.noun2}")
        print(f"you may think he was harm but he was {self.noun3}")
        print(f"you can't get them but I know they are located in {self.place}")
        print(f"when you saw it, you may think it {self.adjective} but it is {self.p_noun}")
           

user= User(noun = input("Choose a noun: "), p_noun = input("Choose a plural noun: "),noun2 = input("Choose a noun: "),place = input("Name a place: "),adjective = input("Choose an adjective (Describing word): "), noun3 = input("Choose a noun: "))
user.story()