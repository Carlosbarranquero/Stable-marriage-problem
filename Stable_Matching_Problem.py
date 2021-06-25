"""
Name: Stable Matching Problem
Author: Carlos Barranquero Díez
Created on Thu Jun 17 21:32:19 2021

This is my implementation to solve the Stable Matching Problem proposed by David Gale and Lloyd Shapley. 
More information on the problem statement can be found at https://en.wikipedia.org/wiki/Stable_marriage_problem.

Template: 
set_A = {"element_a1":["first_preference_set_b", "second_preference_set_b", ...],
         "element_a2":["first_preference_set_b", "second_preference_set_b", ...],
          ...

set_B = {"element_b1":["first_preference_set_a", "second_preference_set_a", ...],
         "element_b2":["first_preference_set_a", "second_preference_set_a", ...],
          ...
"""


queen_choices = {"Queen_Spades": ["King_Heart", "King_Spades", "King_Diamonds", "King_Clubs"],
                "Queen_Heart": ["King_Heart", "King_Spades", "King_Clubs", "King_Diamonds"],			
                "Queen_Diamonds": ["King_Heart", "King_Diamonds", "King_Spades", "King_Clubs"],		
                "Queen_Clubs": ["King_Heart", "King_Diamonds", "King_Spades", "King_Clubs"]
                }

king_choices = {"King_Spades": ["Queen_Spades", "Queen_Diamonds", "Queen_Heart", "Queen_Clubs"],
                "King_Heart": ["Queen_Diamonds", "Queen_Clubs", "Queen_Spades", "Queen_Heart"],		
                "King_Diamonds": ["Queen_Clubs", "Queen_Heart", "Queen_Diamonds", "Queen_Spades"],				
                "King_Clubs ": ["Queen_Diamonds", "Queen_Heart", "Queen_Spades", "Queen_Clubs"]
                }

stable_choice = {"King_Spades": [], "King_Heart": [], "King_Diamonds": [], "King_Clubs": []}
unstable_choice = {"Queen_Spades": 0, "Queen_Heart": 0, "Queen_Diamonds": 0, "Queen_Clubs": 0}


def perform_kings_choice(king, possible_choise):

    d, x = {}, []

    for elem in possible_choise:

        d[elem] = king_choices[king].index(elem)

    choice_sorted = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}

    [x.append(key) for key in choice_sorted.keys()]
    
    return [x[0]], x[1:]


def perform_queens_choice(stable_choice, refused):

    for ref in refused:

            unstable_choice[ref] += 1

            for queen, all_choises in queen_choices.items():

                if(queen == ref):

                    stable_choice[all_choises[unstable_choice[ref]]].append(queen)

    return stable_choice


def is_not_stable(stable_choice):

    for _, possible_choises in stable_choice.items():

        if(len(possible_choises)>1):

            return True

    return False


#start_algorithm
for queen, all_choises in queen_choices.items():
    
    stable_choice[all_choises[0]].append(queen)

#perform searching
while is_not_stable(stable_choice):

    for king, possible_choises in stable_choice.items():

        if(len(possible_choises) > 1):

            match, refused = perform_kings_choice(king, possible_choises)

            stable_choice[king] = match

            stable_choice = perform_queens_choice(stable_choice, refused)


print("Final Matching:\n", stable_choice)

print("Number of times refused:\n", unstable_choice)

        




        

        












    


    

    
        
        

