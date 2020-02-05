from .pcb import PCB
from .rcb import RCB

class Process:
    def __init__(self, pcb_num=16, rcb_num=4, rl_num=3):

        self._max_pcb_num = pcb_num

        self.PCB = [-1 for item in range(pcb_num)]
        self.RCB = [-1 for item in range(rcb_num)]
        self.RL  = [-1 for item in range(rl_num)]

        self.PCB[0] = PCB()
        self.RCB[0] = RCB()
        self.RL[0] = RL(0)

        self.pcb_head = 1
        self.rl_head = 0
        self.running_process = 0


    def create(self): #, priority_value: int):

        self.PCB[self.pcb_head] = PCB()
        self.PCB[self.running_process].add_children(self.pcb_head)
        self.PCB[self.pcb_head].set_parent(self.running_process)
        self.RL[self.rl_head] = self.pcb_head
        print(f"process {self.pcb_head} created")
        self.pcb_head = self.__next_open_process(0)


    def destroy(self, process_num: int):

        if self.pcb_head <= process_num or process_num == 0:
            print("error")
        else:
            self.PCB[process_num].destroy_children()
            self.PCB[process_num].parent = None
            # self.__destroy_rl(process_num)
            self.PCB[process_num].resources = []
            self.PCB[process_num] = -1
            self.pcb_head = self.__next_open_process()
            print(f"{num_of_processes} processes destroyed")


    def request(self, r: int):

        if self.RCB[r].get_state() == 1:
            self.RCB[r].set_state_allocated()
            self.PCB[self.running_process].add_resource(r)
            print(f"resouce {r} allocated")
        else:
            self.PCB[self.running_process].set_state_blocked()
            self.RL.pop()
            self.RCB[r].add_to_waitlist(self.running_process)
            print(f"process {self.running_process} blocked")
            

    def __destroy_rl(self, process_num: int):
        for index in range(len(self.RL)):
            if self.RL[index] == process_num:
                self.RL.pop(process_num)
                return


    def __next_open_process(self, process_num: int) -> None:
        '''
        This find the next available process number
        '''
        for item in range(self._max_pcb_num):
            if self.PCB[item] == -1:
                return item

        #######     DEBUG    #########
        print("All 16 processes are currently in use")
        return -1



class RL:
    def __init__(self, process_num: int):
        self.process = process_num


if __name__ == "__main__":
    p = Process(16, 4, 3)
    p.create(0)
    p.destroy(1)