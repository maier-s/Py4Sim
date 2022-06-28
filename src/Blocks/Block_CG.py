class Block_CG:
    def __init__(self):
        print("Ja ich bin eine CG Einheit")
    def codeGen(self):
        pass
    def step_func(self,input):
        print(f"I take {input} and returning somthing")
        pass



if __name__ == '__main__':
    print("Direkt ausgeführt")
    test = Block_CG()
    test.step_func("Somthing")