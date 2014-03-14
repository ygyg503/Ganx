import easygui
import random

the_code = random.randint(1,100)
guess_times = 6
easygui.msgbox("The game very easy! you guess a number in 1~100")
while guess_times > 0:
	guess_times -= 1
	user_guess =int(easygui.enterbox("Input you guess numbers"))
	if user_guess == the_code:
	    easygui.msgbox("Good job ~you guess the number ! and it's %d" % the_code)
	elif user_guess < the_code:
		easygui.msgbox("To small and you have %d times" % guess_times)
	else:
		easygui.msgbox("To big and you have %d times " % guess_times)
if user_guess != the_code:
	easygui.msgbox("Your lose ! loser Man")
