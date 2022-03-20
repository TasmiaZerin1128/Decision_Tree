import csv
import random

import easygui

import GetFile as Get
import Build_Decision_Tree as BDT


def printTree(root, height, nodeName):
    print(nodeName, '--Attribute ', root.attr, ', Best Value ', root.value)
    for i in range(height):
        print(end=' ')
    if root.left != None:
        printTree(root.left, height + 1, 'Left')
    if root.right != None:
        printTree(root.right, height + 1, 'Right')





def findClass(root,data):
    if root.attr == 0:
        return root.data[0][0]
    if float(data[root.attr])<float(root.value):
        return findClass(root.left, data)
    else:
        return findClass(root.right, data)


def test(root, testset):
    rightAns, totalTest = 0, 0
    for row in testset:
        cls_of_trainset = findClass(root, row)
        writer.writerow([row[0], cls_of_trainset, cls_of_trainset == row[0]])
        if cls_of_trainset == row[0]:
            rightAns += 1
        totalTest += 1
    return rightAns, totalTest


def divideDataset(start,end,dataset):
    trainset, testset = [], []
    i =0
    for row in dataset:
        if i>=start and i<start+(end/10):
            testset.append(row)
        else:
            trainset.append(row)
        i+=1
    return trainset, testset

def writeOutput(grandAccuracy, grandTotal, msg):
    writer.writerow(['Decision Tree Grand Accuracy=' + str(grandAccuracy) + '%', 'Total Tests:' + str(grandTotal)])
    writer.writerow([])
    easygui.msgbox(msg, 'Testing Complete')
    outputFile.close()
    file.close()


def generateTree():
    grandTotal, grandRightTotal = 0, 0

    for i in range(10):
        writer.writerow(['Run:', i + 1])
        writer.writerow(['expected', 'found', 'correctness'])
        size = len(dataset)
        trainset, testset = divideDataset(i * (size / 10), size, dataset)
        root = BDT.buildTree(trainset, numberOfClass)
        rightAns, total_test = test(root, testset)
        grandTotal += total_test
        grandRightTotal += rightAns
        accuracy = (rightAns / total_test) * 100
        print('Test ' + str(i + 1) + ' Accuracy: ' + str(accuracy))
        writer.writerow(['Accuracy=' + str(accuracy), 'Samples=' + str(total_test)])
        print('Printing Decision Tree for Test', i+1)
        printTree(root,0, 'Root')

    grandAccuracy = (grandRightTotal / grandTotal) * 100
    msg = '\nAccuracy: ' + str(grandAccuracy) + '%\n' + 'Total testset size: ' + str(grandTotal)
    print(msg)
    writeOutput(grandAccuracy, grandTotal, msg)




# Start from here

fileName = Get.getFile()
if(fileName!='none'):
    file = open(fileName)
    csvreader = csv.reader(file)
    dataset = []
    for row in csvreader:
        dataset.append(row)
else:
    print('Error in getting file')
    exit();


saveFileName = 'result.csv'
outputFile = open(saveFileName, 'w', newline='')
writer = csv.writer(outputFile)


numberOfClass = 3

random.shuffle(dataset)

generateTree()

print('Decision Tree successful')