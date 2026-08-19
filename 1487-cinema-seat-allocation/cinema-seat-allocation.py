class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        blockA = 0b0000011110   # seats 2–5
        blockB = 0b0001111000   # seats 4–7
        blockC = 0b0111100000   # seats 6–9

        # Store reserved seats per row as bitmask
        reserved = defaultdict(int)
        for row, seat in reservedSeats:
            reserved[row] |= 1 << (seat - 1)  # seat 1 → bit 9, seat 10 → bit 0

        result = 0

        # Process rows with reservations
        for row_mask in reserved.values():
            canA = (row_mask & blockA) == 0
            canB = (row_mask & blockB) == 0
            canC = (row_mask & blockC) == 0

            if canA and canC:
                result += 2
            elif canA or canB or canC:
                result += 1
            # else no group fits

        # Rows without reservations → 2 groups each
        result += (n - len(reserved)) * 2

        return result