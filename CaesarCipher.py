from CaesarArt import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction== "encode":
        for letter in start_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                if new_position > 25:
                    new_position = new_position - 26
                end_text += alphabet[new_position]
            else:
                end_text += letter
        print(f"The {cipher_direction}d text is: {end_text}")
        
    elif direction == "decode":
        for letter in start_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position - shift_amount
                if new_position < 0:
                    new_position = new_position + 26
                end_text += alphabet[new_position]
            else:
                end_text += letter
        print(f"The {cipher_direction}d text is: {end_text}")
    else:
        print("Please type 'encode' or 'decode'!")
        
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    caesar(start_text = text, shift_amount = shift, cipher_direction = direction)
        
        
    restart = input("Do you want to restart? (yes/no)\n")
    if restart == "n":
        should_continue = False
        print("Goodbye!")
        exit()
        