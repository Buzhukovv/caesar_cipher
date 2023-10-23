import alphabet
def encoding(alpha ,double_aplha, origin_text):
    final_ans = ''
    for i in range (len(origin_text)):
        if origin_text[i] in alpha :
            index = alpha.index(origin_text[i]) + shift
            final_ans = final_ans + double_aplha[index]
        else:
            final_ans = final_ans + origin_text[i]
    return final_ans
def decoding(alpha ,double_aplha, origin_text):
    final_ans = ''
    for i in range (len(origin_text)):
        if origin_text[i] in alpha:
            index = alpha.index(origin_text[i]) - shift
            final_ans = final_ans + double_aplha[index]
        else:
            final_ans = final_ans + origin_text[i]
    return final_ans

from art import logo
print(logo)
steps = alphabet.alphabet
doubled = alphabet.alphabet * 2

working_game = True

while working_game == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        output = encoding(steps,doubled, text)
        print("Here's the encoded result: ", output)
    if direction == 'decode':
        output = decoding(steps,doubled, text)
        print("Here's the decoded result: ", output)
    work_or_not = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if work_or_not == 'yes':
        working_game = True
    elif work_or_not == 'no':
        working_game = False

