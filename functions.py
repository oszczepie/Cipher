import string

"""funkcja szyfrujaca"""
def ciphering():
    message = input('Please enter the message you\'d like to encrypt: ')
    s = int(input('Enter the shift in the alphabet to use: '))
    template = "".join([string.ascii_lowercase[s:], string.ascii_lowercase[:s]])
    global coded
    coded = message.translate(message.maketrans(string.ascii_lowercase, template))
    return print('That\'s the coded message: ' + coded)

#assert ciphering('ass', 2) == 'cuu', 'Incorrect ciphering'
#assert ciphering('ball', 26) == 'ball', 'Check the splicing'
#assert ciphering('13EZ', 2) == '13EZ', 'Numbers or uppercase letters change'


"""funkcja deszyfrujaca"""
def deciphering():
    global dict_of_options
    dict_of_options = {}
    for n in range(0, 26):
        un_template = "".join([string.ascii_lowercase[-n:], string.ascii_lowercase[:-n]])
        uncoded = coded.translate(coded.maketrans(string.ascii_lowercase, un_template))
        dict_of_options[n] = uncoded
    return dict_of_options


with open('words_alpha.txt') as words_list:
    english_words = list(set(words_list.read().split()))


"""sprawdzenie obecnosci w slowniku"""
def are_those_words():
    for key, opt in dict_of_options.items():
        odfiltrowane = list(map(lambda word: word in english_words, opt.split(" ")))
        if all(odfiltrowane) == True: return print('The shift value was probably: ' + str(key)
                                                   + '\nThe message was probably: ' + opt)
    return print("Words of the message cannot be recognized")


if __name__ == "__main__":
    ciphering()
    deciphering()
    are_those_words()