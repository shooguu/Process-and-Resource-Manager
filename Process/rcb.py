class RCB:
    def __init__(self, units: int):
        # 1 - Free, 0 - Allocated
        self._state = self._init_unit(units)

        # Waitlist should be initialized as an empty Linked List (Array)
        self._waitlist = []

        self.inventory = 0

    def _init_unit(self, unit: int):
        if unit == 0 or unit == 1:
            return 1
        elif unit == 2:
            return 2
        else:
            return 3

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

    def set_state(self, s: int) -> None:

        self._state = s

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

    def remove_from_waitlist(self, r: int) -> None:
        '''
        Removes item from a the waitlist
        '''
        self._waitlist.pop(self._waitlist.index(r))