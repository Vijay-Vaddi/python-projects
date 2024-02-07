# string contatenation 

new_word = 'General Kenobi'

# print('Hello there ' + new_word)
# print('Hello there {}'.format(new_word))
# print(f"Hello there {new_word}")

adj = input("Adjective : ")
verb1 = input("Verb : ")
verb2 = input("Effect : ")
res = input("Res : ")

madlibs = f"Computer programming is so {adj}! And it makes me excited all the time \
I love to {verb1}. It also gives me {verb2} and but I work hard to get {res}"

print(madlibs)