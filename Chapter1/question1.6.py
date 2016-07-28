def rotate_image(img):
    for i in range(len(img)/2):
        side_length=len(img[i])/2**(i)
        for j in range(i,i+side_length-1):
            #pairs : (i,j),(j,i+side_length-1),(i+side_length-1,-1-j )(-1-j,i)

            temp=img[j][i+side_length-1]
            img[j][i+side_length-1]= img[i][j]
            img[i+side_length-1][-1-j],temp=temp,img[i+side_length-1][-1-j]
            img[-1-j][i],temp=temp,img[-1-j][i]
            img[i][j]=temp
    return img

print rotate_image([[1,2,3],[4,5,6],[7,8,9]])

