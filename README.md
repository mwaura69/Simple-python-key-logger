import pynput
plus = ""

def order(letters):
    global plus



    try:
        plus+= str(letters.char)


    except AttributeError:
        if letters == letters.space:
            plus += " "


        elif letters == letters.backspace:
            number = len(plus)
            number -= 1
            value = 0
            equal = ""

            while number > value:
                equal += plus[value]
                value += 1
            plus = equal

        elif letters == letters.enter:
            plus += "\n"

        else:

            plus += str(letters)
        print(plus)

Listening = pynput.keyboard.Listener(on_press=order)
Listening = pynput.mouse.Listener(on_press=order)

with Listening:
    Listening.join()
    
