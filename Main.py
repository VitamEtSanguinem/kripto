import block
def main():
    b = block.Block('0', 'asdafaf', '2314', 'ghfg')
    n = block.generate_nonce()
    nn = block.Block('1', block.genPreBlock(), 'asd', block.compute_proof_of_work('1'))
    print(n)
    print(block.list_of_blocks)
    proof = block.proofOfWork('0')
    print("proof : " + proof)

    comp=block.compute_proof_of_work('0')
    print(comp)

    root=block.generateMerkleTree(block.transactions)
    print(root)

    blk = block.blockChain()
    print(blk)

if __name__ == '__main__':
    main()