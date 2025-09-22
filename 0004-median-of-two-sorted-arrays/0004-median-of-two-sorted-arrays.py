class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        m, n = len(A), len(B)
        # Ensure A is the smaller array
        if m > n:
            A, B, m, n = B, A, n, m

        lo, hi = 0, m
        half = (m + n + 1) // 2  # left partition size (handles odd total)

        while lo <= hi:
            i = (lo + hi) // 2       # cut in A
            j = half - i             # cut in B

            # A[i] too small -> move right
            if i < m and j > 0 and B[j - 1] > A[i]:
                lo = i + 1
            # A[i-1] too big -> move left
            elif i > 0 and j < n and A[i - 1] > B[j]:
                hi = i - 1
            else:
                # Perfect partition
                if i == 0:
                    maxLeft = B[j - 1]
                elif j == 0:
                    maxLeft = A[i - 1]
                else:
                    maxLeft = max(A[i - 1], B[j - 1])

                # Odd total length: median is left side max
                if (m + n) % 2 == 1:
                    return float(maxLeft)

                if i == m:
                    minRight = B[j]
                elif j == n:
                    minRight = A[i]
                else:
                    minRight = min(A[i], B[j])

                return (maxLeft + minRight) / 2.0
