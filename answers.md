# CMPS 2200 Assignment 3
## Answers

**Name:**Miles Whiteford


Place all written answers from `assignment-03.md` here for easier grading.

1a) Start with the highest value k in which 2^k <= N. Then take as much of 2^k as possible without exceeding N. Now repeat this first step with the next largest value of k in which 2^k <= remaining amount left, and do this with continously smaller denomination until the remainer is 0.  

1b) This choice is optimal because with powers of 2 it is impossible to have a smaller number of coins without using the largest possible power of 2 that is less than or equal to k. This is because with powers of 2, 2^k (the largest possible power of 2 <= N) is divisible by all powers < k. Meaning any assortment of coins less than 2^k that equal N will have a grouping of coins that can be summed to equal 2^k, which reduces the amount of coins used.

1c) Work = O(logn), Span = O(logn). This is because N is reduced by a factor of at least 2 after each successive denomination is used.

2a) If the denominations are (1, 5, 8), then my greedy algorithm would first choose the largest denomination 8. 10-8=2, so the next largest denomination possible would be 1. 2-1=1, 1-1=0. This uses 3 coins total, whereas the actual opitmal solution would be 2 coins worth $5.

2b) This problem has an optimal substructure property because in order to find the minimum number of coins needed one must break the problem into smaller sub-problems. All of these subproblems must contain the optimal amount of coins to have an overall optimal number of coins for a given amount N. If C(N) represnts the problem, with N being the amount of money, then after the first denomination is picked the problem can be represented as C(N-D) + 1 where D is the denomintation. This subproblem therefore must be optimal. However, if it is not optimal then we know our original denomiation was incorrect, thus the problem must recursively evaluate all possible subproblems to guarantee the global optimum. 

2c) The number of subproblems is N x the number of possible denominations (i) and the work done at each subproblem is simply O(1). Therefore the total work and span is O(N x i).

