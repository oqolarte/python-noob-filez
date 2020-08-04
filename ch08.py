import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        print('Done. (not so hard, is it?)')
        sys.exit()
    print('You typed ' + response + '.')
