''' ##################################################
    This script creates the map sheet overview for the K 5000 of Berlin in Soldner coordinate system    
    ##################################################    
'''

''' open csv file '''
txtFile = open('2015-07-16-k4-uebersicht.csv', 'w')

''' List of map sheet endings '''
abcd = ['_A', '_B', '_C', '_D']

''' write the header line '''
txtFile.write('%s;%s\n'%('kb', 'geom_3068'))

''' class for create map sheets in right order: XXX_A , XXX_B, XXX_C, XXX_D '''
def writePolygon(this, kb):
    #kb      = 0
    left    = 0
    right   = 0
    top     = 0
    bottom  = 0
    for sheet in this:
        if '_A' == sheet: 
            left = center_x - 3200
            bottom = center_y + 2400
        if '_B' == sheet: 
            left = center_x + 3200
            bottom = center_y + 2400
        if '_C' == sheet: 
            left = center_x - 3200
            bottom = center_y - 2400
        if '_D' == sheet: 
            left = center_x + 3200
            bottom = center_y - 2400
        right = center_x
        top = center_y    
        polygon = '%s;POLYGON((%s %s, %s %s, %s %s, %s %s, %s %s))\n'%(str(kb) + sheet, left, top, right, top, right, bottom,left, bottom, left, top)
        txtFile.write(polygon)
    
''' 1: create north east map sheets '''
minimum = 101
maximum = 102
center_x = 40000 + 3200
center_y = 10000 + 2400
while 1 < 2:
    print minimum, maximum
    for kbNumber in range(minimum,maximum + 1):
        print kbNumber
        writePolygon(abcd, kbNumber)
        center_x += (3200 * 2)
        
    center_y += (2400 * 2)
    center_x = 40000 + 3200
    minimum += 10
    maximum += 10
    if maximum > 122:
        break 
''' 2: create south east map sheets '''    
minimum = 201
maximum = 202
center_x = 40000 + 3200
center_y = 10000 - 2400
while 1 < 2:
    print minimum, maximum
    for kbNumber in range(minimum,maximum + 1):
        print kbNumber
        writePolygon(abcd, kbNumber)
        center_x += (3200 * 2)
        
    center_y -= (2400 * 2)
    center_x = 40000 + 3200
    minimum += 10
    maximum += 10
    if maximum > 212:
        break    
''' 3: create south west map sheets '''
minimum = 301
maximum = 306
center_x = 40000 - 3200
center_y = 10000 - 2400
while 1 < 2:
    print minimum, maximum
    for kbNumber in range(minimum,maximum + 1):
        print kbNumber
        writePolygon(abcd, kbNumber)
        center_x -= (3200 * 2)
        
    center_y -= (2400 * 2)
    center_x = 40000 - 3200
    minimum += 10
    maximum += 10
    if maximum > 316:
        break    
''' 4: create north west map sheets '''    
minimum = 401
maximum = 406
center_x = 40000 - 3200
center_y = 10000 + 2400
while 1 < 2:
    print minimum, maximum
    for kbNumber in range(minimum,maximum + 1):
        print kbNumber
        writePolygon(abcd, kbNumber)
        center_x -= (3200 * 2)
        
    center_y += (2400 * 2)
    center_x = 40000 - 3200
    minimum += 10
    maximum += 10
    if maximum > 456:
        break
''' close csv file '''
txtFile.close()