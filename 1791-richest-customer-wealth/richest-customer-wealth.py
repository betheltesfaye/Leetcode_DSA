class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # Use a generator expression to sum each customer's wealth
        # and find the maximum total using the built-in max() function.
        return max(sum(customer) for customer in accounts)