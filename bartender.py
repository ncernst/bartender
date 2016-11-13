# random.choice(ingredients[question])
import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong" : ["glug of run", "slug of whiskey", "splash of gin"],
    "salty" : ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter" : ["shake of bitters", "splash of tonic", "twist of lemon"],
    "sweet" : ["sugar cube", "spoonful of honey", "splash of cola"],
    "fruity" : ["slice of orange", "dash of cassis", "cherry on top"],
}

drink_name = {
    "adjective" : ["Fluffy ", "Twirling ", "Dropping ", "Blank ", "Tropical ", "Infused ", "Winged "],
    "noun" : ["Sea-dog", "Monkey", "Frigate", "Buccaneer", "Pirate", "Grog", "Barque", "Brig", "Lass"],
}

drink = {}

customers = {}

def preference_questions():
    for question in questions:
        print(questions[question])
        response = input(">>>")
        
        if response.upper() == "Y" or response.upper() == "YES":
            drink[question] = True
        else:
            drink[question] = False

def make_drink(name):
    print("Yarr, let's fix ye up something...")
    
    for preference in drink:
        if drink[preference] == True:
            print("* Adds a " + str(random.choice(ingredients[preference])) + " *")
    
    your_drink = str(random.choice(drink_name["adjective"])) + str(random.choice(drink_name["noun"]))
    customers[name] = your_drink
    print("Here's yer " + your_drink +". Drink up!")


def tab(name):
    if name == None:
        print("Lemme open ye up a tab. What's yer name, matey?")
        name = input(">>> ")
        return name
    elif name in customers:
        print("Another of the same?")
        another_round = input(">>> ")
        
        if another_round.upper() == "Y" or another_round.upper() == "YES":
            print("Very well, another " + customers[name] +". Drink up!")
        
        else:
            preference_questions()
            make_drink(name)   
    else:
        print("It's yer lucky day, I can't find yer tab. We'll start a new one for ye.")
        preference_questions()
        make_drink(name) 
            
def welcome():
    print("Fancy a drink?")
    thirsty_response = input(">>> ")
    

    
    if thirsty_response.upper() != "Y" and thirsty_response.upper() != "YES":
        print("Then ye best be shoving off.")
        exit()
    else:
        name = tab(None)
        preference_questions()
        make_drink(name)


def another():
    print("Thirsty?")
    another_response = input(">>> ")
    
    if another_response.upper() == "Y" or another_response.upper() == "YES":
        print("Do ye have a tab?")
        tab_response = input(">>> ")
        
        if tab_response.upper() == "Y" or tab_response.upper() == "YES":
            print("What's the name?")
            name = input(">>> ")
            
            tab(name)

            
        else:
            name = tab(None)
            preference_questions()
            make_drink(name)
    else:
        print("Best be paying yer tab then matey.")
        exit()


if __name__ == '__main__':
    welcome()
    while True:
        another()
