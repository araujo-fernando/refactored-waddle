import os

from argparse import ArgumentParser
from src import *

def main(file: str, algorithms):
    graph = CompleteUndirectedGraph(create_vertexes_from_file(file))

    print("Graph data")
    print("Total vertexes:", len(graph.V))
    print("Total edges:", len(graph.edges), "\n")
    
    for alg in algorithms:
        tree = eval(alg)(graph)
        print_results(tree, alg)


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("file", help="File for the graph instance")
    parser.add_argument("algorithm", help="Algorithm to use: Kruskall, Prim, All", choices=["kruskal", "prim", "all"], default="")
    return parser

if __name__ == "__main__":
    parser = parse_arguments()
    args = parser.parse_args()

    if not os.path.isdir("logs"):
        os.mkdir("logs")
    if args.algorithm == "all":
        args.algorithm = ["kruskal", "prim"]

    main(args.file, args.algorithm)
