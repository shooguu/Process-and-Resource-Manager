from .pcb import PCB
from .rcb import RCB

class Process:
    def __init__(self, pcb_num=16, rcb_num=4, rl_num=3):

        self.PCB = [-1 for item in range(pcb_num)]
        self.RCB = [RCB(item) for item in range(rcb_num)]
        self.RL = [[] for i in range(rl_num)]

        self.PCB[0] = PCB()
        self.RL[0] = [0]

        self.pcb_head = 1
        self.running_process = 0


    def create(self, priority_value: int):

        if self.__next_open_process() < 16 and priority_value > 0 and priority_value < 3:
            self.PCB[self.pcb_head] = PCB()
            self.PCB[self.pcb_head].set_priority_value(priority_value)
            self.PCB[self.running_process].add_children(self.pcb_head)
            self.PCB[self.pcb_head].set_parent(self.running_process)
            self.RL[priority_value].append(self.pcb_head)
            self.pcb_head = self.__next_open_process()
            # self.scheduler()
            self.__get_running_process()
            return self.running_process
        else:
            return -1
            

    def destroy(self, process_num: int):

        self.__get_running_process()
        process_destroyed = self.__destroy_helper(process_num)
        if process_destroyed == -1:
            return -1
        self.pcb_head = self.__next_open_process()
        self.__get_running_process()
        return self.running_process


    def request(self, r: int, k: int):
        self.__get_running_process()
        if  r < 4 and \
            self.running_process > 0 and \
            r not in self.PCB[self.running_process].get_resource():
            if self.RCB[r].get_state() >= k and \
               self.RCB[r].get_waitlist() == []:

                self.RCB[r].set_state(self.RCB[r].get_state() - k)
                self.PCB[self.running_process].add_resource((r, k))
                # print(f"resouce {r} allocated")
            else:
                self.PCB[self.running_process].set_state_blocked()
                priority = self.PCB[self.running_process].get_priority_value()
                self.RL[priority].pop(self.RL[priority].index(self.running_process))
                self.RCB[r].add_to_waitlist(self.running_process)
                # print(f"process {self.running_process} blocked")
            self.__get_running_process()
            return self.running_process
        else:
            return -1


    def release(self, r: int, k: int):
        self.__get_running_process()
        if not self.PCB[self.running_process].remove_from_resource((r,k)):
            return -1
        self.RCB[r].set_state(self.RCB[r].get_state() + k)
        while self.RCB[r].get_waitlist() != [] and self.RCB[r].get_state > 0:
            priority = self.PCB[self.RCB[r].get_waitlist()[0]].get_priority_value()
            process_and_unit = self.PCB[self.RCB[r].get_waitlist()[0]]
            if self.RCB[r].get_state() >= k:
                self.RCB[r] -= k
                self.RCB[process_and_unit[1]].add_resource((r, k))
                self.PCB[process_and_unit[1]].set_state_ready()
                self.RCB[r].pop(self.RCB[r].get_waitlist().index(process_and_unit))
                self.RL[self.PCB[process_and_unit[0].get_priority_value()]].append(process_and_unit[0])
            else:
                break
        return self.running_process


    def timeout(self):

        for i in range(len(self.RL) - 1, -1, -1):
            if self.RL[i] != []:
                head = self.RL[i].pop(0)
                self.RL[i].append(head)
                self.running_process = self.RL[i][0]
                # self.scheduler()
                return self.running_process


    def scheduler(self):

        for priority in range(len(self.RL) - 1, -1, -1):
            for process in self.RL[priority]:
                if type(process) == int:
                    print(f"process {process} running")
                    return


    def __destroy_helper(self, process_num: int):

        if (process_num in self.PCB[self.running_process].get_children() or process_num == self.running_process) and process_num != 0:
            children = self.PCB[process_num].get_children()[::]
            num_of_processes = 0
            for child in children:
                num_of_processes += 1
                self.__destroy_rl(child)
                if self.PCB[child].get_children() != []:
                    children.extend(self.PCB[child].get_children())
                self.PCB[child] = -1
            if process_num > 0:
                priority = self.PCB[process_num].get_priority_value()
                self.RL[priority].pop(self.RL[priority].index(process_num))
                self.PCB[process_num] = -1
                num_of_processes += 1
            return num_of_processes
        else:
            return -1


    def __destroy_rl(self, process_num: int):
        priority = self.PCB[process_num].get_priority_value()
        for index in range(len(self.RL[priority])):
            if self.RL[priority][index] == process_num:
                self.RL[priority].pop(index)
                return


    def __next_open_process(self) -> int:
        '''
        This find the next available process number
        '''
        for item in range(len(self.PCB)):
            if self.PCB[item] == -1:
                self.pcb_head = item
                return item
        return 16

    
    def __get_running_process(self) -> None:

        for priority in range(len(self.RL) - 1, -1, -1):
            for process in self.RL[priority]:
                if type(process) == int:
                    self.running_process = process
                    return



if __name__ == "__main__":
    p = Process(16, 4, 3)
    p.create()
    p.timeout()
    p.create()
    p.timeout()
    p.timeout()
    p.create()
    p.timeout()
    p.timeout()
    p.timeout()
    p.create()
    print(p.PCB)
    print(p.RCB)
    print(p.RL)
    p.destroy(1)
    print(p.PCB)
    print(p.RCB)
    print(p.RL)