#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 


b) n^2 because there's a loop nested in a loop.


c) o(n) worst case because it will decrement from the number `bunnies` begins at all the way to 0. this recursive code works similar to a loop that counts down, which is also o(n)

## Exercise II

This is a good use case for binary search. The floors are sorted in ascending order. Check the middle floor. If the eggs break on that floor, we can disregard all the floors above it. Then we check the middle floor of all the remaining floors and so on. Time complexity of log n.
