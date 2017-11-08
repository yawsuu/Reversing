#!/usr/bin/env python
# Bruteforce Script for Cracker

print("++++++++++++++++++++++++++++++++++++")
print("+ DICK - Dictionary Cracker Script +")
print("++++++++++++++++++++++++++++++++++++")
print("+--------: Coded By [RDX] :--------+")
print("++++++++++++++++++++++++++++++++++++")

from sys import stdout
count=0
dict=raw_input("Enter Dictionary File : ")
f=open(dict,'r')
print "Please Wait ..."
for key in f.readlines():
    count+=1
    # print str(count)+" : key -> "+key.strip()
    stdout.write("\r%s" % key.strip())
    stdout.flush()
    # Insert any Algorythm here :)
    num=0
    num2=0
    num3=1
    key=key.strip()
    tlen=int(len(key))
    # print str(tlen)+" is key length"
    for xkey in key:
        num4=ord(xkey)
        # print str(num4)
        for j in range(0,tlen):
            # print str(num)+" "+str(num2)
            num5 = num + num3
            num4 = num4+num5
            num = num4
            #num6 = num2
            #num2 = num6 + num6
            num2 += num2
            num2 ^= num
            num4 = num
            num5 += 1
            num2 += num5
            num3 += 1
    #print str(num)+" "+str(num2)
    if num == 119150724474:
        if num2 == 20047891822756:
            stdout.write('\n')
            print "Bingo! Your BruteForce Succeed at "+str(count)+" counts :P"
            print "[KEY FOND]:===> "+key
            break
        else:
            pass
    else:
        pass




