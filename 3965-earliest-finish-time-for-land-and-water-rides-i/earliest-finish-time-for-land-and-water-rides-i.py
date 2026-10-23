class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')

        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):

                # Land -> Water
                finish_land = landStartTime[i] + landDuration[i]
                finish_both = max(finish_land, waterStartTime[j]) + waterDuration[j]
                ans = min(ans, finish_both)

                # Water -> Land
                finish_water = waterStartTime[j] + waterDuration[j]
                finish_both = max(finish_water, landStartTime[i]) + landDuration[i]
                ans = min(ans, finish_both)

        return ans