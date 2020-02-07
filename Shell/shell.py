from Process.process import Process

class Shell:
    def __init__(self):
        self.process = None

    def run_shell(self):
        
        while (1):
            user_input = input()
            user_input = user_input.strip().split()
            if len(user_input) == 1:
                if user_input[0].lower() == "to" and self.process != None:
                    print(self.process.timeout(), end=" ")
                elif user_input[0].lower() == "in":
                    self.process = Process()
                    print(self.process.running_process, end=" ")
                ################    DEBUG   ##################
                elif user_input[0].lower() == "q":
                    return
                ##############################################
                else:
                    print(-1, end=" ")
            elif len(user_input) == 2:
                try:
                    num = int(user_input[1])
                except ValueError:
                    print(-1, end=" ")
                    continue
                if user_input[0].lower() == "cr" and self.process != None:
                    print(self.process.create(num), end=" ")
                elif user_input[0].lower() == "de" and self.process != None:
                    print(self.process.destroy(num), end=" ")
                else:
                    print(-1, end=" ")
            elif len(user_input) == 3:
                try:
                    num1 = int(user_input[1])
                    num2 = int(user_input[2])
                except ValueError:
                    print(-1, end=" ")
                    continue
                if user_input[0].lower() == "rq" and self.process != None:
                    print(self.process.request(num1, num2), end=" ")
                elif user_input[0].lower() == "rl" and self.process != None:
                    print(self.process.release(num1, num2), end=" ")
                else:
                    print(-1)
            else:
                print(-1)

if __name__ == "__main__":
    s = Shell()
    s.run_shell()