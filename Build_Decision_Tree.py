import InfoGain as ig

class Build:
    def __init__(self,rows,bestAttr,bestVal):
        self.data = rows
        self.attr, self.value = bestAttr, bestVal
        self.left, self.right = None, None


def Split(attr,value,dataset):
    left, right = list(), list()
    for row in dataset:
        if float(row[attr]) < float(value):
            left.append(row)
        else:
            right.append(row)
    return left, right



def getColNum(singlerow):
    num_col = 0
    for col in singlerow:
        num_col+=1
    return num_col


def selectBestAttr(dataset,nClass):
    best_IG = 0.0
    best_val = 0.0
    best_attr = 0
    info_gain = 0
    n_of_Attr = getColNum(dataset[0])
    for row in dataset:
        for col in range(1, n_of_Attr):
            left, right = Split(col,row[col],dataset)
            info_gain = ig.Calculate_IG(dataset, left, right,nClass)
            if info_gain>best_IG:
                best_IG = info_gain
                best_val = row[col]
                best_attr = col
    return best_attr, best_val



def buildTree(dataset,nOfClass):

    bestAttribute, bestValue = selectBestAttr(dataset, nOfClass)
    left, right = Split(bestAttribute, bestValue, dataset)
    leftChild = Build(left, 0, 0.0)
    rightChild = Build(right, 0, 0.0)
    if ig.entropy(left,nOfClass)!=0 and ig.get_total_rows(left)>1:
        leftChild = buildTree(left, nOfClass)
    if ig.entropy(right,nOfClass)!=0 and ig.get_total_rows(right)>1:
        rightChild = buildTree(right,nOfClass)

    node = Build(dataset, bestAttribute, bestValue)
    node.left = leftChild
    node.right = rightChild
    return node
