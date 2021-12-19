

"""

Prescision True positive / (true positive + false positive)

Recall   true ppositive / (true positive + false negative)


F1    2 * ((precision * recall) / (precision + recall))

"""

def precision(TP, FP):
    return TP / (TP + FP)

def recall(TP, FN):
    return TP / (TP + FN)

def F1(TP, FP, FN):
    return 2 * ((precision(TP, FP) * recall(TP, FN))/(precision(TP, FP) + recall(TP, FN)))


def mAP():
    return

def bAP():
    return

def Mean_IoU():
    return


def pixel_accuracy(input,target):
        '''
        :param input: [b,h,w]
        :param target: [b,h,w]
        :param classNum: scalar
        :return:
        '''
    tmp = input == target
     
    return (torch.sum(tmp).float() / input.nelement())


def Iou(input,target,classNum):
    '''
    :param input: [b,h,w]
    :param target: [b,h,w]
    :param classNum: scalar
    :return:
    '''
    inputTmp = torch.zeros([input.shape[0],classNum,input.shape[1],input.shape[2]])#Create a 0 matrix of size [b,c,h,w]
         targetTmp = torch.zeros([target.shape[0],classNum,target.shape[1],target.shape[2]])# Same as above
         input = input.unsqueeze(1)#Expand the input dimension to [b,1,h,w]
         target = target.unsqueeze(1)# Same as above
         inputOht = inputTmp.scatter_(index=input,dim=1,value=1)#input as the index, convert the 0 matrix to onehot matrix
         targetOht = targetTmp.scatter_(index=target,dim=1,value=1)# Same as above
         batchMious = []#Store a miou for each image in the batch
         mul = inputOht * targetOht#After the multiplication calculation, the number of 1 is intersection
         for i in range(input.shape[0]):#traversal image
        ious = []
                 for j in range(classNum):#traverse categories, including background
            intersection = torch.sum(mul[i][j])
            union = torch.sum(inputOht[i][j]) + torch.sum(targetOht[i][j]) - intersection + 1e-6
            iou = intersection / union
            ious.append(iou)
                 miou = np.mean(ious)#Calculate the miou of the image
        batchMious.append(miou)
    return batchMious
