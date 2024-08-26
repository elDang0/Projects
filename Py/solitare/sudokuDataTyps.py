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
    def valNumb(number,sqr):
        tempArrX = []
        tempArrY = []
        for sqre in grid.arr[sqr.Y]:
            if sqre != None:
                tempArrX.append(sqre.numb)
        for sqrArr in grid.arr:
            if sqr != None:
                tempArrY.append(sqrArr[sqr.X].numb)
        if Helper.numbInArr(tempArrY,number) and Helper.numbInArr(tempArrX,number): sqr.numb = number
        boxStartRow = sqr.Y - (sqr.Y % 3) 
        boxStartCol = sqr.X - (sqr.X % 3)

class square:
    numb = None(int)
    X = None
    Y = None 

