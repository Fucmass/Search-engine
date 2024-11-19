def lesInnTekst(filename):
    """Reads and returns the content of a file."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def printTekst(content):
    """Prints the text content provided."""
    print(content)

def tallvelger(content):
    """Allows the user to choose an option in a loop."""
    while True:
        tall = input("Skriv et tall (1 for å lese tekst, 2 for annet, exit to exit): ")
        if tall == "exit":
            print("Avslutter programmet.")
            break
        menyvalg(tall, content)

def menyvalg(valgtTall, content):
    """Handles menu choices based on input."""
    if valgtTall == "1":
        printTekst(content)
    elif valgtTall == "2":
        tellOrd()
    else:
        print("Ugyldig valg. Prøv igjen.")
def count_word_in_file(filename, word):
    try:
        with open(filename, "r") as f:
            content = f.read().lower()  # Read the file and convert to lowercase
            word = word.lower()  # Ensure the word match is case-insensitive
            
            # Clean up the content to only consider whole words
            words = content.split()  # Split the text into individual words
            cleaned_words = [w.strip(".,!?;:\"'()[]{}") for w in words]  # Remove punctuation
            return cleaned_words.count(word)
    except FileNotFoundError:
        print(f"Filen '{filename}' ble ikke funnet.")
        return 0

def tellOrd():
    filename = "tekstfil3.txt"
    search_word = input("Hvilket ord vil du søke etter? ")
    count = count_word_in_file(filename, search_word)
    print(f"Ordet '{search_word}' ble funnet {count} gang(er) i filen.")


# Main Program Execution
filename = "tekstfil3.txt"
try:
    file_content = lesInnTekst(filename)
    tallvelger(file_content)
except FileNotFoundError:
    print(f"Filen '{filename}' ble ikke funnet.")
