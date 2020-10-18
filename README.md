
# Implementation of Shannon-Fano-Elias Coding
In this assignment, done for credit towards ECE F344 (Information Theory and coding), we have implemented an encoding algorithm for efficient representation of symbols called Shannon-Fano-Elias Coding. The group members in this project are: 

1. [Prasoon Baghel](https://github.com/prasoon0459) 
2. [Pranay Piyush](https://github.com/ProxiN-KamezA) 
3. [Harsh Heda](https://github.com/harsh-heda) 
4. [Mudit Mathur](https://github.com/mudit-mathur)
4. [Karan Kaul](https://github.com/sneakyGrit)
## The Algorithm
The algorithm is implemented in the `shannonfanoelias.py` file, and these are the relevant functions that you should be looking at: 

- `mcf` for calculating the modified cumulative frequency
- `len` for calculating the length of the code for a symbol
- `code` for generating the code for a symbol

# Instructions to Run
## Input
You can run the program in two ways. One is by running the predefined example cases in `examples` folder or by giving custom input.
#### 1. Run the example cases
Run the following command in a command-line :
 ``` 
 $ python3 main.py -t 
 ```
It will take a random file as the input from the examples folder and show the result accordingly.
#### 2. Give Custom input
Run the following command in a command-line:
```
 $ python3 main.py
 Please enter the number of symbols :  
```
Enter the number of symbols you want to encode and then their respective probabilities.
```
 $ python3 main.py
 Please enter the number of symbols : 5 
 
Please enter the respective probabilities :
  x0   -> 0.25
  x1   -> 0.25
  x2   -> 0.20
  x3   -> 0.15
  x4   -> 0.15
 
```
## Output
The program displays the symbols used and their respective probabilities. It shows _cumulative frequency_ and _modified cumulative frequency_ along with the generated _codeword_ for each symbol. It also checks and displays whether the code is a _prefix code_ or not. Then it displays the *__entropy__*, the *__average code length__* and the  *__efficiency__* for the coding scheme and the given data set as shown below:

```

# Symbols

Symbol  Probability
―――――――――――――――――――
 x0       0.2500    
 x1       0.2500    
 x2       0.2000    
 x3       0.1500    
 x4       0.1500    


# Shannon-Fano-Elias-Coding
                                                  
Symbol  Probability    F(x)      F̅(x)     Codeword
――――――――――――――――――――――――――――――――――――――――――――――――――
 x0       0.2500       0.2500   0.1250     001            
 x1       0.2500       0.5000   0.3750     011            
 x2       0.2000       0.7000   0.6000     1001           
 x3       0.1500       0.8500   0.7750     1100           
 x4       0.1500       1.0000   0.9250     1110           


―――――――――――――――――――――――――――――――――――――――――――――――
 The generated code is a valid prefix code.
―――――――――――――――――――――――――――――――――――――――――――――――

Entropy for the given data is                              : 2.2855 bits
Average length for Shannon Fano Elias Code is              : 3.5000 bits
Efficiency of the coding scheme for the given data set is  : 0.6530 


```