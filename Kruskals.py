from DSU import *
class Kruskals:
    def __init__(self, dsu:DSU):
        self.dsu = dsu
        self.weight_li = []

    def sort_weight_adj_lists(self, adj_dic):
        weight_li = []

        for key, value in adj_dic.items():
            for tup in value:
                if key <= tup[0]:
                    weight_li.append((tup[1], tup[0], key))


        weight_li = sorted(weight_li)
        self.weight_li = weight_li
        return weight_li

    def sort_weight_matrix(self, adj_matrix):
        weight_li = []

        for x in range(len(adj_matrix)):
            for y in range(len(adj_matrix)):
                if adj_matrix[x][y] != 0 and x > y:
                    weight_li.append((adj_matrix[x][y], x, y))


        weight_li = sorted(weight_li)
        self.weight_li = weight_li
        return  weight_li

    def kruskal_mst(self):
        mst = []

        for weight, ver1, ver2 in self.weight_li:
            if self.dsu.union(ver1, ver2):
                mst.append((ver1, ver2, weight))

        mst_value = sum([value[2] for value in mst])

        return mst_value

    def kruskal_mst_optimized(self):
        mst = []
        counter = 0
        print(f"DEBUG: Parent len: {len(self.dsu.parent)}, Target MST: {len(self.dsu.parent) - 1}")
        for weight, ver1, ver2 in self.weight_li:
            counter += 1

            if self.dsu.union(ver1, ver2):
                mst.append((ver1, ver2, weight))

                if len(mst) >= len(self.dsu.parent) - 1:
                    break

        mst_value = sum([value[2] for value in mst])

        percent_edge_looked = (counter / len(self.weight_li)) * 100

        return mst_value, percent_edge_looked


