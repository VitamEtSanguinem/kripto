import hashlib
import datetime
import os

block_chain = []
list_of_blocks = []
transactions = [
    ["A mined 10 BTC",
     "B mined 10 BTC",
     "C mined 0 BTC",
     "B donated a liver"
     ],

    [
        "A sent B 5 BTC",
        "B sent C 2 BTC",
        "C mined 10 BTC",
        "B mined 10 BTC"
    ],
    [
        "C sent B 0 BTC",
        "A sent C 2 BTC",
        "B mined 10 BTC",
        "A mined 10 BTC"
    ],
[
        "C sent B 0 BTC",
        "A sent C 2 BTC",
        "B mined 10 BTC",
        "A mined 10 BTC"
    ]

]

def blockChain(n):
    for i in range(n):
        tmp =generateMerkleTree(transactions)
        blk = Block(n , genPreBlock(), tmp, compute_proof_of_work(n))
        block_chain.append(blk)
    return block_chain



def hashCurrentMerkleLevel(list):
    out = []
    for i in range(0, len(list), 2):
        tmp = list[i] + list[i + 1]
        out.append(hashlib.sha256(tmp.encode('ascii')).hexdigest())

    return out


# Generate merkle Tree
def generateMerkleTree(transactions):
    joinedList=[]
    for i in (transactions):

        for j in i:
            joinedList.append(j)

    # 1. hash every entry
    for i in range(len(joinedList)):
        joinedList[i] = hashlib.sha256(joinedList[i].encode('ascii')).hexdigest()

    # 2. iteratively merge them

    while (len(joinedList) != 1):
        joinedList = hashCurrentMerkleLevel(joinedList)

    return joinedList[0]

def genPreBlock():
    preBlock = hashlib.sha256(str(list_of_blocks[-1]).encode('ascii')).hexdigest()
    return preBlock



def compute_proof_of_work(num):
    tmp = proofOfWork(num)
    while (tmp[:4] != '0000'):
        tmp = proofOfWork(num)

    return tmp


def proofOfWork(num):
    nonce = generate_nonce()
    pp = hashlib.sha256((currentDatetime() + str(nonce) + str(num) + genPreBlock()).encode('ascii')).hexdigest()
    return pp


def currentDatetime():
    now = datetime.datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S")
    # print("date and time =", dt_string)
    return dt


def generate_nonce(length=4):
    nonce = int.from_bytes(os.urandom(length), byteorder='big')
    return nonce





class Block:

    def __init__(self, num, pre_hash, payload, proof_of_work):
        self.num = num
        self.pre_hash = pre_hash
        self.payload = payload
        self.proof_of_work = proof_of_work
        list_of_blocks.append(self)

    #def __str__(self):
     #   return str(self.num) +" "+ str(self.pre_hash) + " " + str(self.payload)+ " " + str(proofOfWork(self.num))


    def add_first_block(self):
        block = Block('00000000000000000000', transactions[0], proof_of_work=self.proof_of_work())
        list_of_blocks.append(block)

    def __str__(self):
        return str(self.num) + '\n' + str(self.pre_hash) + '\n' + str(self.payload) + '\n' + str(self.proof_of_work)



    # def merkleTree(self):
    #
    #     node_hash = []
    #     for i in range(len(transactions)):
    #         for j in range(len(transactions[i])):
    #             #print(transactions[i])
    #             lhash = hashlib.sha256(transactions[i][j].encode('ascii')).hexdigest()
    #             node_hash.append(lhash)
    #             #print(node_hash)
    #
    #     while (len(node_hash) != 1):
    #
    #         for i in range(len(node_hash), 2):
    #             temp = []
    #             temps = node_hash[i] + node_hash[i + 1]
    #             temp.append(hashlib.sha256(temps[i].encode('ascii')).hexdigest())
    #             node_hash = temp
    #
    #     return node_hash
