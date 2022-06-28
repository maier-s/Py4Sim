import Graph
from XML_Parser import XML_Parser
from Blocks import P4S_Sin
class Graph_Creator:
    cal_Vertex = {}
    block_factory_dict = {
        "Sin" : P4S_Sin.Sin(),
        "SubSystem": "Graph",
        "Scope": "Scope"
    }
    def __init__(self, path: str):
        self.XML_Parser = XML_Parser()
        self.XML_Parser.convert_xml(path)
        self.calGraph = Graph.Graph()
        self.createVertex()
        self.createEdges()
    def createVertex(self):
        for name,property in self.XML_Parser.systemBlockData.items():
            #print(property)
            new_Vertex = self.calGraph.add_vertex(containter=self.block_factory_dict[property["BlockType"]])
            if(name == "Sine Wave"):
                print(new_Vertex.container.step_func(0.05))
            self.cal_Vertex[name] = new_Vertex
        self.calGraph.print_matrix()
        print(self.cal_Vertex)

    def createEdges(self):
        for line,container in self.XML_Parser.systemLineData.items():
            self.calGraph.add_edge(self.cal_Vertex[container['SrcBlock']],self.cal_Vertex[container['DstBlock']])
            print(f"Line No.{line}\nFrom: {container['SrcBlock']}({self.XML_Parser.systemBlockData[container['SrcBlock']]['BlockType']}) --> To: {container['DstBlock']}({self.XML_Parser.systemBlockData[container['DstBlock']]['BlockType']}) ")
        print(self.calGraph.print_matrix())
if __name__ == '__main__':
    test = Graph_Creator("..\\test\\Test_XML.xml")
