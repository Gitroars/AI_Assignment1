import random
import math
cities = {
    'a': {'b': 12, 'c': 10, 'g': 12},
    'b': {'a': 12, 'c': 8, 'd': 12},
    'c': {'a': 10, 'b': 8, 'd': 11, 'e': 3, 'g': 9},
    'd': {'b': 12, 'c': 11, 'e': 11, 'f': 10},
    'e': {'c': 3, 'd': 11, 'f': 6, 'g': 7},
    'f': {'d': 10, 'e': 6, 'g': 9},
    'g': {'a': 12, 'c': 9, 'e': 7, 'f': 9}
}


def initialize_population(num_individuals, cities):
    num_cities = len(cities)
    population = []

    city_list = list(cities.keys())
    city_list.remove('a')

    for _ in range(num_individuals):
        
        random.shuffle(city_list)

        
        route = ['a'] + city_list + ['a']
        
        # Ensure valid connections
        while not is_valid_route(route, cities):
            random.shuffle(city_list)
            route = ['a'] + city_list + ['a']
        
        population.append(route)

    return population

def is_valid_route(route, cities):
    for i in range(len(route) - 1):
        from_city = route[i]
        to_city = route[i + 1]
        if to_city not in cities[from_city]:
            return False
    return True

def calculate_total_distance(route, cities):
    total_distance = 0
    for i in range(len(route) - 1):
        from_city = route[i]
        to_city = route[i + 1]
        if to_city in cities[from_city]:
            total_distance += cities[from_city][to_city]
        else:
            # determine route is invalid
            return float('inf')  
    return total_distance


def calculate_fitness(route, cities):
    total_distance = calculate_total_distance(route, cities)
    if total_distance == float('inf'): #handle invalid route
        return 0.0  
    else:
        return 1.0 / total_distance

def proportional_selection(population,fitness_values):
    total_fitness = sum(fitness_values)
    selection_probabilities = [fitness / total_fitness for fitness in fitness_values]
    parent1 = random.choices(population, selection_probabilities)[0]
    parent2 = random.choices(population, selection_probabilities)[0]

    return parent1, parent2

def crossover(parent1, parent2):
    crossover_point = random.randint(1,len(parent1)-2)
    offspring = [None] * len(parent1)
    offspring[0] = 'a'
    offspring[-1] = 'a'
    offspring[1:crossover_point] = parent1[1:crossover_point]
    remaining_cities = [city for city in parent2 if city not in offspring]

    for i in range(1, len(offspring) - 1):
        if offspring[i] is None:
            offspring[i] = remaining_cities.pop(0)

    return offspring

def mutate(offspring):
    pos1,pos2 = random.sample(range(1,len(offspring)-1),2)
    offspring[pos1],offspring[pos2] = offspring[pos2],offspring[pos1]
    return offspring

def replace_population(old_population, offspring, num_individuals):
    combined_population = old_population + offspring
    combined_population.sort(key=lambda route: calculate_fitness(route, cities), reverse=True)
    new_population = combined_population[:num_individuals]
    return new_population

num_individuals = 50  
num_generations = 100

population = initialize_population(num_individuals, cities)
print(population)

for generation in range(num_generations):
    fitness_values = [calculate_fitness(route, cities) for route in population]
    new_population = []
    for i in range(num_individuals//2):
        parent1, parent2 = proportional_selection(population, fitness_values)
        offspring = crossover(parent1, parent2)
        offspring = mutate(offspring)
        new_population.append(offspring)
    
    population = replace_population(population, new_population, num_individuals)

best_route = min(population, key=lambda route: calculate_fitness(route, cities))
best_fitness = calculate_fitness(best_route, cities)
print("Best Route:", best_route)
print("Best Fitness:", best_fitness)
    
