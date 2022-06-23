'''
Peter Yu
6/15/2022
'''

# men preferences
men_preferences = {
    'A': ['c', 'b', 'd', 'a'],
    'B': ['b', 'a', 'c', 'd'],
    'C': ['b', 'd', 'a', 'c'],
    'D': ['c', 'a', 'd', 'b']
}

# woman preferences
women_preferences = {
    'a': ['A', 'B', 'D', 'C'],
    'b': ['C', 'A', 'D', 'B'],
    'c': ['C', 'B', 'D', 'A'],
    'd': ['B', 'A', 'C', 'D']
}

# possible engagments
possible_engagements = []

# Avaliable men
free_men = []

# Initial: Add all men to the men that are free to the free_men list
for man in men_preferences.keys():
    free_men.append(man)

def start_match(man):
#   getting woman values for integer man
    for woman in men_preferences[man]:

        # Get woman and man - matches
        taken_match = [matching for matching in possible_engagements if woman in matching]

        # If match has not happened, then append the new match        
        if(len(taken_match) == 0):
            # Add the new matching        
            possible_engagements.append([man, woman])
            
            # Remove the man from the free_men list            
            free_men.remove(man)
            break
        
        # The woman is already matched; however, we can still see if the man is prefered 
        elif(len(taken_match) > 0):
            
            # Current man the women is with
            # Important: we are taking the index of the woman's prefered man         
            current_man = women_preferences[woman].index(taken_match[0][0])
            
            # potential man that can replace current man index             
            potential_man = women_preferences[woman].index(man)

            # If the potential man is higher ranked that the current man (Lower Index)           
            if(current_man > potential_man):
                # The potential man is better than the current man the woman has
                # Thus, he is the new man
                
                # Remove man from the free_men list           
                free_men.remove(man)

                # Add the old man back into the free_men list            
                free_men.append(taken_match[0][0])

                # Potential man takes the spot of the previous man                 
                taken_match[0][0] = man
                break
                
# If free_men list is greater than 0, then keep on matching men
# man is an integer
while(len(free_men) > 0):
    for man in free_men:
        start_match(man)

print('STABLE MATCHING:')
print(possible_engagements)

# For this data set, we will get [['D', 'c'], ['C', 'b'], ['B', 'a'], ['A', 'd']]

# ---Important notes---
# Dataset is organized in a dictionary where it is the 'individual': [preference_list]
# taken_match is a 2D list, so we have to have taken_match[0][0] for a specific index
