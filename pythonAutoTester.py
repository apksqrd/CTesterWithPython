# sorry for the messy code, I wrote it mostly on a train ride

import os


def runSingle(path, inPath="test.in", outPath="test.out"):
    if(len(path) > 2):
        if(path[-2:] == ".c"):  # if this isn't compiled already
            # bad when outPath is path but without the .c
            os.system("gcc "+path+" -o "+path[:-2])
            path = path[:-2]
    # \" so that there can be spaces
    os.system("./\""+path+"\" <\""+inPath+"\" >\""+outPath+"\"")


def testSingle(path, inPath="test.in", correctOutPath="test.out",
               outToCheckPath="testCompare.out", blanksMatter=False, printResults=False):
    runSingle(path, inPath, outToCheckPath)
    correctOut = open(correctOutPath, "r").read()
    outToCheck = open(outToCheckPath, "r").read()
    if(not blanksMatter):
        correctOut = correctOut.rstrip(" \n")
        outToCheck = outToCheck.rstrip(" \n")
    if(printResults):
        if(correctOut == outToCheck):
            print("Success")
        else:
            print("Fail")
        print("Expected: "+correctOut)
        print("Returned: "+outToCheck)
    return correctOut == outToCheck


def testMultiple(codePath, ioPathList: list, outToCheckPath="testCompare.out", blanksMatter=False, printResults=True):
    totalSucceed = 0
    totalCount = 0  # isn't rly neccesary # how 2 spell nececarry
    for ioPath in ioPathList:
        print("Testing: "+ioPath[0]+" and "+ioPath[1])
        isWorking = testSingle(
            codePath, *ioPath, outToCheckPath=outToCheckPath, printResults=False)
        if(isWorking):
            print("Success")
            totalSucceed += 1
        else:
            print("Fail on: "+ioPath[0]+" and "+ioPath[1])
            expectedString = open(ioPath[1], "r").read()
            returnedString = open(outToCheckPath, "r").read()
            if(not blanksMatter):
                expectedString = expectedString.rstrip(" \n")
                returnedString = returnedString.rstrip(" \n")
            if(printResults):  # Why can't I name it printResultsOnError?
                pass
            print("Expected: "+returnedString)
            print("Returned: "+returnedString)
        totalCount += 1
    print(totalSucceed, "success out of", totalCount)


if __name__ == "__main__":
    codePath = "JohnHasNoBrown.c"
    ioPathList = [["no cow/"+str(i)+".in", "no cow/"+str(i)+".out"]
                  for i in range(1, 11)]
    testMultiple(codePath, ioPathList)
