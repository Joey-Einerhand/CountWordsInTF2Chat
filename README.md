# CountWordsInTF2Chat
Counts the words which have been said in your Team Fortress 2 chat history.

# How does it work?
Preface: If you wish to simply test the program without setting up Team Fortress 2, I've attached a demo file to the release so you can test out the script without installing TF2 yourself.

This python script filters the console output of the videogame Team Fortress 2 and counts which words have been said in your chat history.
The Team Fortress 2 chat is received through the in-game console. This console can save itself to a file, but doesn't do this by default.
To enable this, add "con_logfile tf2consoleoutput.log" to your [autoexec file](https://www.youtube.com/watch?v=1aT7kFj7ZGI)
This tells the in-game console to save itself to the tf2consoleoutput.log file every time it is updated. The file can be found in your Team Fortress 2\tf folder, usually located in `C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2\tf` on windows.
I've also attached an example console output file if you wish to test the application first.
The program expects this file to be in the same directory as the script (by default), so copy over the tf2consoleoutput.log file to the location of the script.

Executing the script at this point will filter and count the words in each chat message.

# Step by step instructions:
1. Install [python](https://www.python.org/downloads/). This file was made with 3.7, but anything 3.x should work. 2.x hasn't been tested.
2. Add "con_logfile tf2consoleoutput.log" to your [autoexec file](https://www.youtube.com/watch?v=1aT7kFj7ZGI)
3. From this point forward, chat messages will probably be saved to `C:\Program Files (x86)\Steam\steamapps\common\Team Fortress 2\tf\tf2consoleoutput.log`  
4. Copy this file to the same location as the CountWordsInTF2Chat.py script.
5. Run the script by double-clicking CountWordsInTF2Chat.py. This should work if you've installed Python correctly.

Alternatively, run [the file via command prompt](https://www.wikihow.com/Use-Windows-Command-Prompt-to-Run-a-Python-File) and add one of the following arguments:
-h or -help : Shows all available arguments
-filter <filename> / -f <filename>: Filter specified console file for chat messages and create a new file containing them. Does not change the original file.
-count <filename> / -c <filename>: Count the words in the specified file. File should be a filtered version of tf2\'s output console file.
