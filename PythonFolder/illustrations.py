import cowsay, pyfiglet
from termcolor import colored


print('termcolor, colored:')
print(colored('Hello, World!', 'red'))

print('cowsay:')
message = "Hello, this is a cool terminal illustration!"
cowsay.cow(message)

print('pyfiglet')
banner = pyfiglet.Figlet(font='slant')
print(banner.renderText('Hello, World!'))