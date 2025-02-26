import random

pokemon_iniciales = {
    "Generación I": ["Bulbasaur", "Charmander", "Squirtle"],
    "Generación II": ["Chikorita", "Cyndaquil", "Totodile"],
    "Generación III": ["Treecko", "Torchic", "Mudkip"],
    "Generación IV": ["Turtwig", "Chimchar", "Piplup"],
    "Generación V": ["Snivy", "Tepig", "Oshawott"],
    "Generación VI": ["Chespin", "Fennekin", "Froakie"],
    "Generación VII": ["Rowlet", "Litten", "Popplio"],
    "Generación VIII": ["Grookey", "Scorbunny", "Sobble"],
    "Generación IX": ["Sprigatito", "Fuecoco", "Quaxly"]
}

# Convertir todos los Pokémon iniciales en una lista plana
todos_pokemon = sum(pokemon_iniciales.values(), [])

# Seleccionar un Pokémon aleatorio
pokemon_aleatorio = random.choice(todos_pokemon)

print(f"¡Tu Pokémon inicial aleatorio es: {pokemon_aleatorio}!")
