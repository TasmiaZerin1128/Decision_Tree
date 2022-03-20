import math

class_index = 0

def get_total_rows(dataset):
    n_row =0;
    for row in dataset:
        n_row+=1

    return n_row

def get_class_rows(dataset,nClass):
    class_rows = [0]* nClass
    for row in dataset:
        class_rows[int(row[class_index])-1]+=1

    return class_rows


def entropy(dataset,nClass):
    entropy = 0
    totalRows = int(get_total_rows(dataset))
    classRows = get_class_rows(dataset,nClass)
    if totalRows<=0:
        return 0
    for x in classRows:
        prob = float(x/totalRows)
        if(prob>0):
            entropy += (prob * math.log(prob))
    return -entropy


def Calculate_IG(dataset, leftN, rightN, numClass):
    p_entropy = entropy(dataset,numClass)
    left_entropy = entropy(leftN,numClass)
    right_entropy = entropy(rightN,numClass)

    parent_row = get_total_rows(dataset)
    left_row = get_total_rows(leftN)
    right_row = get_total_rows(rightN)

    infoGain = p_entropy - ((left_row/parent_row)*left_entropy + (right_row/parent_row)*right_entropy)
    return infoGain
