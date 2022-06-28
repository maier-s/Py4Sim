from Blocks import Block_CG
from math import sin
class Sin(Block_CG.Block_CG):
    def __init__(self):
        super().__init__()
    def codeGen(self):
        print("I am a sine wave")
    def step_func(self,timestamp:float):
        return sin(timestamp)


if __name__ == '__main__':
    test = Sin()
    test.codeGen()
    print(test.step_func(0.05))