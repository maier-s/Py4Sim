import matlab.engine
import os
class Simulink_XML_Exporter:
    matlab_engine = None
    def __int__(self):
        if self.connectToMatlab():
            print(f'SUCESS: Connection to Matlab established')
        else:
            print(f'ERROR: Failed to execute connectioToMatlab function')
    def connectToMatlab(self):
        try:
            self.matlab_engine = matlab.engine.start_matlab()
            return True
        except:
            print(f'ERROR: Somthing went wrong during Py4Sim tried to connect to Matlab')
            return False
    def exportModell(self,mdl_name:str=None,mdl_path:str=None):
        if mdl_name == None or mdl_path == None :
            print("ERROR: At least one parameter is None")
            return False

        try:
            os.chdir(mdl_path)
            #self.matlab_engine.open_system(mdl_name,nargout=0)
            #self.matlab_engine.save_system(mdl_name,f'{mdl_name}.xml','ExportToXML','true')
            return True
        except:
            print("ERROR: Something went wrong with exporting the model")
            return False
if __name__ == '__main__':
    test = Simulink_XML_Exporter()
    test.exportModell("Test","D:\\Stefa\\Stream\\Py4Sim\\test\\")

