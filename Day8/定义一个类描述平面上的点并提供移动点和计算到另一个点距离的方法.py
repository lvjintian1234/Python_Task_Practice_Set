class Dot():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def move(self,a,b):
        c=self.x+a
        d=self.y+b
        distance = ((c-self.x)**2+(d-self.y)**2)**0.5
        return distance

def main():
    dot=Dot(0,0)
    print(dot.move(3,4))


if __name__=='__main__':
    main()
