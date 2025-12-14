from DSU import DSU
from Graph import Graph
from Kruskals import Kruskals
import time

class Benchmarks:
    def __init__(self):
        self.SIZES = [20, 50, 100, 150, 200]
        self.DENSITIES = [10, 30, 50, 70, 90]
        self.ITERATIONS = 25

        self.results = []

    def test(self):
        for n in self.SIZES:
            for d in self.DENSITIES:

                adj_lists_times = []
                adj_matrix_times = []

                mst_times = []
                mst_optimized_times = []
                mst_percentages = []


                print(f"🔄 Тестую: {n} вершин, щільність {d}%...", end="\r")

                for _ in range(self.ITERATIONS):
                    graph = Graph(n, d)
                    g = graph.generate_graph()

                    adj_lists = graph.adjacency_lists(g)
                    adj_matrix = graph.adjacency_matrix(g)

                    #adj_lists
                    dsu_li = DSU(graph.set_a[:])
                    kruskals_li = Kruskals(dsu_li)

                    start_time = time.perf_counter()

                    kruskals_li.sort_weight_adj_lists(adj_lists)
                    kruskals_li.kruskal_mst()

                    end_time = time.perf_counter()

                    adj_lists_times.append(end_time - start_time)

                    #adj_matrix

                    dsu_mat = DSU(graph.set_a[:])
                    kruskals_mat = Kruskals(dsu_mat)

                    start_time = time.perf_counter()

                    kruskals_mat.sort_weight_matrix(adj_matrix)
                    kruskals_mat.kruskal_mst()

                    end_time = time.perf_counter()

                    adj_matrix_times.append(end_time - start_time)

                    #mst_experement
                    #not optimized
                    dsu_not_opt = DSU(graph.set_a[:])
                    kruskals_not_opt = Kruskals(dsu_not_opt)
                    kruskals_not_opt.weight_li = kruskals_mat.weight_li


                    start_time = time.perf_counter()

                    kruskals_not_opt.kruskal_mst()

                    end_time = time.perf_counter()

                    mst_times.append(end_time- start_time)

                    #optimized
                    dsu_opt = DSU(graph.set_a[:])
                    kruskals_opt = Kruskals(dsu_opt)
                    kruskals_opt.weight_li = kruskals_mat.weight_li

                    start_time = time.perf_counter()

                    _, percent = kruskals_opt.kruskal_mst_optimized()

                    end_time = time.perf_counter()

                    mst_optimized_times.append(end_time- start_time)
                    mst_percentages.append(percent)

                avg_list_time = sum(adj_lists_times) / len(adj_lists_times)
                avg_matrix_time = sum(adj_matrix_times) / len(adj_matrix_times)

                avg_mst = sum(mst_times) / len(mst_times)
                avg_mst_optimized = sum(mst_optimized_times) / len(mst_optimized_times)

                avg_mst_optimized_percentage = sum(mst_percentages) / len(mst_percentages)

                print(f"{n:<10} | {d:<10} | {avg_list_time:.6f}          | {avg_matrix_time:.6f}        ")

                self.results.append({
                    "Vertices": n,
                    "Density": d,
                    "List_Time": avg_list_time,
                    "Matrix_Time": avg_matrix_time,
                    "MST_time" : avg_mst,
                    "MST_optimized_time": avg_mst_optimized,
                    "MST_optimized_percentages": avg_mst_optimized_percentage
                })


        return self.results


