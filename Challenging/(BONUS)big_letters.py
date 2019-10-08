#CHALLENGING PROBLEMS #3 (BIG LETTERS)
#DISPLAYS ANY LETTER FROM A - E IN LARGE FORMAT

def print_big(letter):
    letterdict = {
        "a": "  *  \n * * \n*****\n*   *\n*   *",
        "b": "**** \n*   *\n**** \n*   *\n****",
        "c": " *** \n*   *\n*    \n*   *\n *** ",
        "d": "**** \n*   *\n*   *\n*   *\n****",
        "e": "*****\n*    \n**** \n*    \n*****"
    }
    big_letter = letterdict.get(letter)
    return big_letter

print(print_big("e"))
