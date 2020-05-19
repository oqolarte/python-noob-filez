import webbrowser, sys, pyperclip
sys.argv
# check if command line arguments are passed
if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/' + address)



