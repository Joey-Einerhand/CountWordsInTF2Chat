from operator import truediv
import re
import sys
import pathlib

defaultUnfilteredConsoleFileName = 'tf2consoleoutput.log'
defaultFilteredFileName = 'filteredConsoleFile.txt'

#Assumes the file exists. This should be checked prior to calling this method.
def filterConsoleFile(fileName = defaultUnfilteredConsoleFileName):
    unfilteredConsoleFile = open(fileName)

    # Filtered log file filled in through this script. Creates new if doesnt exist, always overwrites
    filteredConsoleFile = open(defaultFilteredFileName, 'w+', encoding="ISO-8859-1")

    print("Filtering. This might take a while.")
    # Matches any string with a ' :'. After the ' :', needs to have at least one non-whitespace character.Stops at a line break.
    regexForNonEmptySpeech = '.*( :)+.*[^\s]+'

    # Checks if a line is an in-game error line by checking if it starts with "Error:".
    # The nature of the previous regex and error lines in the TF2's output file results in error lines sometimes being picked up
    # by the previous regex, because there might be a " :" in an error message. This filters those out.
    # For example: "Error: Material "models/weapons/c_models/c_ubersaw/c_ubersaw" : proxy "AnimatedWeaponSheen" unable to initialize!" will no longer be picked up.
    # Has the unfortunate side effect of also filtering out messages from usernames which start with "Error: "
    regexForTF2ErrorMessage = '^Error:'

    for line in unfilteredConsoleFile:
        # Only write line to filtered file if it's a non-empty chat message
        nonEmptySpeechLine = re.match(regexForNonEmptySpeech, line)
        if (nonEmptySpeechLine != None):
            # Make sure to filter out the message if it's an assumed error message
            errorMessage = re.match(regexForTF2ErrorMessage, nonEmptySpeechLine[0])
            if (errorMessage == None):
                filteredConsoleFile.write(nonEmptySpeechLine[0] + "\n")

    unfilteredConsoleFile.close()
    filteredConsoleFile.close()
    print('Filtering complete! Saved filtered file as "{}"'.format(defaultFilteredFileName))

def countSpecificWordsInFile(fileName = defaultFilteredFileName):
    filteredConsoleFile = open(fileName, 'r', encoding="ISO-8859-1")
    # Dictionary. Keys are the words, values are the count of that word.
    # So to get the total count of the word "Hello", check the value of wordCount[Hello]
    wordCount = {}
    # Each chatMessage is one line.
    for chatMessage in filteredConsoleFile:
        words = chatMessage.split()
        for word in words:
            # Check if the word (as a key) exist in the dict. If it does not exist, create it with a value of 0, and add 1.
            # If it does exist, get the existing value and add 1.
            wordCount[word] = wordCount.get(word, 0) + 1
    sortedWordCount = {}
    sortedKeys = sorted(wordCount, key=wordCount.get)

    for word in sortedKeys:
        sortedWordCount[word] = wordCount[word]
    
    for word in sortedKeys:
        if sortedWordCount[word] > 1:
            print(word +  " : " + str(sortedWordCount[word]))
    print("")
    print("Counting has finished.")

def getInputFile():
    while (True):
        print('Could not find the specified file.')
        print('Please type the name of the file (including file extention) in this console.')
        print('If you wish to cancel, press control + c at the same time.')
        filteredConsoleFileName = input()
        if (checkFileExists(filteredConsoleFileName)):
            return filteredConsoleFileName

def checkFileExists(pathToFile):
    fileToCheck = pathlib.Path(pathToFile)
    fileExists = fileToCheck.exists()
    return fileExists


def main():
    if (len(sys.argv) > 1):
        if (sys.argv[2] != None):
            userSpecifiedFile = sys.argv[2]
            # -filter means the user wants to filter their log file which was output by TF2's system.
            if (sys.argv[1] == "-filter" or sys.argv[1] == "-Filter" or sys.argv[1] == "-f" or sys.argv[1] == "-F"):
                # Check if input file name is correct. Only moves to the FilterConsoleFile function if file can be found
                if not (checkFileExists(userSpecifiedFile)):
                    # asks for file from user until it is found
                    print('Could not find the unfiltered console file.')
                    userSpecifiedFile = getInputFile()
                filterConsoleFile(userSpecifiedFile)
                input()
                quit()

            if (sys.argv[1] == "-count" or sys.argv[1] == "-Count" or sys.argv[1] == "-c" or sys.argv[1] == "-C"):
                # Check if input file name is correct. Only moves to the FilterConsoleFile function if file can be found
                if not (checkFileExists(userSpecifiedFile)):
                    # asks for file from user until it is found
                    print('Could not find the filtered console file.')
                    userSpecifiedFile = getInputFile()
                countSpecificWordsInFile(userSpecifiedFile)
                input()
                quit()

            # -visualise means the user wants to visualise the data from the filtered file.
            # This method doesn't check if it actually is the filtered file. This is the user's responibility.
            #TODO
        elif (sys.argv[1] == "-h" or sys.argv[1] == "-H" or sys.argv[1] == "-help" or sys.argv[1] == "-Help"):
            print('')
            print('Help menu requested. Available arguments:')
            print('-filter <filename> / -f <filename>: Filter specified console file for chat messages and create a new file containing them. Does not change the original file.')
            print('-count <filename> / -c <filename>: Count the words in the specified file. File should be a filtered version of tf2\'s output console file.')
            print('All filenames should include their file extentions.')
        else:
            print('invalid arguments detected. Type -help to display all available arguments.')
            print('Did you forget to state a filename after an argument?')
            print('For example: "consolehandler.py -filter tf2consoleoutput.log"')
            input()
            quit()
    # If no parameters are filled in, check if filtered or unfiltered files (default names) are present. If not, ask for input
    # Makes it so you don't have to fill in parameters per se, saves time if showing script
    else:
        print('No arguments given. Continuing with default values.')
        print('If this is not desired, execute the file with -filter <unfiltered filename> or -count <filtered filename> arguments without <>.')
        print('Checking if default filtered file exists.')
        if (checkFileExists(defaultFilteredFileName)):
            print('Default filtered file found- counting words')
            countSpecificWordsInFile()
            input()
            quit()
        else:
            print('Default filtered file not found. Checking for default unfiltered file..')
            if (checkFileExists(defaultUnfilteredConsoleFileName)):
                print('Default unfiltered file found. Continuing to filter this file.')
                filterConsoleFile()
                print('Finished filtering console file. Counting words..') 
                countSpecificWordsInFile()
                input()
                quit()
            else:
                print('Could not find default unfiltered console file. Please transfer the console file to this program\'s folder.')
                print('Alternatively, launch this program with the -filter or -count arguments.')
                input()
                quit()





if __name__ == "__main__":
    main()


