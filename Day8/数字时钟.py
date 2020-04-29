from time import sleep

class Clock():
    def __init__(self, second=0, minute=0, hour=0):
        self.second=second
        self.minute=minute
        self.hour=hour

    def run(self):
        self.second+=1
        if self.second==60:
            self.second=0
            self.minute+=1
            if self.minute==60:
                self.minute=0
                self.hour+=1
                if self.hour==24:
                    self.hour=0

    def show(self):
        return '%d:%d:%d' % (self.hour, self.minute, self.second)

def main():
    time = Clock(30,20,10)
    while True:
        time.run()
        sleep(1)
        print(time.show())

if __name__=='__main__':
    main()
