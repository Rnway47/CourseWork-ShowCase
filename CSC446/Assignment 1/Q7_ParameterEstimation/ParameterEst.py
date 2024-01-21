import sys 
import numpy
# input a number greater than 0 smaller than 1 as P

def main():
    while True:
        try:
            head_prob = float(input("Enter the probability for Head: "))
        except: #check for valid input 
            print("Please enter a valid decimal number for probability")
            continue
        else:
            if(head_prob >=1 or head_prob <=0): #check for valid prob value
                print("The value for probability should be greater than 0 and smaller than 1")
                continue
            else:
                toss = 0 #need to reach 10000
                tail_prob = 1 - head_prob
                known_head = 0
                coin = [0, 1] # 0 is head, 1 is tail
                coin_prob = [head_prob, tail_prob]
                while toss < 10000:
                    toss += 1
                    outcome = numpy.random.choice(coin, size = 1, p=coin_prob)
                    if outcome == 0:
                        known_head += 1
                estimated = known_head/10000
                print("Estimated Value of P: ", estimated)
                print("Normalized Estimation Error: ", abs(head_prob-estimated)/head_prob)
                break

main()