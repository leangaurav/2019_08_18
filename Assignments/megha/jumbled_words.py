import random
import urllib.request as request

def get_word():

	word = None

	try:

		req_obj = request.urlopen('http://tuteurpy.pythonanywhere.com/randomword')

		word = req_obj.read().decode("UTF-8")

		word = word.strip()

	except Exception as e:

		print("Exception getting Random word", str(e))

	return word

def jumble(word): 
    # sample() method shuffling the characters of the word 
    random_word = random.sample(word, len(word)) 
  
    # join() method join the elements 
    # of the iterator(e.g. list) with particular character . 
    jumbled = ''.join(random_word) 
    return jumbled 
  
  
# Function for playing the game. 
def play(): 
  
    # keep looping 
    while True: 
  
        # choose() function calling 
        picked_word = get_word() 
  
        # jumble() fucntion calling 
        qn = jumble(picked_word) 
        print("jumbled word is :", qn) 
        ans = input("Guess the word: ") 
        # checking ans is equal to picked_word or not 
        if ans == picked_word:
           print("Success")
           print("1.Play")
           print("2.Exit")
           z=int(input("Press 2 for exit:"))
           exit()
        else: 
             print("Better luck next time .. Continue the game") 

print("1.Play")
print("2.Exit")
i=int(input("Enter(1/2):"))
if(i==1):
    play() 
else:
    exit()


    
