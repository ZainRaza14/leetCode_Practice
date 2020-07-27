class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        temp1 = []
        lenPushed = len(pushed)
        tempFlag = 0
        for i in pushed:
            temp1.append(i)
            while temp1 and tempFlag < len(popped) and temp1[-1]==popped[tempFlag]:
                temp1.pop()
                tempFlag += 1
                
        return tempFlag == len(popped)
            
            