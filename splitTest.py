word = 'bookworm'
spltWrd = list(word)
print(spltWrd)



# new = word.replace('o','w')
# print(new)


trying = True
while trying == True:
    #My dashes
    length = len(word)
    dash =''
    for i in range(length):
        dash = dash +'_'+' '
    print(dash)



    user = input('Enter a letter\n')
    initial = 0
    
    for i in spltWrd:
        if i == user:
            print(initial)
        initial += 1

    if user in spltWrd:
        print(True)
    else:
        print(False)
