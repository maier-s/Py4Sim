import xml.etree.ElementTree as ET

class XML_Parser:
    def __init__(self):
        pass

    def convert_xml(self,file_path:str = None):
        self.xml_data = ET.parse(file_path)
        self.root_data = self.xml_data.getroot()
    def get_system_data(self):
        self.system_block_data = self.root_data.findall("./Model/System/Block")
        self.system_line_data = self.root_data.findall("./Model/System/Line")
    def element_hasChild(self,element:ET.Element):
        if len(element):
            return True
        return False

if __name__ == '__main__':
    print("XML_parser")
    test = XML_Parser()
    test.convert_xml("..\\test\\Test_XML.xml")
    test.get_system_data()

