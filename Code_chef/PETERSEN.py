# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 11:08:55 2016

@author: shashank
"""
        
neighbours_out = {'A':'ABE','B':'BAC','C':'CBD','D':'DCE','E':'EAD'}
neighbours_in = {'A':'ACD','B':'BDE','C':'CAE','D':'DAB','E':'EBC'}
indices = {'A':'0','B':'1','C':'2','D':'3','E':'4','a':'5','b':'6','c':'7','d':'8','e':'9'}
T = input()
for i in range(T):
    S = raw_input()
    ic = 0
    new_string = [0 for i in range(len(S))]
    for i in range(1,len(S)):
        if S[i] != S[ic]:
            if S[i] in neighbours_out[S[ic]]:
                new_string[i] = S[i]
                dummy = 0
                for j in range(ic,-1,-1):
                    if dummy == 0:
                        new_string[j] = S[j]
                        dummy = 1
                    elif dummy == 1:
                        new_string[j] = S[j].lower()
                        dummy = 0
            elif S[i] in neighbours_in[S[ic]]:
                new_string[i] = S[i]
                dummy = 1
                for j in range(ic,-1,-1):
                    if dummy == 0:
                        new_string[j] = S[j]
                        dummy = 1
                    elif dummy == 1:
                        new_string[j] = S[j].lower()
                        dummy = 0
            break
        ic+=1
    k = ic+1
    output = ''
    if new_string[0] != 0:        
        for i in range(k-1,len(S)-1):
            if (((S[i+1] not in neighbours_out[S[i]]) and (new_string[i].isupper())) or ((S[i+1] not in neighbours_in[S[i]]) and (new_string[i].islower()))) :
                output = -1
                break
            elif S[i+1] == S[i]:
                if new_string[i].isupper():
                    new_string[i+1] = S[i+1].lower()
                else:
                    new_string[i+1] = S[i+1]
            elif S[i+1] in neighbours_out[S[i]]:
                new_string[i+1] = S[i+1]
            elif S[i+1] in neighbours_in[S[i]]:
                new_string[i+1] = S[i+1].lower()
    if new_string[0] == 0:
        new_string[0] = S[0]
        for j in range(1,len(S)):
            if new_string[j-1].isupper():
                new_string[j] = S[j].lower()
            else:
                new_string[j] = S[j]
    if output != -1:
        for l in range(len(new_string)):
            output = output + (indices[new_string[l]])
    if new_string[0] == 'A' and output != -1:
        print '%d%d'%(0,int(output))
    else:
        print int(output)
                
        
        
    
                        
                    
            
            
            
            
