class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # result = []
        # for i in range (len(accounts)):
        #     add = sum(accounts[i])
        #     result.append(add)

        # maximum = max(result)
        # return maximum

        # Solution # 02

        wealth = sum(accounts[0])
        for i in range(1 , len(accounts)):
            add = sum(accounts[i])
            if add > wealth:
                wealth = add
        return wealth
