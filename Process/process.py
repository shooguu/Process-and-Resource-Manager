from .pcb import PCB
from .rcb import RCB

class Process:
    def __init__(self, pcb_num=16, rcb_num=4, rl_num=3):

        self._max_pcb_num = pcb_num
        self._max_rl_num = rl_num

        self.PCB = [-1 for item in range(pcb_num)]
        self.RCB = [RCB() for item in range(rcb_num)]
        self.RL = [0]

        self.PCB[0] = PCB()

        self.pcb_head = 1
        self.rl_head = 0
        self.running_process = 0


    def create(self): #, priority_value: int):

        self.PCB[self.pcb_head] = PCB()
        self.PCB[self.running_process].add_children(self.pcb_head)
        self.PCB[self.pcb_head].set_parent(self.running_process)
        self.RL.append(self.pcb_head)
        self.rl_head += 1
        print(f"process {self.pcb_head} created")
        self.pcb_head = self.__next_open_process()
        

    def destroy(self, process_num: int):

        if self.PCB[process_num] == -1:
            print("error")
        else:
            process_destroyed = self.__destroy_pcb_child(process_num)
            if process_num > 0:
                self.PCB[process_num] = -1
                process_destroyed += 1
            self.pcb_head = self.__next_open_process()
            print(f"{process_destroyed} processes destroyed")


    def request(self, r: int):
        if self.running_process != 0:
            if self.RCB[r].get_state() == 1:
                self.RCB[r].set_state_allocated()
                self.PCB[self.running_process].add_resource(r)
                print(f"resouce {r} allocated")
            else:
                self.PCB[self.running_process].set_state_blocked()
                self.RL.pop()
                self.RCB[r].add_to_waitlist(self.running_process)
                print(f"process {self.running_process} blocked")
        else: ###########   DEBUG   ###############
            print(f"DEBUG (request): Requesting a process when current process is {self.running_process}")


    def timeout(self):

        head = self.RL.pop(0)
        self.RL.append(head)
        self.running_process = self.RL[0]
        self.scheduler()


    def scheduler(self):

        print(f"process {self.RL[0]} running")


    def __destroy_pcb_child(self, process_num: int):

        children = self.PCB[process_num].get_children()[::]
        num_of_processes = 0
        for child in children:
            num_of_processes += 1
            if self.PCB[child].get_children() != []:
                children.extend(self.PCB[child].get_children())
            self.PCB[child] = -1
        return num_of_processes


    def __destroy_rl(self, process_num: int):
        for index in range(len(self.RL)):
            if self.RL[index] == process_num:
                self.RL.pop(process_num)
                return


    def __next_open_process(self) -> None:
        '''
        This find the next available process number
        '''
        for item in range(self._max_pcb_num):
            if self.PCB[item] == -1:
                return item

        #######     DEBUG    #########
        print("All 16 processes are currently in use")
        return -1



if __name__ == "__main__":
    p = Process(16, 4, 3)
    p.create(0)
    p.destroy(1)