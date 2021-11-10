# Nodes tree
Simple test application to generate the tree of nodes and manipulate it.
### Requirements
> Python 3.6 or higher (Python 3.10 was used for the implementation)
### How to run it
Execute the `main.py` file :)
```commandline
python3 main.py
```
### Example of the program output:
```commandline
Please specify the index of the node to change: 4
Ready state for node 4 was changed to True
 Node 0 not ready

- Node 1 not ready

-- Node 5 not ready

--- Node 8 not ready

- Node 2 not ready

-- Node 7 not ready

- Node 3 not ready

-- Node 6 not ready

- Node 4 ready

1 (or `help`) - Help
2 - Change node ready state
3 - Add new node
4 - Remove node
5 - Print nodes tree
6 - Re-generate nodes tree
7 - Exit
Choose the command: 7
Exiting, bye bye :)
```
