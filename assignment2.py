import os

filepath = r"C:\Users\Jurre Luijten\Documents\Master\2022-2023\Q3\Evolutionary Computing"
filename = "graph_data.txt"
file = os.path.join(filepath, filename)


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
   
               
with open(file, 'r') as data:

    points_list = []

    for line in data:

        components = line.strip().split()

        index = int(components[0])
        coordinates = components[1].split(',')
        coordinates = (coordinates[0][1:], coordinates[1][:-1])
        num_adjacent = int(components[2])
        adjacent_indices = list(map(int, components[3:]))

        new_point = Point(index, coordinates, num_adjacent, adjacent_indices)

        points_list.append(new_point)

print(points_list)


class Partition:
    def __init__(self, 
    





