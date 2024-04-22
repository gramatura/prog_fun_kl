def check_anagrams(s1, s2):
    if(sorted(s1)== sorted(s2)):
        print("anagram") 
    else:
        print("nie anagram")         
         
s1 ="faal"
s2 ="fala"
check_anagrams(s1, s2)

s1="nwm"
s2="nieniewiem"
check_anagrams(s1,s2)
