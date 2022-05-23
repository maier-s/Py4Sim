import matlab.engine
import os

class Simulink_Exporter:
    def __init__(self):
        self.eng = matlab.engine.start_matlab()
        pass

    def export_XML_from_model(self,mdl_path:str=None,mdl_name:str=None):
        if mdl_path != None and mdl_name != None:
            print("Doing something")
            print(self.eng.sqrt(4.0,nargout=1))
            os.chdir(mdl_path)
            print(os.getcwd())
            self.eng.eval(f'load_system(Test)',nargout=0)
            #self.eng.save_system(mdl_name,f'{mdl_name}.xml','ExportToXML','true',nargout=1)
            return True


        print("Something went wrong")
        return False

if __name__ == '__main__':
    Test = Simulink_Exporter()
