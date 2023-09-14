from calculate import *

inputs = []
check_0 = True
print("\nYou can input while you do not input 0\n")
while check_0:
    check_input = True
    while check_input:
        print("Enter number of balls in range 27-127:")
        numballs = int(input())
        if numballs == 0:
            check_0 = False
            check_input = False
        elif 27 <= numballs <= 127:
            inputs.append(numballs)
            check_input = False
        else:
            print("Entered number of balls is not supported.")

for i in inputs:
    clocks = Clock(i)
    result_cycles = clocks.simulate()
    print("With number of balls: ", i)
    print("Cycles to revert in previous state: ", Clock.cycles_to_time(result_cycles))
    print("--------------------------------------------------")
