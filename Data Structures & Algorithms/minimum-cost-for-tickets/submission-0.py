class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel_days = set(days)
        dp = [0] * 366  # dp[d] = min cost through day d
        
        for d in range(1, 366):
            if d not in travel_days:
                dp[d] = dp[d - 1]  # no travel, no new cost
            else:
                dp[d] = min(
                    dp[max(0, d - 1)]  + costs[0],  # 1-day pass
                    dp[max(0, d - 7)]  + costs[1],  # 7-day pass
                    dp[max(0, d - 30)] + costs[2],  # 30-day pass
                )
        
        return dp[365]