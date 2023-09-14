# Counting Time (py-3-5)  
  
---  
  
## Create and switch to new branch ***Internship-py-3-5*** using Sourcetree  
  
___  
  
## Update `calculate.py` to bring all the pieces of the clock together:  
  
**1.** Create a method that indicates the clock is working and time is being counted  
  
**2.** Create a library call for counting time  
  
- Call the tick() function repeatedly until the balls come to rest in their original positions  
  
- Call the check_balls_sequence() function to tell when the balls have returned to their original positions  
  
---  
  
## Update `main.py` to implement the ‘calculate’ library for counting time:  
  
**1.** Implement ability to accept continuous user input (any number between 27 and 127) until the user enters ***0*** to indicate the end of the stream  
  
**2.** Implement the validation of the input data  
  
**3.** Write the output to the terminal window  
  
___  
  
## Run the app  
  
`% python3 main.py`  
```

You can input while you do not input 0

Enter number of balls in range 27-127:
15
Entered number of balls is not supported.
Enter number of balls in range 27-127:
30
Enter number of balls in range 27-127:
45
Enter number of balls in range 27-127:
60
Enter number of balls in range 27-127:
75
Enter number of balls in range 27-127:
90
Enter number of balls in range 27-127:
105
Enter number of balls in range 27-127:
120
Enter number of balls in range 27-127:
135
Entered number of balls is not supported.
Enter number of balls in range 27-127:
0
With number of balls:  30
Cycles to revert in previous state:  15 days 
--------------------------------------------------
With number of balls:  45
Cycles to revert in previous state:  378 days 
--------------------------------------------------
With number of balls:  60
Cycles to revert in previous state:  495 days 
--------------------------------------------------
With number of balls:  75
Cycles to revert in previous state:  1955 days 
--------------------------------------------------
With number of balls:  90
Cycles to revert in previous state:  1218 days 
--------------------------------------------------
With number of balls:  105
Cycles to revert in previous state:  1464 days 
--------------------------------------------------
With number of balls:  120
Cycles to revert in previous state:  1224 days 
--------------------------------------------------  
```  
  
---  
  
## Push to GitHub with Sourcetree  
  
---  
