planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")

planet_list.extend(["Uranus", "Neptune"])

planet_list.insert(1, "Venus")

planet_list.insert(2, "Earth")

planet_list.append("Pluto")

del planet_list[-1]

rocky_planets = slice(4)

print(planet_list)

print(planet_list[rocky_planets])

planet_list.append("Pluto is a real planet. >:[ You can never take them from my heart.")
