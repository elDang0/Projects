class grid:
    arr = [ 
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]

class Helper:
    def bubbleSort(arr):
        sorted = False
        i = 0
        while not sorted:
            if i == arr.__len__+1: i = 0
            if arr[i] > arr[i+1] : 
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                i += 1
        return arr
    def numbInArr(arr,numb):
        for x in arr:
            if x.numb == numb: return True
        return False
class square:
    numb = None(int)
    posX = None
    posY = None 

    def valNumb(number,self):
        tempArrX = []
        tempArrY = []
        for sqr in grid.arr[self.posY]:
            if sqr != None:
                tempArrX.append(sqr.numb)
        for sqrArr in grid.arr:
            if sqr != None:
                tempArrY.append(sqrArr[self.posX].numb)
        if Helper.numbInArr(tempArrY,number) and Helper.numbInArr(tempArrX,number): self.numb = number