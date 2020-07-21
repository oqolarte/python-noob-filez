def is_anagram(textA, textB):
    ana = list(textB)
    for i,c in enumerate(textA):
       if textA[i] not in ana:
           print('False')
           break
       else:
           print('True')
           break

is_anagram('ajdsflkajdslixxxxf', 'babaiyyyyyzzzzdook')
is_anagram('bob', 'obb')
is_anagram('bob', 'adskjflau')
is_anagram('typhoon', 'opython')
is_anagram('ana', 'bob')


