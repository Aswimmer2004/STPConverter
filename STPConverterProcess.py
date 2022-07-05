#Item Class
class Item:
    def __init__(self):
        self.name = ""
        self.variables = []
        self.lists = {}
        self.broadcasts = {}
        self.blocks = []
        self.comments = {}
        self.currentCostume = 0
        self.costumes = {}
        self.sounds = {}
        self.blockDict = {}

    def sifter(self, leftovers):
        leftoversCopy = []
        if len(leftovers) == 0:
            return None
        else:
            for i in self.blockDict:
                for j in leftovers:
                    if (self.blockDict[i][len(self.blockDict[i]) - 1].name == j.parentBlock):
                        self.blockDict[i].append(j)
                    else:
                        leftoversCopy.append(j)
        return leftoversCopy

    def sortBlocks(self):
        self.listCopy = self.blocks
        self.noStart = []
        self.noStartCopy = []
        self.blockCount = 0

        while len(self.listCopy) > 0:
            for i in self.listCopy:
                if i.parentBlock is None:
                    self.blockDict[self.blockCount] = []
                    self.blockDict[self.blockCount].append(i)
                    self.blockCount += 1
                else:
                    self.noStart.append(i)
                self.listCopy.remove(i)

        print(self.noStart)
        self.noStartCopy = self.sifter(self.noStart)
        print(self.noStartCopy)
        """while True:
            self.noStartCopy = []
            self.noStartCopy = self.sifter(self.noStart)
            self.noStart = None
            self.noStart = self.noStartCopy
            if(self.noStart == None):
                break"""




    def __repr__(self):
        return self.name + " : " + str(self.blockDict) + " Vars: " + str(self.variables)

#Block Class
class Block:
    def __init__(self):
        self.name = ""
        self.opcode = ""
        self.nextBlock = None
        self.parentBlock = None
        self.inputs = {}
        self.fields = {}
        self.shadow = None
        self.topLevel = None
        #self.xPos = 0
        #self.yPos = 0

    def __repr__(self):
        return self.opcode

class Variable:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.value = None

    def __repr__(self):
        return self.name

#Main Class
import json

f = open('obstaclesgame.json')

data = json.load(f)

sprites = []
stages = []

for i in data['targets']:
    blockKeys = i['blocks'].keys()
    varKeys = i['variables'].keys()
    item = Item()
    item.name = i['name']
    for j in blockKeys:
        block = Block()
        block.name = j
        block.opcode = i['blocks'][j]['opcode']
        block.nextBlock = i['blocks'][j]['next']
        block.parentBlock = i['blocks'][j]['parent']
        block.inputs = i['blocks'][j]['inputs']
        block.fields = i['blocks'][j]['fields']
        block.shadow = i['blocks'][j]['shadow']
        block.topLevel = i['blocks'][j]['topLevel']
        #block.xPos = i['blocks'][j]['x']
        #block.yPos = i['blocks'][j]['y']
        item.blocks.append(block)
    for k in varKeys:
        variable = Variable()
        variable.id = k
        variable.name = i['variables'][k][0]
        variable.value = i['variables'][k][1]
        item.variables.append(variable)
    item.sortBlocks()

    if(i['isStage'] == False):
        sprites.append(item)
    else:
        stages.append(item)

print(sprites)
print(stages)

f.close()
