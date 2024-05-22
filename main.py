morse_code_dict = {"a" : ".-",
                "b" : "-...",
                "c" : "-.-.",
                "d" : "-..",
                "e" : ".",
                "f" : "..-.",
                "g" : "--.",
                "h" : "....",
                "i" : "..",
                "j" : ".---",
                "k" : "-.-",
                "l" : ".-..",
                "m" : "--",
                "n" : "-.",
                "o" : "---",
                "p" : ".--.",
                "q" : "--.-",
                "r" : ".-.",
                "s" : "...",
                "t" : "-",
                "u" : "..-",
                "v" : "...-",
                "w" : ".--",
                "x" : "-..-",
                "y" : "-.--",
                "z" : "--..",
                "1" : ".----",
                "2" : "..---",
                "3" : "...--",
                "4" : "....-",
                "5" : ".....",
                "6" : "-....",
                "7" : "--...",
                "8" : "---..",
                "9" : "----.",
                "0" : "-----",
                " " : " "}

is_on = True
while is_on:
    message = input('Enter a message to be converted to morse code (only letters and numbers): ').lower()
    if message != '$':
        message_in_morse = []
        space_between_letters = '   '
        for i in message:
            try:
                morse_letter = morse_code_dict[i]
                message_in_morse.append(morse_letter)
            except KeyError:
                print(f"{i} is not in the morse code dictionary")

        joint = "   ".join(message_in_morse)
        print(joint)
        print('Enter $ to exit')
    else:
        is_on = False
