import random

color_list=[
    "blue",
    "red",
    "yellow",
    "purple",
    "orange",
    "green",
    "black",
    "white",
]


def combination_counter(multicolor, length, color_count):
    combinations = 0
    if multicolor == "ja":
        combinations = color_count**length

    elif multicolor == "nej":
        combinations = color_count
        for n in range(1, length):
            combinations += combinations*(color_count-n-1)
    return combinations

def difficulty():
    print("Välj svårighetsgrad genom att sätta in önskade parametrar:")
    multicolor_inp = input("Ska färger kunna repeteras? Ja/nej: ").lower()
    color_code_length = int(input("Kodlängd: "))
    while True:    
        color_code_count = int(input("Antal färger: "))
        if color_code_count < color_code_length and multicolor_inp == "nej":
            print("Det måste finnas minst lika många färger som kodlängden är lång")
        else: 
            break
    color_code = generate_color_code(multicolor_inp, color_code_length, color_code_count)
    return color_code

def play_round(player_count):
    '''Här spelas varje runda'''
    player_list = []
    for n in range(1, player_count):
        player = input(f"Namnge spelare {n} : ")
        player_list.append(player)
   
    return player_list

def generate_color_code(multicolor, length, color_count):

    color_code = []
    if multicolor == "nej":
        for colors in range(length):
            c = random.sample(color_list, k=colors+1) #Sample tar ut ett unikt element ur listan
            print(c)
            color_code.append(c)
    else: 
        for color in range(length):
            c = random.choice(color_list[0:color_count])
            color_code.append(c)
            print(color_code)
    
    return color_code

def guess_check(guess_list, difficulty):
    answer_clues = []
    for color in range(difficulty):
        if guess_list == color_code:
            return 1
        elif guess_list[color] == color_code[color]:
            
            answer_clues.append("röd pigg")

        elif guess_list[color] in color_code:
           

            answer_clues.append("vit pigg") 

    random.shuffle(answer_clues)

    return answer_clues


while True:
    for guesses in range(12):
        color_code = difficulty()
        
        print(f"Du har {12-guesses} gissningar kvar. ")
        print(f"Ps. Koden är {color_code}.")
        guess_raw = input((f"Gissa {len(color_code)} färger eller skriv \"omstart\" om du vill starta om eller \"avsluta\" om du vill avsluta: ")).lower()

        if guess_raw =="kod":
            print(color_code)
        elif guess_raw == "avsluta":
            exit()
        elif guess_raw == "omstart":
            break
        else:
            guess_list = guess_raw.split()
            result = guess_check(guess_list, difficulty)
            if result == 1:
                print(f"Du vann med {guesses+1} gissningar!")
                break
            elif guesses == 12:
                print("Game over!")
                break
            else:
                print(result)