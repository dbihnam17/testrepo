
import math

def main():
    index = 0

    cellPlatingList = []

    volumeList = []

    cellPlatingList.append(findCellCount(volumeList))
    print()

    keepGoing = input("Are you counting another cell type? [Y] or [N]: ")
    print()

    while( keepGoing == 'Y' or keepGoing == 'y' and index < 1):
        print("I can't plate multiple cell types together yet,")
        print('but I can still count them! Check back later...')
        print()
        cellPlatingList.append(findCellCount(volumeList))
        print()
        index = index + 1

    if (index == 0):
        print('{:,}'.format(cellPlatingList[0]))

    else:
        print(str('{:,}'.format(cellPlatingList[0]))+'  ''{:,}'.format(cellPlatingList[1]))
    
    if(index == 0) :
        print(' Cell 1')
    if(keepGoing == 'Y' or keepGoing == 'y' and index == 1):
        print(' Cell 1     Cell 2')
    
    print()
    
    beginPlating = input('Will you be plating your cells? [Y] or [N]: ')
    print()

    if(beginPlating == 'Y' or beginPlating == 'y'):
        cellsPerWell(volumeList, cellPlatingList)

    else:
        print('Thanks for using the cell counter program!')
    
def findCellCount(volumeList):
    average = int(input('Enter average cell count: '))

    dilution = int(input('Enter dilution factor: '))

    volume = int(input('Enter sample volume [ml]: '))

    volumeList.append(volume)

    multiplicationValue = pow(10, 4)

    divisionValue = pow(10, 6)
    print()

    cellCount = average * dilution * multiplicationValue * volume

    print (str(cellCount/divisionValue) + "*10^6 Total Cells")

    print (str('{:,}'.format(cellCount))+ " Total Cells")

    return cellCount

def cellsPerWell(volumeList, cellPlatingList):

    givenCellCount = cellPlatingList[0]

    numCell0 = int(input('How many cells would you like in each well? : '))
    print()

    while(numCell0 >= cellPlatingList[0]):
        print("Oops! You don't have enough cells for that...")
        numCell0 = int(input('Re-enter a lower amount of cells in each well: '))
        print()
    
    changeVolume = input('Have you changed your sample volume? [Y] or [N]: ')

    if (changeVolume == 'Y' or changeVolume == 'y'):
        plateVol = int(input('Enter new sample volume [mL]: '))
        print()
        result = numCell0 / (givenCellCount / plateVol)
        retVol1 = volumeList[0]

    else:
        retVol0 = volumeList[0]
        print()
        result = numCell0 / (givenCellCount / retVol0)

    if (plateVol == retVol1):
        print('LIAR!')
        print()

    print (str('{:.2f}'.format(result)) + ' mL/well')
    print (str('{:.2f}'.format(result * 1000)) + ' uL/well')
    print()

    quantWells = input('Would you like to know how many wells you can fully fill? [Y] or [N]: ')
    print()

    if (quantWells == 'Y' or quantWells == 'y'):
        lastResult = givenCellCount / numCell0
    
    if(quantWells == 'Y' or quantWells == 'y'):
        print(str(math.floor(lastResult))+' Wells')
        print()
        print('Thanks for using the cell counter program!')

    else:
        print('Thanks for using the cell counter program!')


main ()






    

















