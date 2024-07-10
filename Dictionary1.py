"""
programming_dictionary = {
    'python': 'a high level programming language',
    'java': 'a high level programming language',
    'c++': 'a high level programming language',
    'javascript': 'a high level programming language',
    'ruby': 'a high level programming language',
    'php': 'a high level programming language',
    'c#': 'a high level programming language',
    'go': 'a high level programming language',
    'rust': 'a high level programming language',
    'elixir': 'a high level programming language',
    'kotlin': 'a high level programming language',
    'haskell': 'a high level programming language',
    'lisp': 'a high level programming language',
    'perl': 'a high level programming language',
    'lua': 'a high level programming language',
    'r': 'a high level programming language',
    'bash': 'a high level programming language',
    'assembly': 'a low level programming language',
    'lisp': 'a low level programming language',
    'Bug': 'An error in program that prevent the program from running as expected',
    'Loop': 'A loop is a block of code that is executed repeatedly',
    'Function': 'A function is a block of code that performs a specific task',
    'Variable': 'A variable is a container for storing data values',
    'Array': 'An array is a container that holds multiple values',
}

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

#a dictionary of countries and their capitals
capitals = {
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome',
    'Spain': 'Madrid',
    'United Kingdom': 'London',
    'United States': 'Washington, D.C.',
    'Canada': 'Ottawa',
}
#list nested inside a dictionary
travel_destinations = {
    'France': ['Paris', 'Lille', 'Dijon'],
    'Germany': ['Berlin', 'Hamburg', 'Munich'],
    'Italy': ['Rome', 'Milan', 'Naples'],
    'Spain': ['Madrid', 'Barcelona', 'Valencia'],
    'United Kingdom': ['London', 'Manchester', 'Birmingham'],
    'United States': ['Washington, D.C.', 'New York City', 'Los Angeles'],
    'Canada': ['Ottawa', 'Toronto', 'Vancouver'],
}

#a dictionary nested inside a dictionary
food_preferences = {
    'France': {'Food': {'Pizza', 'Pasta', 'Sushi'}, 
            'Drink': {'Coffee', 'Tea', 'Beer'},
    },
    'Germany': {
        'Food': {'Pasta', 'Pizza', 'Sushi'},
        'Drink': {'Coffee', 'Tea', 'Beer'},
    },
    'Ghana': 
        {
        'Food': {'Banku', 'Yam', 'Tuozaafi'},
        'Drink': {'Coffee', 'Tea', 'Beer'},
    },
}

# a dictionary nested inside a list

travel_log = [
    {
        'country': 'France',
        'cities_visited': ['Paris', 'Lille', 'Dijon'],
        'total visits': 3,
    },
    {
        'country': 'Germany',
        'cities_visited': ['Berlin', 'Hamburg', 'Munich'],
        'total_visits': 5,
    },
    {
        'country': 'Italy',
        'cities_visited': ['Rome', 'Milan', 'Naples'],
        'total_visits': 4,
    },
]
"""
# Exercise 1:
travel_log = [
    
    {
        'country': 'France',
        'cities_visited': ['Paris', 'Lille', 'Dijon'],
        'total visits': 3,
    },
    {
        'country': 'Germany',
        'cities_visited': ['Berlin', 'Hamburg', 'Munich'],
        'total_visits': 5,
    },
    {
        'country': 'Italy',
        'cities_visited': ['Rome', 'Milan', 'Naples'],
        'total_visits': 4,
    },
    
]

def add_new_country(country, cities_visited,times_visited):
    new_country = {}
    new_country['country'] = country
    new_country['visits'] = times_visited
    new_country['cities'] = cities_visited
    travel_log.append(new_country)
    
my_country = input("Enter the name of your country: \n")
visits = int(input("Enter the number of times visited: \n"))
cities_visited = input("Enter the cities visited by the country: \n")

add_new_country(country=my_country, times_visited=visits, cities_visited=cities_visited)
print(travel_log)