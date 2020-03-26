from utils.utils import euclideanDistance

class Repository:
    """
        fileNameIn - name of the file with the graph
        fileNameOut - name of the file to write
        adjacency - true if the graph is stored as an adjacency matrix
    """
    def __init__(self,fileNameIn,fileNameOut,adjacency):
        self.__fileNameIn = fileNameIn
        self.__fileNameOut = fileNameOut
        self.__graph = []
        self.__noNodes = 0
        if(adjacency):
            self.__readFromFile()
        else:
            self.__readLocationFromFile()
    
    """
        Reads the graph from the given file and stores it
    """
    def __readFromFile(self):
        with open(self.__fileNameIn,"r") as f:
            lines = f.read().splitlines()
            self.__noNodes = int(lines[0])
            for i in range(1,self.__noNodes+1):
                neighbours = []
                for x in lines[i].split(","):
                    neighbours.append(int(x))
                self.__graph.append(neighbours)

    """
        Reads the graph from the given file and stores it
    """
    def __readLocationFromFile(self):
        with open(self.__fileNameIn,"r") as f:
            lines = f.read().splitlines()
        startIndex = 0
        for line in lines:
            if line.startswith("DIMENSION") == True:
                self.__noNodes = int(line.split(" ")[1])
            if line[0].isdigit():
                break
            startIndex += 1
        nodes = []
        for i in range(0,self.__noNodes):
            index = startIndex + i
            x = float(lines[index].split(" ")[1])
            y = float(lines[index].split(" ")[2])
            nodes.append((x,y))
        for firstNode in nodes:
            neighbours = []
            for secondNode in nodes:
                 neighbours.append(euclideanDistance(firstNode,secondNode))
            self.__graph.append(neighbours)
    """
        Writes the path and weight into the fileNameOut
    """
    def writeBest(self,tspPath,tspWeight):
        strTspPath = ""
        for x in tspPath:
            strTspPath += str(x+1) + ","
        with open(self.__fileNameOut,"w") as f:
            f.write(str(self.__noNodes) + "\n")
            f.write(strTspPath[:-1] + "\n")
            f.write(str(tspWeight)+ "\n")

    """
        Returns the stored graph
    """
    def get_graph(self):
        return self.__graph
    
    """
        Returns the no of nodes in the graph
    """
    def get_noNodes(self):
        return self.__noNodes