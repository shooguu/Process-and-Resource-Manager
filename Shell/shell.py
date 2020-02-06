from Process.process import Process

class Shell:
    def __init__(self):
        self.process = None

    def run_shell(self):
        
        while (1):
            user_input = input("> ")
            user_input = user_input.strip().split()
            if len(user_input) == 1:
                if user_input[0].lower() == "cr" and self.process != None:
                    print("create")
                    self.process.create()
                elif user_input[0].lower() == "to" and self.process != None:
                    print("timeout")
                    self.process.timeout()
                elif user_input[0].lower() == "in":
                    print("init")
                    self.process = Process()
                ################    DEBUG   ##################
                elif user_input[0].lower() == "q":
                    return
                ##############################################
                else:
                    print("* error")
            elif len(user_input) == 2:
                try:
                    num = int(user_input[1])
                except ValueError:
                    print("* error")
                    continue
                
                if user_input[0].lower() == "de" and self.process != None:
                    print(f"destroy {num}")
                    self.process.destroy(num)
                elif user_input[0].lower() == "rq" and self.process != None:
                    print(f"request {num}")
                    self.process.request(num)
                elif user_input[0].lower() == "rl" and self.process != None:
                    print(f"release {num}")
                    self.process.release(num)
                else:
                    print("* error")
            else:
                print("* error")

if __name__ == "__main__":
    s = Shell()
    s.run_shell()