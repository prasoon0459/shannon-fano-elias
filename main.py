import sys
from shannonfanoelias import sfe
from prefcode import isprefixcode
from util import avgLength, entropy, efficiency, rand

#input

prob={}
no=len(sys.argv)

if no > 1 and sys.argv[1]=="-t":        # user wants the test data to be loaded

    i=rand(1,6) 
    filename= str(i)
    path="examples/"+filename
    f=open(path, "r")
    n=int(f.readline())
    for i in range(n):
        sym="x"+str(i)
        x=float(f.readline())
        prob[sym]=x
    print("Loading Test Data : ")

else:                                   # user wants to give the input

    n=int(input("Please enter the number of symbols : "))
    print("\nPlease enter the respective probabilities :")
    for i in range(n):
        sym="x"+str(i)
        x=float(input(" {}   -> ".format(sym)))
        prob[sym]=x
    print("")


# show input symbols and probabilities
print("\n# Symbols\n")
print("Symbol  Probability")
print("―――――――――――――――――――")
for s, p in prob.items():
    print(' %-8s' % s,'%-10.4f' % p)
print("\n")

# code
print("# Shannon-Fano-Elias-Coding")
code = sfe(prob)

# show the result
print(    "                                                  ")
print(    "Symbol  Probability    F(x)      F̅(x)     Codeword")
print(    "――――――――――――――――――――――――――――――――――――――――――――――――――")
curr_sum=0.0
for s in prob.keys():
    mc=curr_sum+prob[s]/2
    curr_sum+=prob[s]
    print(' %-8s' % s, '%-12.4f' % prob[s], '%-8.4f' % curr_sum, '%-10.4f' % mc, '%-15s' % code[s])

# checking whether the code is a valid prefix code or not
isprefixcode(code)

# calculating and displaying the entropy, avg length and the efficiency of the code
print("")
en = entropy(prob.values())
av_len= avgLength(code, prob)
ef= efficiency(en, av_len)
print("Entropy for the given data is                              : {:.4f} bits".format(en))
print("Average length for Shannon Fano Elias Code is              : {:.4f} bits".format(av_len))
print("Efficiency of the coding scheme for the given data set is  : {:.4f} ".format(ef))

print("")
#end