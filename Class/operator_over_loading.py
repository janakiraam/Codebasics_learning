from datetime import datetime

class Cricketplayer:
    def __init__(self,fname,lname,birth_year,team):
        self.first_name=fname
        self.last_name=lname
        self.birth_year = birth_year
        self.team=team
        self.scores=[]
    
    def add_Score(self,score):
        self.scores.append(score)

    def get_average_score(self):
        return sum(self.scores)/len(self.scores)
    
    def find_age(self):
        current_year = datetime.now().year
        age = current_year - self.birth_year
        return age
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name} is cirketplayer from {self.team}")  
    
    ### less than operator overloading.
    
    def __lt__(self,other):
        get_average_score = self.get_average_score()
        get_other_average_score = other.get_average_score()
        return get_average_score < get_other_average_score
    

    ### equal to operator overloading

    def __eq__(self,other):
        get_age= self.find_age()
        get_other_age = other.find_age()
        return get_age == get_other_age




virat = Cricketplayer('virat','kohil',1998,"India")

print(virat) #this will trigger __str__

virat.add_Score(79)
virat.add_Score(49)

print(virat.first_name)
print(virat.last_name)
print(virat.team)
print(virat.scores)
print(virat.get_average_score())
j=virat.find_age()
print(f"Age of virat: {j}")


david = Cricketplayer('david','warner',1996,"Aus")

print(david) #this will trigger __str__

david.add_Score(89)
david.add_Score(6)

print(david.first_name)
print(david.last_name)
print(david.team)
print(david.scores)
print(david.get_average_score())
k= david.find_age()
print(f"Age of david: {k}")
print(k<j)

print(f"less than operator overloading: ",david < virat)

print(f"equal to operator overloading: ",virat == david)
