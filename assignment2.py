import os
import random

class Point:
    def __init__(self, index, coordinates: (float, float), num_adjacent, adjacent_indices):
        self.index = index
        self.coordinates = coordinates
        self.num_adjacent = num_adjacent
        self.adjacent_indices = adjacent_indices
    
    def __str__(self):
        return f'({self.index}, ({self.coordinates[0]}, {self.coordinates[1]}), {self.num_adjacent}, {self.adjacent_indices})'
    
    def __repr__(self):
        return f'({self.index}, ({self.coordinates[0]}, {self.coordinates[1]}), {self.num_adjacent}, {self.adjacent_indices})'

class Graph:
    def __init__(self, points: [Point]):
        self.points = points
        
    def number_of_edges(self):
        result = 0
        for point in self.points:
            result += point.num_adjacent        
        return result / 2

class Partition:
    def __init__(self, bitstring=None):
        self.bitstring = bitstring
        if bitstring == None:
            self.bitstring = self.create_random_partition()
            
    def __str__(self):
        return f'({self.bitstring})'
    
    def create_random_partition(self):
        ones = [1] * 250
        zeros = [0] * 250
        
        random_partition = ones + zeros
        random.shuffle(random_partition)
        return random_partition
           
    def is_valid(self):
        return len(self.bitstring) == 500 and sum(self.bitstring) == 250
    
    def fitness_part(self, graph: Graph):
        fitness = 0
        for i, value in enumerate(self.bitstring):
            if value == 1:
                for adjacent_index in graph.points[i].adjacent_indices:
                    if self.bitstring[adjacent_index - 1] == 0:
                        fitness += 1
        return fitness
    
def load_file(file):
    with open(file, 'r') as data:    
        points = []
    
        for line in data:    
            components = line.strip().split()
    
            index = int(components[0])
            coordinates = components[1].split(',')
            coordinates = (coordinates[0][1:], coordinates[1][:-1])
            num_adjacent = int(components[2])
            adjacent_indices = list(map(int, components[3:]))
    
            new_point = Point(index, coordinates, num_adjacent, adjacent_indices)
    
            points.append(new_point)
            
    return Graph(points)
    
def genetic_algorithm(file):
    graph = load_file(file)
    print(graph.number_of_edges())
    partition = Partition()
    fitness = partition.fitness_part(graph)
    print(fitness)

def main():
    filepath = r"C:\Users\Jurre Luijten\Documents\Master\2022-2023\Q3\Evolutionary Computing\Evolutionary-Computing-Assignment-2"
    filename = "graph_data.txt"
    file = os.path.join(filepath, filename)
    
    genetic_algorithm(file)

if __name__== "__main__":
    main()





