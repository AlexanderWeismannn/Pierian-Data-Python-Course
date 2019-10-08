#LEVEL 1 PROBLEM 2 ( MASTER YODA)
#given a sentence return the sentence in reverse order

def master_yoda(sentence):
    yoda_list = sentence.split()
    new_list = yoda_list[::-1]
    string_list = ' '.join(new_list)
    return string_list

sentence = "I Am Home"
print(master_yoda(sentence))
