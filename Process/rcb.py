class RCB:
    def __init__(self):
        # 1 - Free, 0 - Allocated
        self._state = 1

        # Waitlist should be initialized as an empty Linked List (Array)
        self._waitlist = []

    def set_state_free(self) -> None:
        '''
        Sets the RCB state to Free (1)
        '''
        self._state = 1

    def set_state_allocated(self) -> None:
        '''
        Sets the RCB state to allocated (0)
        '''
        self._state = 0

    def get_state(self) -> int:
        '''
        Returns the current state of RCB
        '''
        return self._state

    def add_to_waitlist(self, process_num: int) -> None:
        ''' 
        Adds a process number to the waitlist
        '''
        self._waitlist.append(process_num)

    def get_waitlist(self) -> [int]:
        '''
        Returns the waitlist
        '''
        return self._waitlist