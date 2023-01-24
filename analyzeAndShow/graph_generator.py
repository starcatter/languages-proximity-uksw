import argparse

from analyzeAndShow.constants_mysql import all_languages, all_categories
from analyzeAndShow.graph_coordinates import produce_graph
from analyzeAndShow.word_metrics import functions_dict

parser = argparse.ArgumentParser(description='Calculates differences between the selected languages over the selected categories and shows the results as a graph.', )
parser.add_argument("--lang", "-l", choices=all_languages + ["all"], required=True, metavar='L', nargs='+', help="languages for comparison, at least 2")
parser.add_argument("--cat", "-c", choices=all_categories + ["all"], required=True, metavar='C', nargs='+', help="at least one category")
parser.add_argument("--node", "-n", choices=["lang", "cat"], default="lang", metavar="N", help="type of node displayed on the graph")
parser.add_argument("--metric", "-m", choices=list(functions_dict.keys()), metavar='M', default="Levenshtein", help="a metric used for string distance calculations")
parser.add_argument("--n_cpu", "-p", default=1, type=int, help="number of cores used to compute distances")
parser.add_argument("--display", "-d", default=False, const=True, action="store_const", help="should the graph be displayed in GraphGtream")
parser.add_argument("--export", "-e", default=False, const=True, action="store_const", help="should the graph be exported to PNG file in the current working directory")

if __name__ == "__main__":
    args = parser.parse_args()
    if "all" not in args.lang and len(args.lang) < 2:
        print("There should be at least 2 languages specified!")
        exit(1)
    if "all" in args.lang and len(args.lang) > 1:
        print("\"all\" cannot be merged with languages!")
        exit(1)
    if "all" in args.cat and len(args.cat) > 1:
        print("\"all\" cannot be merged with categories!")
        exit(1)
    if not args.display and not args.export:
        print("Please select -d for display or -e for export in order to see the graph!")
        exit(1)
    print(args)
    produce_graph(args.lang, args.cat, args.node, args.metric, args.n_cpu, args.display, args.export)
    if args.display:
        input("Press \"Enter\" to close graph.\n")
        exit(0)
