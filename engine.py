import os

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
        tall = input("Skriv et tall (1 for å lese tekst, 2 for å telle ord, 3 for å søke ord, 4 for å vite om ordet fins, 5 for å se alle linjene ordet er i, exit to exit): ")
        if tall == "exit":
            print("Avslutter programmet.")
            break
        menyvalg(tall, content)

def menyvalg(valgtTall, content):
    """Handles menu choices based on input."""
    os.system('cls' if os.name == 'nt' else 'clear')

    if valgtTall == "1": # Starts the printTekst Function
        printTekst(content)
    elif valgtTall == "2": # Starts the tellOrd Function
        tellOrd()
    elif valgtTall == "3": # Starts the printOrd Function
        printOrd(content)
    elif valgtTall =="4": # Starts the finnOrd Function
        finnOrd(content)
    elif valgtTall =="5": # Starts the finnLinje Function
        finnLinje(content)
    else:
        print("Ugyldig valg. Prøv igjen.")

def count_word_in_file(filename, word):
    try:
        with open(filename, "r", encoding="utf-8") as f:  # Opens the file and changes encoding to utf-8 to compansate for Norwegian
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
    """Prompts the user for a word to count in a file."""
    filename = "tekstfil3.txt"
    search_word = input("Hvilket ord vil du søke etter? ")
    count = count_word_in_file(filename, search_word)
    print(f"Ordet '{search_word}' ble funnet {count} gang(er) i filen.")

def printOrd(content):
    """Searches for a word in the content."""
    Pord = input("Hvilket ord er du etter?: ").lower()  # Convert input to lowercase
    words = content.lower().split()  # Normalize content to lowercase and split into words
    cleaned_words = [w.strip(".,!?;:\"'()[]{}") for w in words]  # Clean punctuation
    if Pord in cleaned_words:
        print(Pord)
    else:
        print("Fant ikke ordet i teksten.")

def finnOrd(content):
    """Checks if a word exists in the content."""
    tfOrd = input("Hvilket ord vil du vite om fins?: ").lower()  # Convert input to lowercase
    words = content.lower().split()  # Normalize content to lowercase and split into words
    cleaned_words = [w.strip(".,!?;:\"'()[]{}") for w in words]  # Clean punctuation
    if tfOrd in cleaned_words:  # Check for whole word
        print("true")
    else:
        print("false")

def finnLinje(content):

    """Prints lines containing the specified word."""
    lOrd = input("Hvilket ord vil du se linjen til?: ").lower()  # Convert input to lowercase
    lines = content.splitlines()  # Split content into lines
    linjeNr = 0 # Set current line number to 0

    for line in lines:
        linjeNr += 1 # Add 1 to linjeNr for each line
        words = line.lower().split()  # Normalize line to lowercase and split into words
        cleaned_words = [w.strip(".,!?;:\"'()[]{}") for w in words]  # Clean punctuation
        
        if lOrd in cleaned_words:  # Check for the word in the cleaned words for this line
            print("Ln", linjeNr, line)  # Print the entire line with current line number




# Main Program Execution
filename = "tekstfil3.txt"
try:
    file_content = lesInnTekst(filename)
    tallvelger(file_content)
except FileNotFoundError:
    print(f"Filen '{filename}' ble ikke funnet.")
