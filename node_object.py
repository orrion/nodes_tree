from typing import Optional, List


class Node:

    def __init__(self, identifier: int, parent: Optional['Node'] = None):
        self._identifier = identifier
        self._ready = False
        self._parent = parent
        self._child_nodes: List[Node] = []
        if self._parent is not None:
            # Add itself as a child to the parent
            self._parent.add_child(self)

    def identifier(self) -> int:
        # Separate method to return the identifier as maybe we would want to
        # somehow change the processing of the identifier itself without touching the class interface.
        return self._identifier

    def is_ready(self) -> bool:
        return self._ready

    def has_children(self) -> bool:
        return len(self._child_nodes) > 0

    def set_ready_state(self, is_ready: bool):
        # Do the processing only in case state was really changed.
        if self._ready != is_ready:
            self._ready = is_ready
            if self._parent is not None:
                self._parent._check_ready_state()

    def add_child(self, child_node: 'Node'):
        self._child_nodes.append(child_node)
        # New child is always not ready.
        self.set_ready_state(False)

    def _remove_child(self, child_node: 'Node'):
        self._child_nodes.remove(child_node)
        self._check_ready_state()

    def destroy_node(self):
        if self._parent is not None:
            self._parent._remove_child(self)

    def _check_ready_state(self):
        # If there is no children then parent became a simple child and it state should be manually changed.
        if self.has_children():
            for node in self._child_nodes:
                if not node.is_ready():
                    self.set_ready_state(False)
                    return
            self.set_ready_state(True)

    def pretty_print(self, level: int = 0):
        # Print nice, colored hierarchy of nodes tree.
        # If node is not ready it going to be `Red`, otherwise - `Green`
        print(f'{"-" * level} \x1b[6;30;4{"2" if self.is_ready() else "1"}m{self}\x1b[0m\n')
        for child_node in self._child_nodes:
            child_node.pretty_print(level + 1)

    def __repr__(self):
        return f'Node {self._identifier}{"" if self.is_ready() else " not"} ready'
