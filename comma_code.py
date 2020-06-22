def commaCode(spam):
        try:
                i = 0
                while i != len(spam) - 1:
                        print(spam[i], end=', ')
                        i += 1
                print('and ', end=str(spam[-1]))
        except IndexError:
                print('List is empty')
print('This commaCode puts together the input string with comma')

spam = []
while True:
        print('Enter data or enter nothing to end: ')
        data = input()
        if data == '':
                break
        spam = spam + [data]

commaCode(spam)
