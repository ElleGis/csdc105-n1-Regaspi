# Author          : Ma. Giselle N. Regaspi
# Course and Year : BS IT-2 
# Filename        : Regaspi_e2.py
# Description     : A program that prints the personal information
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

data = {}
data["name"] = "Ma. Giselle N. Regaspi"
data["spirit_animal"] = "Elephant shrew"
data["reason"] = "I don't easily give up"
data["hobbies"] = ["Watching movies", "Reading Wattpad stories", "Riding in a bicycle"]
data["dream"] = "Artist"

print("I am {}.".format(data["name"]))
print("My spirit animal is {},".format(data["spirit_animal"]))
print("because {}.".format(data["reason"]))
print("When not in school, I love to: ")
print("* {}".format(data["hobbies"][0]))
print("* {}".format(data["hobbies"][1]))
print("* {}".format(data["hobbies"][2]))
print("I dream of being an {} in the future.".format(data["dream"]))

