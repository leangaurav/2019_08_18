import random
def get_word():
    words=['Rear','Apple','Bargain','Teenager','Keen','Bagheera','Tanmay','Tornado']
    return random.choice(words).upper()

def guess_word_status(word,attempts,guess):
    status=''
    matches=0
    for letter in word:
        if letter in attempts:
            status+=letter
        else:
            status+='*'

        if letter==guess:
            matches+=1

    if matches>1:
        print('Yes! The word contains',matches,'"'+guess+'"'+'s')
    elif matches==1:
         print('Yes! The word conatins the letter"'+guess+'"')
    else:
        print('Sorry. The word does not contain the letter"'+guess+'"')
    return status

def play_game():
    word=get_word()
    attempts=[]
    attempted=False
    print('The word contains',len(word),'letters')
    while not attempted:
        text='Please enter one letter or a {} letter word,'.format(len(word))
        guess=input(text)
        guess=guess.upper()
        if guess in attempts:
            print('You already guessed"'+guess+'"')
        elif len(guess)==len(word):
            attempts.append(guess)
            if guess==word:
                attempted=True
            else:
                print('Sorry this is imcorrect')
        elif len(guess)==1:
             attempts.append(guess)
             result=guess_word_status(word,attempts,guess)
             if result==word:
                attempted=True
             else:
                  print(result)
        else:
            print('Invalid entry')
    print('Yes the word is',word+'! You got it in',len(attempts),'tries')     

play_game()
        
