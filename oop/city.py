# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3_399
city1.population = 358_052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2_290
city2.population = 1_241_675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9_733_509


def max_elevation_city(min_population):
	# Initialize the variable that will hold 
    # the information of the city with 
    # the highest elevation 
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city1.population >= min_population and city1.population < city2.population and city1.population < city3.population:
		return_city = city1
		
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city2.population >= min_population and city2.population < city1.population and city2.population < city3.population:
		return_city = city2
		
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city3.population >= min_population and city3.elevation > city1.elevation and city3.elevation > city2.elevation:
		return_city = city3

	# Format the return string
	if return_city.name:
		return return_city.name + ", " + return_city.country
	else:
		return ""

print(max_elevation_city(100_000)) # Should print "Cusco, Peru"
print(max_elevation_city(1_000_000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10_000_000)) # Should print ""