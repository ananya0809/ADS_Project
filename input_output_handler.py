from enum import Enum

class FileHandler:

    def __init__(self):
        self.input = open("input_new.txt", "r")
        self.output = open("output.txt", "w+")

    def parseParam(self, line: str):
        openbracket = line.index("(")
        closebracket = line.index(")")
        parameter = line[openbracket+1:closebracket]
        if len(parameter) != 0:
            return [eval(i) for i in parameter.split(",")] 
        else:
            return []

    def parseLine(self, line: str):
        if line.startswith("Insert"):
            return [OperationType.INSERT] + self.parseParam(line)
        if line.startswith("GetNextRide"):
            return [OperationType.GETNEXTRIDE]

    def parseFile(self):
        inputLines = self.input.readlines()
        parseLines = []

        for eachLine in inputLines:
            parseLines.append(self.parseLine(eachLine))
        return parseLines


class OperationType(Enum):

    PRINT_SINGLE = 1
    PRINT_MULTIPLE = 2
    INSERT = 3
    GETNEXTRIDE = 4
    CANCELRIDE = 5
    UPDATETRIP = 6

fileHandling = FileHandler()

fileHandling.parseFile()

