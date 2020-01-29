class PCB:
    def __init__(self):
        # 1 - Ready State, 0 - Blocked State
        self.state = 1

        # Parent should be initialized as None
        self.parent = None

        # Child should be initialized as an empty Linked List (Array)
        self.children = []

        # Resource should be initialized as an empty Linked List (Array)
        self.resources = []

        self.priority = 0
        

    def destroy_children(self):
        '''
        Recursively destroys all the children
        '''
        if len(self.children) == 0:
            return
        else:
            self.children.pop()
            self.destroy_children()

    def set_state_ready(self) -> None:
        '''
        Sets the PCB process state to ready (1)
        '''
        self.state = 1

    def set_state_blocked(self) -> None:
        '''
        Sets the PCB process state to blocked (0)
        '''
        self.state = 0

if __name__ == "__main__":
    p = PCB()