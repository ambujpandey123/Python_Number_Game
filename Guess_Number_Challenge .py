about='\n\nAbout This Game:\n\nIn This Game The Computer Has Guessed The Number And You Have To Guess The Same Number.'

#importing random module
import random
num= random.randrange(1,41)
#print basic Rules of the game 
print('-------------- WELCOME TO NUMBER GUESS CHALLEGE GAME --------------')
info='\n \n\n RULES: Guess The Number in between 1 to 40\n\tOnly "5 chance" do you have.\n\nClick "about" To know game info \nClick "Enter" to start game:\n\n'
print(info)
count=5 #Total Chances declear
great=0  #Count Chances 

#  Creating a Function To take the Number and Check The number is correct or not
def check(guess):
	if num == guess:
	       print(f'\nYou Win at {great} Chance(s) Congratulations')
	       return True
	# if you fail to guess this condition occur
	if count == 0:
	       print(f'Total {great} False guesses.\nYou have No More Chances {count} \n')
	       print('\nYou Fail to Win the game..')
	       return False
	#Sujjest the number is greater then you guess	      
	elif(num>guess):
		print('Please Try larger number. ')
		print(f'Total {great} False guesses.\nComplete The game  at  {count} Chance(s) only do you have\n')
	#Sujjest the number is less then you guess
	else:
		print('Please Try lower number.')
		print(f'Total {great} False guesses.\nComplete The game  at  {count} Chance only do you have\n')

# Game Enter Section 
enter=input('Start\\..')							
if(enter == ''):
	#Run the While loop 5 times
	while(count>0):
		count-=1
		great+=1				
		guess=int(input('   Enter a numer: '))
		if guess <1 or guess>40:
			print('Please Enter Number in between 1 to 40')
		#by Creating object run the function
		a=check(guess)
		#if user guess is correct break the loop.
		if(a):
			break
		else:
			continue
#Game Quit Condition below		
else:
	if enter=='about':
		print(about)
		print(info)
	else:
		print('Game Quit Successfully')	