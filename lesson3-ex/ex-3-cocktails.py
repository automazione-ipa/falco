cocktails = {
    "margarita": {
        "ingredients": ["Tequila 50ml", "Triple sec 20ml", "Lime juice 20ml", "Salt for the rim of the glass"]
    },
    "mojito": {
        "ingredients": ["White rum 50ml", "Lime juice 30ml", "Brown sugar 2 teaspoons", "Fresh mint", "Soda", "Crushed ice"]
    },
    "negroni": {
        "ingredients": ["Gin 30ml", "Red vermouth 30ml", "Campari bitter 30ml", "Ice", "Orange peel"]
    },
    "old fashioned": {
        "ingredients": ["Bourbon 50ml", "Sugar cube", "Angostura 2 drops", "Splash of soda", "Orange peel", "Ice"]
    },
    "daiquiri": {
        "ingredients": ["White rum 50ml", "Lime juice 25ml", "Sugar syrup 15ml", "Ice"]
    }
}

print('Which cocktail you want to prepare?')
cocktail = input()
if cocktail.lower() in cocktails:
    print("Here is your cocktail: " + str(cocktail))
    for ingredient in cocktails[str(cocktail)]["ingredients"]:
        print("- " + ingredient)
else:
    print("Cocktail not found.")
