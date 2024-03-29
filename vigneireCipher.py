def generateKey(string, keyword):

    newKeyword = ""
    count = 0
       #coule be rewritten with just using keyword[i % len(keyword) ] but I just wanted to make my 
       #students learn how to use strings not everyone was killing it in the programming game so I tried to make 
    #things intuitive and not need a big math background
    if len(keyword) < len(string):
        while len(newKeyword) < len(string):
            newKeyword += keyword[count]
            count += 1
            if count >= len(keyword) :
                count = 0

    elif len(keyword) == len(string):
        return keyword

    else:
        while len(newKeyword) < len(string):
            newKeyword += keyword[count]
            count += 1
            if count >= len(string):
                count = 0

    return newKeyword


# This function returns the
# encrypted text generated
# with the help of the key
def cipherText(string, key):
    cipher_text = []
    alphabet =  "abcdefghijklmnopqrstuvwxyz"

    for index in range(len(string)):

        current = string[index]
        current_key_index = alphabet.find(key[index ])
        if string[index] != " ":
            x = chr(( (ord(current) + current_key_index) % 26 + ord('A')))
            cipher_text += x
        else:
            cipher_text += current #adds the space



    return "".join(cipher_text)

# This function decrypts the
# encrypted text and returns
# the original text
def originalText(cipher_text, key):
    orig_text = []
    alphabet =  "abcdefghijklmnopqrstuvwxyz"
    for index in range(len(cipher_text)):

        current = cipher_text[index]
        current_key_index = alphabet.find(key[index])

        if cipher_text[index] != " ":
            x = chr(((ord(current) - current_key_index) % 26 + ord('A')))
            orig_text += x
        else:
            orig_text += current  # adds the space



    return "" . join(orig_text)

def main():
    string = input("enter a message").upper()
    keyword = "LOL"
    key = generateKey(string, keyword)

    cipher_text = cipherText(string, key)
    print(key)
    print("Ciphertext :", cipher_text)
    print("Original/Decrypted Text :", originalText(cipher_text, key))

main()
