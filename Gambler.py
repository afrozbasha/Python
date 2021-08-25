"""
    @Author: Afroz Basha
    @Date: 2021-08-25
    @Title: 2D ARRAY
"""
import random
import sys

"""
Description:
 Simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
times he/she wins and the number of bets he/she makes. Run the experiment N
times, averages the results, and prints them out.

Parameter:
    No Syntax only Logic Using While and if condition
    
Return:
        It returns the amount gambled.
"""

Rs = 100
lossCount = 0
win = 200
count = 1
winCount = 0

while True:
    bet = random.randrange(2)
    count += 1
    if bet == 1:
        Rs += 1
        winCount += 1
        if Rs == win:
            print("You win 100 Rs")
            print("You win ", winCount, " times")
            print("You attempted ", count, " times")
            sys.exit()
    else:
        Rs -= 1
        lossCount += 1
        if Rs == 0:
            print("You loss 100 Rs")
            print("You loss ", lossCount, " times")
            print("You attempted ", count, " times")
            sys.exit()