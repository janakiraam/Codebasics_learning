import datetime

def get_average_Score(player):
    return sum(player['scores'])/len(player['scores'])
def get_Age(player):
    current_year = datetime.datetime.now().year
    return current_year - player['birth_date']
virat = {
    'first_name' : 'virat',
    'last_name' : 'kohil',
    'scores': [],
    'birth_date' : 1988
}

virat['scores'].append(80)
virat['scores'].append(100)
virat['scores'].append(0)

print (virat['scores'])

print(get_average_Score(virat))
print(get_Age(virat))

#for another player we need to define the dictionary again
