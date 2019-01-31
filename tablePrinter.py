tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def findLongestString(table):
    colWidth = [0] * len(table)
    cols = len(table[0])
    rows = len(table)
    
    for x in range(rows):
        for y in range(cols):
            if colWidth[x] < len(table[x][y]):
                    colWidth[x] = len(table[x][y])
    return colWidth
            
def printTableJustifiedToLongestStringInRow(table):
    cols = len(tableData[0])
    rows = len(tableData)
    colWidths = findLongestString(tableData)

    for x in range(cols):
        for y in range(rows):
            print((table[y][x]).rjust(colWidths[y]), end = ' ')
        print()
    
printTableJustifiedToLongestStringInRow(tableData)

def findLongestString(table):
    colsWidth = [0] *len(table)
    cols = len(table[0])
    rows = len(table)

    for x in range(cols):
        for y in range(rows):
            if colsWidth[y] < len(table[y][x]):
                colsWidth[y] = len(table[y][x])
    return colsWidth

def printTable(table):
    colsWidth = findLongestString(tableData)
    rows = len(table)
    cols = len(table[0])

    for x in range(cols):
        for y in range(rows):
            print((table[x][y]).rjust(colsWidth[y]))
        print()
    



















        
