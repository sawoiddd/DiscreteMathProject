
from benchamark import Benchmarks
from visuals import Visuals


bench = Benchmarks()
visuals = Visuals(bench.test())
visuals.show_plots()
visuals.plot_optimization_efficiency()










