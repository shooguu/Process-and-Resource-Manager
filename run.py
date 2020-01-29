from Process.process import Process

if __name__ == "__main__":
    p = Process(16, 4, 3)
    p.create(0)
    p.destroy(1)