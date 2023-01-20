# Project: Languages Proximity

## Setup

### Prerequisites
- Java 1.8
- Maven
- Python 3.10 (other versions not tested)

### Repository download
`git clone https://github.com/akelm/languages_proximity_uksw.git`
### Build fat jar, create Python venv and install dependencies
```
chmod +x setup.sh
JAVA_HOME=<your-java-1.8-home-path> ./setup.sh
```

## Execution

### Generate graph from data, save and/or plot results
```
chmod +x run_graph_generator.sh
./run_graph_generator.sh
```
The script `run_graph_generator.sh` is a proxy to Python module `analyzeAndShow.graph_generator`, which accepts the following arguments:
```
$ ./run_graph_generator.sh -h
usage: graph_generator.py [-h] --lang L [L ...] --cat C [C ...] [--node N] [--metric M] [--n_cpu N_CPU] [--display] [--export]

Calculates differences between the selected languages over the selected categories and shows the results as a graph.

options:
  -h, --help            show this help message and exit
  --lang L [L ...], -l L [L ...]
                        languages for comparison, at least 2
  --cat C [C ...], -c C [C ...]
                        at least one category
  --node N, -n N        type of node displayed on the graph
  --metric M, -m M      a metric used for string distance calculations
  --n_cpu N_CPU, -p N_CPU
                        number of cores used to compute distances
  --display, -d         should the graph be displayed in GraphGtream
  --export, -e          should the graph be exported to PNG file in the current working directory

```


## Disclaimer
**Not tested on MacOS**