def count_islands(st):
    circles=0
    for i in range(len(st)):
        if st[i][i]:
            consume_neighborhood(st,i)
            circles+=1
    return circles



def consume_neighborhood(st,num):
    stack=[num]
    circle=[]
    while stack:
        cur=stack.pop()
        #print cur
        circle.append(cur)
        if st[cur][cur]:
            for index,friend in enumerate(st[cur]):
                if friend and index!=cur:
                    stack.append(index)
                    st[cur][index]=0
                    st[index][cur]=0
            st[cur][cur]=0
    return circle



neighbors=[[1,1,0,0],[1,1,1,0],[0,1,1,0],[0,0,0,1]]

print consume_neighborhood(neighbors,3)
print count_islands(neighbors)