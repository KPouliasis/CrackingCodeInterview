def merge(arrayA,arrayB,ocup_A,ocup_B):
    i=ocup_A-1
    j=ocup_B-1
    cur= ocup_A  + ocup_B -1
    while cur>=0:
        if i>=0 and j>=0:
            if arrayA[i]>arrayB[j]:
                arrayA[cur]=arrayA[i]
                i-=1
            else:
                arrayA[cur]=arrayB[j]
                j-=1
        else:
            if i<0:
                arrayA[cur]=arrayB[j]
                j-=1
            elif j<0:

                break

        cur-=1
    return arrayA

print merge([1,2,3,4,5,89,90,107,-1,-1,-1,-1],[56, 91,888,1000],8,4)