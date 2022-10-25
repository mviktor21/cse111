planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

planets[3] = "Red Planet"

print("Mars is also known as", planets[3])

planets_total = len(planets)

print ("There are", planets_total, "planets in the solar system.")

planets.append("Pluto")
number_planets = len(planets)

print("There are", number_planets, "planets in the solar system?")

planets.pop()
number_of_planets = len(planets)

print("No, there are definitely", number_of_planets, "planets in the solar system.")

jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")