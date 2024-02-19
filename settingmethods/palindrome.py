word="malayalam"
count=len(word)
p_str=""
for i in range(count-1,-1,-1):
    p_str+=word[i]
print("palindrome" if word==p_str else"not palindrome")

