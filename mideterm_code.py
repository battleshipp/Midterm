from textblob import TextBlob, Word
# The TextBlob class and its subsequent subclasses are used for basic text
# processing operations (Natural Language Processing)
# TextBlob objects are similar to strings but with more language processing methods
# The title method changes the first letter of each word to upper case if it is not already
# This code asks a user for their address information, puts each value into a dictionary of textblobs,
# and makes sure they are all in title case, as they should be on a shipping label
address_info = {}
keys = ["street", "city", "state", "country"]
# Create locations as a list of the values in the dictionary
locations = []
street_address = TextBlob(input("Please enter your street name and number"))
locations.append(street_address)
city_name = TextBlob(input("Please enter the name of your city"))
locations.append(city_name)
state_name = TextBlob(input("Please enter the name of your state"))
locations.append(state_name)
country_name = TextBlob(input("Please enter the name of your country"))
locations.append(country_name)
counter = 0
for key_value in keys:
    address_info[keys[counter]] = locations[counter].title()
    counter += 1
print(f"Your shipping address is {address_info.values()}")

# This code takes in full names in the form of TextBlobs, and makes sure they are capitalized
# This code creates a list of dictionaries in order to store the names
list_of_names = []
while True:
    first_name = TextBlob(input("Please enter your first name , or q to finish"))
    firstn = first_name.title()
    if first_name == 'q':
        break
    last_name = TextBlob(input("Please enter your last name, or q to finish"))
    lastn = last_name.title()
    if last_name == 'q':
        break
    dictionary_names = {firstn : lastn}
    list_of_names.append(dictionary_names)
for name in list_of_names:
    print(name)
# The correct method returns corrections to the given text
# This code checks the given text for corrections,
# asks the user to try again if it has errors, and gives an option to see the corrections
# This is useful for writing anything that requires correct spelling
while True:
    blob_to_correct = TextBlob(input("Enter some english text"))
    corrected_blob = blob_to_correct.correct()
    if blob_to_correct != corrected_blob:
        blob_to_correct = TextBlob(input("There are errors in your text Please try again, or enter A to see the correction"))
        if blob_to_correct == 'A':
             print(f"The corrected text looks like: {corrected_blob}")
             break
        elif blob_to_correct == blob_to_correct.correct():
            print("The text you entered does not have any errors")
            break
        else:
            continue
    else:
        print("The text you entered does not have any errors")
        break

# This code can be used to proof read an essay, checking the title for proper case
# As well as proper spelling in both the title and the following text
# This is done using the title method and the correct method
title_blob = TextBlob(input('Please enter the essay title'))
if title_blob != title_blob.correct():
    title_blob = title_blob.correct()
    print(f"Your title had spelling errors, it should look like this: {title_blob}")
if title_blob != title_blob.title():
    print(f"Your title is in the wrong case and should be changed to: {title_blob.title()}")
else:
    print("That title looks good!")
while True:
    first_blob = TextBlob(input('Please begin writing the assignment, or enter q to exit'))
    if first_blob == 'q':
        break
    if first_blob != first_blob.correct():
     print(f"You text should be changed to {first_blob.correct()}")
    else:
     print("The entered text does not contain errors")

# Subjectivity method analyzes the subjectivity of a phrase on a scale of 0-1,
# 0 being objective and 1 being subjective
# Ask the user to enter multiple sentences of text
blob_to_analyze = TextBlob(input('Enter multiple sentences of text'))
counter = 0
# The sentences method returns a list of sentence objects
# This loop analyzes each individual sentence for subjectivity
for b in blob_to_analyze.sentences:
    counter += 1
    print(f"The subjectivity of sentence number {counter} on a scale of 0 to 1 is {b.subjectivity}")


# This code is used to determine whether or not a given sentence is objective
# This is useful for writing an assignment that requires objective points
next_blob = TextBlob(input('Enter an objective phrase'))
while True:
    if next_blob.subjectivity > 0:
        next_blob = TextBlob(input("The phrase you entered is somewhat subjective. Please reword it"))
    else:
        print(
            f"The phrase you entered: {next_blob}, is objective, and better suited for this type of writing assignment")
        break


# This code will ask the user for the degree of subjectivity they are expected to be writing with for a given assignment
# This code will then check the entered sentence for subjectivity, and let the user know if his or her
# writing is in line with the requiremenmt
desired_subjectiveness = float(input("please enter the required maximum degree of subjectivity for this assignment in the form of a percentage"))
while True:
    sub_blob = TextBlob(input("Please enter the phrase"))
    if desired_subjectiveness < sub_blob.subjectivity:
     print(f"The subjectivity of the entered text is {sub_blob.subjectivity}, and is too subjective for this assignment. Please try again")
    else:
        print(f"The subjectivity of the entered phrase is {sub_blob.subjectivity}, and is objective enough for this assignment")
        break


# The word_counts method returns a dictionary of word frequencies in the text
# The replace method replaces the first instance of a word with another given word
# The find method finds the first instance of a word in the text
blob_to_change = TextBlob(input('Enter a sentence to edit: '))
list_of_words = blob_to_change.word_counts
# This code identifies duplicate words in a sentence and allows users to choose
# a replacement word for the first instance of the duplicate, and then corrects any other errors
# This code is useful for anyone trying to write clean, well-written sentences
for words in list_of_words:
    print(f"The word {words} appears {list_of_words.get(words)} time(s)")
    if list_of_words.get(words) > 1:
        print(f"The word {words} appears more than once in the same sentence, consider using a synonym")
        word_location = blob_to_change.find(words, 0, blob_to_change.__len__())
        replacement: str = input(f"Enter a word to replace the first instance of the duplicate at location {word_location}")
        new_blob = (blob_to_change.replace(words, replacement, 1))
        print(new_blob.__str__())





# Imported from textblob, word is a subclass with methods used to analyze text
# This code uses methods from textblob.blob.word to check if a string
# is alphanumeric, numeric, uppercase, or lowercase, or both
word_to_check = Word(input('Enter text'))
if word_to_check.isnumeric() == True:
    print("The text entered represents a numeric value")
elif word_to_check.isspace() == True:
    print("The given text is just white space")
elif word_to_check.isalpha() == True:
    if word_to_check.islower() == True:
        print(f"The entered text is alphabetic and consists of only lowercase letters. In uppercase, the text would look like this: {word_to_check.upper()}")
    elif word_to_check.isupper() == True:
        print(f"The entered text is alphabetic and consists of only uppercase letters. In lowercase, the text would look like this: {word_to_check.lower()}")
    else:
        print("The entered text is alphabetic and consists of both lower and uppercase letters")



