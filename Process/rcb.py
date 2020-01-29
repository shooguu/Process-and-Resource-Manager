class RCB:
    def __init__(self):
        # 1 - Free, 0 - Allocated
        self.state = 1

        # Waitlist should be initialized as an empty Linked List (Array)
        self.waitlist = []

    def set_state_free(self) -> None:
        '''
        Sets the RCB state to Free (1)
        '''
        self.state = 1

    def set_state_allocated(self) -> None:
        '''
        Sets the RCB state to allocated (0)
        '''
        self.state = 0