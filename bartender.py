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

for question in questions:
    print(questions[question])