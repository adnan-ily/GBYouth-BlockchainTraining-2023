import hashlib

file = open('lacture_file.pptx', "rb")
content = file.read()

listOfHashes = []

blockSize = len(content) // 1024
dataBlocks = [content[i:i + blockSize] for i in range(0, len(content), blockSize)]


def makeMarkelTreeAndReturnMarkelRoot(data):
    treeHashes = data

    while (len(treeHashes) > 1):
        newHashs = []
        if (len(treeHashes) % 2 != 0):
            treeHashes.append(treeHashes[len(treeHashes) - 1])

        for y in range(0, len(treeHashes), 2):
            firstHash = treeHashes[y]
            secondhash = treeHashes[y + 1]
            concatinatedHashes = firstHash + secondhash
            hashOfConcatinatedHashes = hashlib.sha256(concatinatedHashes.encode()).hexdigest()
            newHashs.append(hashOfConcatinatedHashes)

        treeHashes = newHashs

    return treeHashes[0]





for x in range(len(dataBlocks)):
    stringHash = hashlib.sha256(dataBlocks[x]).hexdigest()
    listOfHashes.append(stringHash)

finalMarkelRoot = makeMarkelTreeAndReturnMarkelRoot(listOfHashes)
print('\n')
print(f"Markel Root is: {finalMarkelRoot}")
print('\n')