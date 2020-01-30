from .pcb import PCB
from .rcb import RCB

class Process:
    def __init__(self, pcb_num: int, rcb_num: int, rl_num: int):
        self._max_pcb_num = pcb_num

        self.PCB = [-1 for item in range(pcb_num)]
        self.RCB = [-1 for item in range(rcb_num)]
        self.RL  = [-1 for item in range(rl_num)]

        self.PCB[0] = PCB()
        self.RCB[0] = RCB()
        self.RL[0] = RL(0)
        
        self.pcb_head = 1
        self.rl_head = 0


    def create(self, priority_value: int):

        self.PCB[self.pcb_head] = PCB()
        self.PCB[self.rl_head].add_children(self.pcb_head)
        self.PCB[self.pcb_head].set_parent(self.rl_head)
        self.PCB[self.pcb_head].set_priority_value(priority_value)
        self.RL[self.rl_head] = self.pcb_head
        self.__print_proess_created()
        self.__next_open_process(self.pcb_head)


    def destroy(self, process_num: int):
        if self.pcb_head <= process_num or process_num == 0:
            print("error")
        else:
            self.PCB[process_num].destroy_children()
            self.PCB[process_num].parent = None
            # self.__destroy_rl(process_num)
            self.PCB[process_num].resources = []
            self.PCB[process_num] = -1
            self.pcb_head -= 1
            self.__next_open_process(process_num)
            self.__print_process_destroyed(100)


    def __print_proess_created(self) -> None:
        '''
        Print to stdout the process number that was just created
        '''
        print(f"process {self.pcb_head} created")

    
    def __print_process_destroyed(self, num_of_processes: int) -> None:
        '''
        Print to stdout the number of processes that was destroyed
        '''
        print(f"{num_of_processes} processes destroyed")


    def __destroy_rl(self, process_num: int):
        for index in range(len(self.RL)):
            if self.RL[index] == process_num:
                self.RL.pop(process_num)
                return

    def __next_open_process(self, process_num: int) -> None:
        '''
        This find the next available process number
        '''
        for item in range(process_num, self._max_pcb_num):
            if self.PCB[item] == -1:
                self.pcb_head = item
                return
        ####### DEBUG #########
        print("All 16 processes are currently in use")

class RL:
    def __init__(self, process_num: int):
        self.process = [process_num]


if __name__ == "__main__":
    p = Process(16, 4, 3)
    p.create(0)
    p.destroy(1)