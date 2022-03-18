import random, string
from pystyle import Colorate, Colors, Center, System
import requests
from os import system
from time import sleep




System.Title("Lixio github.com/LixioCrac - ViewBot")




header_final = """

███╗░░░███╗███████╗███╗░░██╗░█████╗░░█████╗░███████╗
████╗░████║██╔════╝████╗░██║██╔══██╗██╔══██╗╚════██║
██╔████╔██║█████╗░░██╔██╗██║███████║██║░░╚═╝░░███╔═╝
██║╚██╔╝██║██╔══╝░░██║╚████║██╔══██║██║░░██╗██╔══╝░░
██║░╚═╝░██║███████╗██║░╚███║██║░░██║╚█████╔╝███████╗
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░╚══════╝\n\n\n\n"""


x = 0


print(Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter(header_final)))
url = input("Votre url: ")

while True:
	a = requests.get(url)
	x = x + 1 
	print(x, "Vue generer")
