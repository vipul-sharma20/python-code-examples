# Finding palindromic subsequence
s = raw_input('')
for i in range(len(s)):
    for j in range(i, len(s)):
        if s[i:j] == s[i:j][::-1] and len(s[i:j])>=2:
            print s[i:j]
