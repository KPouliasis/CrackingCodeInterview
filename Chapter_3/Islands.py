class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        island=0
        dimensiony=len(grid)-1
        print dimensiony
        dimensionx=len(grid[0])-1
        print dimensionx
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    island+=1
                    state=[(i,j)]
                    grid[i][j]='-1'
                    while  state:
                        new_st=[]
                        for el in state:
                            (l,c)=el
                            print "calling neighbors of ",l,c
                            print "in", grid
                            for neighb in list(self.neighbours(l,c,dimensiony,dimensionx,grid)):
                                new_st.append(neighb)
                        state=new_st
                        print "unvisisted neighbours are", state
                        #print state
        return island



    def neighbours(self,i,j,m,n,grid):
        neighbs=[]
        if i>0 :
            if grid[i-1][j]=='1':
                grid[i-i][j]='-1'
                neighbs.append((i-1,j))
        if i<m and grid[i+1][j]=='1' :
            grid[i+1][j]='-1'
            neighbs.append((i+1,j))
        if j>0 and grid[i][j-1]=='1':
            grid[i][j-1]='-1'
            neighbs.append((i,j-1))
        if j<n and grid[i][j+1]=='1':
            grid[i][j+1]='-1'
            neighbs.append((i,j+1)
        return neighbs
sol=Solution()
grid = [list("10111"),list("10101"),list("11101")]
sol.numIslands(grid)
