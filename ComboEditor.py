import re
import os


def clean(textfile):
    combos = open(textfile, 'r', encoding="utf-8")
    wombo = []
    for combo in combos:
        combo = combo.strip()
        x = re.findall(r"(?i)[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}:[A-Za-z0-9*.?!\/|@#$%^&*()]+", combo)
        for i in x:
            if len(i) > 0:
                wombo.append(i)
    return [*set(wombo)]

def password_editor(combo):
    special_characters = ('''!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~''')
    wombo = []
    for emailpass in combo:
        wombo.append(emailpass)
        email = (emailpass.partition(':')[0])
        password = (emailpass.partition(':')[2])
        try:
            if not password[0].isupper():
                password = password.capitalize()
            if len(password) < 8:
                password = (password + '123')
            if not any(c in special_characters for c in password):
                list = ['!', '@', '$']
                lol = range(3)
                for number in lol:
                    special_password = (password + list[number])
                    wombo.append(email + ':' + special_password)
        except:
            pass
    try:
        percentage = ((len([*set(wombo)]) / len(combo)) * 100)
        print(f'''Great your combo was increased by  {round(percentage)}%''')
    except:
        print('Your combo cannot be greater')
        exit()

    return [*set(wombo)]

def save(name, data):
    with open(name + '.txt', 'w', encoding="utf-8") as fp:
        for line in data:
            fp.write("%s\n" % line)

if __name__ == '__main__':
    print('''Grab the txt file''')
    file = input()
    name = (os.path.basename(file).split('.txt')[0])
    save((name + '-Cleaned'), clean(file))
    save((name + '-Improved'), password_editor(clean(file)))
