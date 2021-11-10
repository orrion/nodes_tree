import random
from typing import Dict, Any

from node_object import Node

node_index = 0  # Using a global index here to be able to add new children to the tree
root_node = Node(node_index)    # First node would our root node without a parent
active_nodes: Dict[int, Node] = {}  # To be able to manipulate nodes during the execution


def generate_random_nodes():
    """
        Generate a random initial tree of nodes.
    """
    global node_index
    active_nodes[node_index] = root_node
    parent_node = root_node
    while node_index < random.randint(6, 10):
        node_index += 1
        node = Node(node_index, parent_node)
        active_nodes[node_index] = node
        # Randomly select a parent for the child node.
        parent_node = active_nodes.get(random.randrange(0, node_index))


def process_node_selection(index: Any) -> Node:
    """
        Validate the given input and check if selected node exists
    :param index: index of the selected node (raw input from the user)
    :type index: Any
    :return: selected node by given index
    :rtype: Node
    """
    try:
        index = int(index.strip())
    except ValueError:
        raise Exception('Not valid node index specified')
    node = active_nodes.get(index)
    if node is None:
        raise Exception('Specified node does not exist')
    return node


if __name__ == '__main__':
    try:
        generate_random_nodes()
        root_node.pretty_print()
        help_msg = '1 (or `help`) - Help\n' \
                   '2 - Change node ready state\n' \
                   '3 - Add new node\n' \
                   '4 - Remove node\n' \
                   '5 - Print nodes tree\n' \
                   '6 - Re-generate nodes tree\n' \
                   '7 - Exit'
        print(help_msg)
        while True:
            command = input('Choose the command: ').strip()
            if command == '1' or command == 'help':
                print(help_msg)
                continue
            elif command == '2':
                try:
                    node_to_change = process_node_selection(input('Please specify the index of the node to change: '))
                except Exception as e:
                    print(e)
                    continue
                # We should not allow to manually change the state of the parent node as then we would have
                # inconsistent children ready states.
                if node_to_change.has_children():
                    print('You cannot change the ready state for the node with children')
                    continue
                node_to_change.set_ready_state(not node_to_change.is_ready())
                print(f'Ready state for node {node_to_change.identifier()} was changed to {node_to_change.is_ready()}')
            elif command == '3':
                try:
                    node_to_change = process_node_selection(
                        input('Please specify to which node you want to add a child: '))
                except Exception as e:
                    print(e)
                    continue
                node_index += 1
                active_nodes[node_index] = Node(node_index, node_to_change)
                print(f'New node {node_index} was added to the selected parent {node_to_change.identifier()}')
            elif command == '4':
                try:
                    node_to_change = process_node_selection(
                        input('Please specify which child node you want to remove: '))
                except Exception as e:
                    print(e)
                    continue
                # Decided to not allow to remove the parent node as it gives an easy way to destroy the entire tree :)
                if node_to_change.has_children():
                    print('You cannot remove the node which has children')
                    continue
                node_to_change.destroy_node()
                del active_nodes[node_to_change.identifier()]
                print(f'Node {node_to_change.identifier()} was removed.')
            elif command == '5':
                root_node.pretty_print()
                continue
            elif command == '6':
                # Just do the reset...
                active_nodes = {}
                node_index = 0
                root_node = Node(node_index)
                generate_random_nodes()
                print('Nodes were re-generated')
            elif command == '7':
                print('Exiting, bye bye :)')
                exit(0)
            else:
                print('Please, provide a valid command (Use the number on the left)')
                print(help_msg)
                continue
            root_node.pretty_print()
            print(help_msg)
    except KeyboardInterrupt:
        # Just to not throw an ugly exception in case of a keyboard interruption.
        print('Exiting, bye bye :)')
        exit(0)
