class PCB:
    def __init__(self, state=1, parent=None, children=[], resouce=[], priority=0):
        # 1 - Ready State, 0 - Blocked State
        self._state = state

        # Parent should be initialized as None
        self._parent = parent

        # Child should be initialized as an empty Linked List (Array)
        self._children = children

        # Resource should be initialized as an empty Linked List (Array)
        self._resources = resouce

        self._priority = priority
        

    def set_state_ready(self) -> None:
        '''
        Sets the PCB process state to ready (1)
        '''
        self._state = 1

    def set_state_blocked(self) -> None:
        '''
        Sets the PCB process state to blocked (0)
        '''
        self._state = 0

    def get_state(self) -> int:
        '''
        Gets the current state
        '''
        return self._state

    def set_parent(self, parent: int) -> None:
        '''
        Sets the current parent with given index
        '''
        self._parent = parent

    def get_parent(self) -> int:
        '''
        Returns the current parent value
        '''
        return self._parent

    def add_children(self, running_index: int):
        '''
        Appends the child with the given index value
        '''
        self._children.append(running_index)

    def get_children(self) -> [int]:
        '''
        Returns the children
        '''
        return self._children

    def destroy_children(self):
        '''
        Recursively destroys all the children
        '''
        if len(self._children) == 0:
            return
        else:
            self._children.pop()
            self.destroy_children()

    def set_priority_value(self, priority_value: int):
        '''
        Sets the current priority value with the given priority value
        '''
        self._priority = priority_value

    def get_priorty_value(self) -> int:
        '''
        Returns the current priorty value
        '''
        return self._priority

if __name__ == "__main__":
    p = PCB()