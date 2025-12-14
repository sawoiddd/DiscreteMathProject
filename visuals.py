import matplotlib.pyplot as plt

class Visuals:
    def __init__(self, results):
        self.results = results

        self.unique_sizes = sorted(list(set(r['Vertices'] for r in results)))
        self.unique_densities = sorted(list(set(r['Density'] for r in results)))

        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(14, 6))


    def __dependency_vertices(self):
        target_densities = [10, 90]
        colors = ['blue', 'red']

        for i, d in enumerate(target_densities):
            # Фільтруємо дані тільки для цієї щільності
            data = [r for r in self.results if r['Density'] == d]

            x = [r['Vertices'] for r in data]
            y_list = [r['List_Time'] for r in data]
            y_matrix = [r['Matrix_Time'] for r in data]

            # Малюємо лінії
            self.ax1.plot(x, y_list, marker='o', linestyle='-', color=colors[i], label=f'Lists (D={d}%)')
            self.ax1.plot(x, y_matrix, marker='x', linestyle='--', color=colors[i], label=f'Matrix (D={d}%)')

        self.ax1.set_title('Залежність часу від Кількості Вершин')
        self.ax1.set_xlabel('Кількість Вершин (N)')
        self.ax1.set_ylabel('Час (сек)')
        self.ax1.legend()
        self.ax1.grid(True)

    def __dependency_density(self):
        max_n = max(self.unique_sizes)
        data_n = [r for r in self.results if r['Vertices'] == max_n]

        x_d = [r['Density'] for r in data_n]
        y_list_n = [r['List_Time'] for r in data_n]
        y_matrix_n = [r['Matrix_Time'] for r in data_n]

        self.ax2.plot(x_d, y_list_n, marker='o', label='Adjacency Lists', color='green')
        self.ax2.plot(x_d, y_matrix_n, marker='x', label='Adjacency Matrix', color='purple')

        self.ax2.set_title(f'Залежність часу від Щільності (при N={max_n})')
        self.ax2.set_xlabel('Щільність (%)')
        self.ax2.set_ylabel('Час (сек)')
        self.ax2.legend()
        self.ax2.grid(True)

    def show_plots(self):
        self.__dependency_vertices()
        self.__dependency_density()
        plt.tight_layout()

        plt.savefig("benchmark_results.png")

        plt.show()

    def plot_optimization_efficiency(self):
        plt.figure(figsize=(10, 6))
        plt.grid(True, linestyle='--', alpha=0.7)

        for n in self.unique_sizes:
            data_n = [r for r in self.results if r['Vertices'] == n]

            data_n.sort(key=lambda x: x['Density'])

            densities = [r['Density'] for r in data_n]
            percentages = [r['MST_optimized_percentages'] for r in data_n]

            plt.plot(densities, percentages, marker='o', label=f'N={n}')

        plt.xlabel('Щільність графа (%)')
        plt.ylabel('Відсоток перевірених ребер (%)')
        plt.title('Ефективність оптимізації алгоритму Крускала')
        plt.legend(title="Кількість вершин")

        plt.savefig("optimization_efficiency.png")

        plt.show()