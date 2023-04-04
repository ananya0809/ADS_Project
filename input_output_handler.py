from enum import Enum

class FileHandler:

    def __init__(self):
        self.input = open("input.txt", "r")
        self.output = open("output.txt", "w+")

    def parseParam(self, line: str):
        openbracket = line.index("(")
        closebracket = line.index(")")
        parameter = line[openbracket+1:closebracket]
        if len(parameter) != 0:
            return parameter.split(",")
        else:
            return []

    def parseLine(self, line: str):
        if line.startswith("Insert"):
            print(self.parseParam(line))

    def parseFile(self):
        inputLines = self.input.readlines()

        for eachLine in inputLines:
            self.parseLine(eachLine)


class OperationType(Enum):

    PRINT_SINGLE = 1
    PRINT_MULTIPLE = 2
    INSERT = 3
    GETNEXTRIDE = 4
    CANCELRIDE = 5
    UPDATETRIP = 6

fileHandling = FileHandler()

fileHandling.parseFile()

