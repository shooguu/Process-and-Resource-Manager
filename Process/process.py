class Process:
    def __init__(self, pcb_num: int, rcb_num: int, rl_num: int):
        self.PCB = [-1 for item in range(pcb_num)]
        self.RCB = [-1 for item in range(rcb_num)]
        self.RL  = [-1 for item in range(rl_num)]

        self.__init_pcb()
        self.__init_rcb()
        
        self.pcb_head = 1
        self.rl_head = 0

    def __init_pcb(self):
        self.PCB[0] = PCB()

    def __init_rcb(self):
        self.RCB[0] = RCB()

    def create(self):
        self.PCB[self.pcb_head] = PCB()
        # self.PCB[self.pcb_head].parent = 
        self.PCB[self.pcb_head].children.append(self.pcb_head)
        self.RL[self.rl_head] = self.pcb_head
        self.pcb_head += 1
        print(f"process {self.rl_head} created")

    def destroy(self, process_num: int):
        if self.pcb_head < process_num:
            print("error")
        else:
            # Recursively Destroy the children
            self.__destroy_pcb_children(process_num)

            # Remove process_num from parent's list
            self.PCB[process_num].parent = None

            # Remove process_num from RL
            self.__destroy_rl(process_num)

            # Release all resources from process_num
            self.PCB[process_num].resources = []

            # Free PCB of process_num
            self.PCB[process_num] = -1

    def __destroy_pcb_children(self, process_num: int):
        if len(self.PCB[process_num].children) == 0:
            return 
        else:
            self.PCB[process_num].children.pop()
            self.__destroy_pcb_children(process_num)

    def __destroy_rl(self, process_num: int):
        for index in range(len(self.RL)):
            if self.RL[index] == process_num:
                self.RL.pop(process_num)
                return



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

class RCB:
    def __init__(self):
        # 1 - Free, 0 - Allocated
        self.state = 1

        # Waitlist should be initialized as an empty Linked List (Array)
        self.waitlist = []


if __name__ == "__main__":
    p = Process(16, 4, 3)
    p.create()
    p.destroy(1)
