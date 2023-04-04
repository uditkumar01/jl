import os
import colorama
# list all files
files = os.listdir('.')
print(files)

print(colorama.Fore.RED + 'Hello World' + colorama.Fore.RESET)
print("\u001B[31mHello World\u001B[0m")
