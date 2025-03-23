import random

jokes = [
    "Why do programmers prefer dark mode? Because the light attracts bugs!",
    "Why did the Python programmer break up with their partner? They kept making exceptions.",
    "Why was the JavaScript developer sad? Because they didn’t know how to ‘null’ their feelings.",
    "Why don’t programmers like nature? It has too many bugs.",
    "Why did the developer go broke? Because they used up all their cache.",
    "How do you comfort a JavaScript bug? You console it.",
    "Why was the Python function so good at socializing? It had great arguments!",
    "What’s a programmer’s favorite hangout place? The ‘while’ loop.",
    "Why do programmers hate climbing? Because they’re always getting stuck in loops.",
    "Why don’t skeletons ever fight each other? They don’t have the guts... just like some programmers!"
]

def display_joke():
    random_joke = random.choice(jokes)  
    print(f"\nHere's a programming joke for you:\n{random_joke}\n")

def main():
    print("Welcome to the Random Joke Generator!")
    input("Press Enter to hear a joke...\n")
    display_joke()

if __name__ == "__main__":
    main()
