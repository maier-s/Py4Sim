import xml.etree.ElementTree as ET

class XML_Parser:
    # Local Variables
    systemBlockData = {}
    systemLineData = {}
    root_data = None
    xml_data = None

    def __init__(self):
        pass

    def convert_xml(self,file_path:str = None):
        self.xml_data = ET.parse(file_path)
        self.root_data = self.xml_data.getroot()
        self.get_system_data()
    def get_system_data(self):
        self.system_block_data = self.root_data.findall("./Model/System/Block")
        for block in self.system_block_data:
            self.systemBlockData[block.attrib["Name"]]={"BlockType":block.attrib["BlockType"]}
        self.system_line_data = self.root_data.findall("./Model/System/Line")
        for idx, line in enumerate(self.system_line_data):
            self.systemLineData[idx]={"SrcBlock":line[1].text,"DstBlock":line[3].text}
    def get_parameter(self,element):
        return element.findall("./P")
    def element_hasChild(self,element:ET.Element):
        if len(element):
            return True
        return False

if __name__ == '__main__':
    print("XML_parser")
    test = XML_Parser()
    test.convert_xml("..\\test\\Test_XML.xml")
    test.get_system_data()
    #print(test.system_block_data)
    print(test.systemBlockData)
    print(test.systemLineData)

