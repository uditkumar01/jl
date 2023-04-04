import os
import colorama
# list all files
files = os.listdir('.')
print(files)

print(colorama.Fore.RED + 'Hello World' + colorama.Fore.RESET)
