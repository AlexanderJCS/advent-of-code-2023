from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Node:
    name: str
    left: str
    right: str


def parse_node(line: str) -> Node:
    name, edges = line.split(" = ")
    left, right = edges.strip("()").split(", ")

    return Node(name, left, right)


def walk_tree(steps: str, nodes: dict[str, Node], start_node="AAA", end_node_re="ZZZ") -> int:
    num_steps: int = 0

    current_node: Node = nodes[start_node]

    end_node_re = re.compile(end_node_re)

    while end_node_re.match(current_node.name) is None:
        for step in steps:
            if end_node_re.match(current_node.name) is not None:
                break

            num_steps += 1

            if step == "L":
                current_node = nodes[current_node.left]
            else:
                current_node = nodes[current_node.right]

    return num_steps


def main():
    with open("input.txt") as f:
        lines = f.read().splitlines()

    nodes_dict = {}
    for line in lines[2:]:
        node = parse_node(line)
        nodes_dict[node.name] = node

    print(walk_tree(lines[0], nodes_dict))


if __name__ == "__main__":
    main()
