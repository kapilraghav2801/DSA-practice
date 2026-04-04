class Solution:
    def maxScore(self, cards: List[int], k: int) -> int:
        n = len(cards)
        total = sum(cards)

        if k == n:
            return total 
        i = 0
        j = 0
        result = float('inf')      # fix 1: '-inf' → 'inf'
        curr_sum = 0
        window = n - k

        while j < n:
            curr_sum += cards[j]

            if j - i + 1 < window:
                j += 1

            elif j - i + 1 == window:
                result = min(result, curr_sum)   # fix 2: max → min
                curr_sum -= cards[i]

                i += 1
                j += 1

        return total - result      # fix 3: result → total - result

def maxScore(self, cardPoints: List[int], k: int) -> int:
        max_score = score = sum(cardPoints[-k:])
        n = len(cardPoints)

        left = 0
        for right in range(n - k, n):
            score += cardPoints[left] - cardPoints[right]
            left += 1
            max_score = max(max_score, score)
        
        return max_score
