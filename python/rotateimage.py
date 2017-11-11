a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
	 
def rotateImage(a):
    rotatedImage = []
    row = []
    
    for i in range(len(a)):
        #print (a[i][0])
        row.insert(0,a[i][0])
        print (row)
        
    rotatedImage.append(row)
    print (rotatedImage)
    row = []
    
    for i in range(len(a)):
        print (a[i][1])
        row.insert(0, a[i][1])
        #print (row)
        
    rotatedImage.append(row)
    #print (rotatedImage)
    row = []
    
    for i in range(len(a)):
        #print (a[i][2])
        row.insert(0, a[i][2])
        #print (row)
    
    rotatedImage.append(row)
    print (rotatedImage)
    
#rotateImage(a)

b = [[1]]

def rotateImageV2(a):
    rotatedImage = []
    
    for i in range(len(a)):
        row = []
        for j in range(len(a)):
            print (a[i][j])
            row.insert(0, a[j][i])
        rotatedImage.append(row)
    print (rotatedImage)
            
rotateImageV2(a)