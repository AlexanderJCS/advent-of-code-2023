import math

import part_1


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    nodes_dict = {}
    for line in lines[2:]:
        node = part_1.parse_node(line)
        nodes_dict[node.name] = node

    a_nodes = [node_name for node_name in nodes_dict.keys() if node_name[-1] == "A"]

    steps_for_each_node = [
        part_1.walk_tree(lines[0], nodes_dict, start_node=a_node, end_node_re="..Z")
        for a_node in a_nodes
    ]

    print(math.lcm(*steps_for_each_node))


if __name__ == "__main__":
    main()
