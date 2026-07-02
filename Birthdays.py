birthdays = {'Alice':'April 1', 'Bob':'December 12','Carol':'March 4'}

while True:
    print('Enter a name: (0 to quit ; 1 to print all birthdays; 2 to print all names)')
    name = input()
    if name == '0':
        break
    elif name == '1':
        for v in birthdays.values():
            print(v)
        continue
    elif name == '2':
        for k in birthdays.keys():
            print(k)
        continue
    if name in birthdays:
        print(birthdays[name]+' is the birthday of '+name)
    else:
        print('I do not have the birthday information for '+name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')