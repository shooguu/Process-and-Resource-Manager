class PCB:
    def __init__(self):
        # 1 - Ready State, 0 - Blocked State
        self._state = -1

        # Parent should be initialized as None
        self._parent = None

        # Child should be initialized as an empty Linked List (Array)
        self._children = []

        # Resource should be initialized as an empty Linked List (Array)
        self._resources = []

        self._priority = 0
        

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

    def set_priority_value(self, p: int):
        '''
        Sets the priority value to the given value
        '''
        self._priority = p

    def get_priority_value(self) -> int:
        '''
        Returns the current priorty value
        '''
        return self._priority

    def add_resource(self, resource: int) -> None:
        '''
        Appends the resouce with the given resource value
        '''
        self._resources.append(resource)

    def get_resource(self) -> int:
        '''
        Returns the resouce list
        '''
        return self._resources

    def remove_from_resource(self, r: int) -> None:

        try:
            self._resources.pop(self._resources.index(r))
            return 1
        except ValueError:
            return 0

if __name__ == "__main__":
    p = PCB()