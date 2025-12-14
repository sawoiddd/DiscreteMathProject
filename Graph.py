import random
from email.contentmanager import raw_data_manager


class Graph:
    def __init__(self, num_ver, density):
        self.num_ver = num_ver
        self.density = density
        self.set_a = [i for i in range(0, self.num_ver)]

    def generate_graph(self):
        r = []
        all_edges = []
        for x in self.set_a:
            for y in self.set_a:
                if x != y and x > y:
                    all_edges.append((x, y))


        chosen_edges = random.sample(all_edges, k=round((len(all_edges) * (self.density / 100))))
        for x, y in chosen_edges:
            r.append((x, y, random.randint(1, 100)))

        return r

    def adjacency_lists(self, r):

        adj_lists = {}

        for i in r:
            adj_lists.setdefault(i[0], [])
            adj_lists.setdefault(i[1], [])

            adj_lists[i[0]].append((i[1], i[2]))
            if i[0] != i[1]:
                adj_lists[i[1]].append((i[0], i[2]))

        sorted_adj_lists = dict(sorted(adj_lists.items()))
        return sorted_adj_lists

    def adjacency_matrix(self, r):

        adj_matrix = [[0 for __ in range(len(self.set_a))] for _ in range(len(self.set_a))]

        for tup in r:
            adj_matrix[tup[0]][tup[1]] = tup[2]
            adj_matrix[tup[1]][tup[0]] = tup[2]


        return adj_matrix