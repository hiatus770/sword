# ███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗ #
# ██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗#
# ███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║#
# ╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║#
# ███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝#
# ╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ #

# pair for positioning or count #
optimal = []
misplaced = []
lc = {}
letters = set()

# Holds all the possible words in wordle #
words = []

# Alphabet #
alpha = "abcdefghijklmnopqrstuvwxyz"
for i in alpha:
    # setting all the letters to 0 initially 
    lc[i] = 0

# vars #
txtDir = "wordle-answers-alphabetical.txt"

# Load all the words into the array #
def initiate():
    print("<INITIATING>")
    with open(txtDir, "r") as txt:
        for i in txt.readlines():
            words.append(i.replace("\n", ""))
    words.sort() 
    print("<DONE UPDATING WORDS>")

def narrow(optimal, misplaced, lc):
    global letters; global words; 
    print("NARROWING DOWN LIST")
    newList = [] 
    for word in words: 
        # Check for the positioning # 
        append = False;
        
        for i in range(5):
            letter = word[i]; 
            for pair in optimal:
                if pair[1] == i and pair[0] == letter:
                    print("HERE")    
                    append = True 
                elif pair[1] == i and pair[0] != letter: 
                    append = False
                if append == False:
                    break; 
            if append == False:
                break; 

        if append: 
            print("APPENDING", word)
            newList.append(word)

    words = newList 


def updateList():
    print("UPDATING LIST")
    word = input().lower() 
    pos = input().lower()

    for i in word:
        lc[i] = lc[i]+1
        letters.add(i) # keep track of letters with data assigned to them 

    for i in range(5):
        if pos[i] == "g":
            # Optimal Placement #
            optimal.append([word[i], i])
        elif pos[i] == "y":
            # Misplacement #
            misplaced.append([word[i], i])
        elif pos[i] == "b":
            # Not in the word or count of misplacement #
            lc[word[i]] = lc[word[i]]-1
            

    print("Letter Counts", lc)
    print("Optimals", optimal)
    print("Misplaced", misplaced)
    print("Letters with Data", letters)
    
    # Narrows down the choice of words with the given information # 
    narrow(optimal, misplaced, lc)
    print(words)
    

initiate()
updateList()