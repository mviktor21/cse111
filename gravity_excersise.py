gravity_on_earth = 1.0
gravity_on_moon = 0.166

gravity_on_planets = [0.378, 0.907, 1.0, 0.377, 2.36, 0.916, 0.889, 1.12]

variable = float(gravity_on_earth)

print("The gravity on Earth is", variable)

bus_weight = 12650

print("The bus weight on Mercury is", bus_weight * gravity_on_planets[0], "Kg")