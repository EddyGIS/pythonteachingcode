# [] create words after "G" following the Assignment requirements use of functions, methods and keyowrds
# Sample quote: "Old age isnt so bad wheen you consider the alternative" ~ George Burns (1896 - 1996)
# The auto fill text added George Burns' birthday,, all by itself. Cool!!

def words_after_g():
    quote = input("Welcome, Edward Graham. Enter a 1 sentence quote, non-alpha separate words: ")
    word = ""


    for letter in quote + " ":
        if letter.isalpha():
            word = word + letter
        else:
            if word != "":
                if word[0].lower() > "g":
                    print(word.upper())
                else:
                    word = ""
                word = ""


words_after_g()



