import sys

# Biblioteca de caracteres
tableau = [["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],
           ["B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A"],
           ["C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B"],
           ["D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C"],
           ["E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D"],
           ["F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E"],
           ["G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F"],
           ["H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G"],
           ["I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H"],
           ["J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I"],
           ["K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J"],
           ["L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K"],
           ["M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L"],
           ["N","O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M"],
           ["O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N"],
           ["P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"],
           ["Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"],
           ["R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q"],
           ["S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R"],
           ["T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S"],
           ["U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"],
           ["V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U"],
           ["W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V"],
           ["X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W"],
           ["Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X"],
           ["Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y"]]

vocabulary = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def vigenere_encrypt(key,parameter_t, text):
    encrypted_text=[]
    key = key.upper()
    text = text.replace(" ","").upper()
    if len(text) % parameter_t != 0:
        num_x_to_add = parameter_t - (len(text) % parameter_t)
        text += 'X' * num_x_to_add
    text_length = len(text)
    extended_key = (key * (text_length // len(key))) + key[:text_length % len(key)]

    for i in range(0, len(text)):
        key_code = vocabulary.index(extended_key[i])
        text_code = vocabulary.index(text[i])
        encrypted_text.append(tableau[key_code][text_code])
    encrypted_text = "".join(encrypted_text)
    eText_blocks = [list(encrypted_text[i:i+parameter_t]) for i in range(0, len(encrypted_text), parameter_t)]
    eText_blocks = ["".join(block) for block in eText_blocks]

    return " ".join(eText_blocks)

def vigenere_decrypt(key,parameter_t, text):
    decrypted_text=[]
    key = key.upper()
    text = text.replace(" ","").upper()
    if len(text) % parameter_t != 0:
        num_x_to_add = parameter_t - (len(text) % parameter_t)
        text += 'X' * num_x_to_add
    text_length = len(text)
    extended_key = (key * (text_length // len(key))) + key[:text_length % len(key)]
    for i in range(0, len(text)):
        key_code = vocabulary.index(extended_key[i])
        text_code = tableau[key_code].index(text[i])
        decrypted_text.append(vocabulary[text_code])
    decrypted_text = "".join(decrypted_text)
    eText_blocks = [list(decrypted_text[i:i+parameter_t]) for i in range(0, len(decrypted_text), parameter_t)]
    eText_blocks = ["".join(block) for block in eText_blocks]

    return " ".join(eText_blocks)


def main():
    if len(sys.argv) < 5:
        print("Uso: python vigenere.py [modo] [clave] [parametro_t] [mensaje]")
        print("modo: encrypt o decrypt")
        sys.exit(1)

    mode = sys.argv[1].lower()
    key = sys.argv[2]
    parameter_t = int(sys.argv[3])
    text = ' '.join(sys.argv[4:])

    if mode == 'encrypt':
        result = vigenere_encrypt(key, parameter_t, text)
        print(f"Texto cifrado: {result}")

    elif mode == 'decrypt':
        result = vigenere_decrypt(key, parameter_t, text)
        print(f"Texto descifrado: {result}")

    else:
        print("Modo no válido. Usa 'encrypt' o 'decrypt'.")
        sys.exit(1)


if __name__ == "__main__":
    main()