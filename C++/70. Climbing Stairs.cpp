class Solution
{
public:
    int climbStairs(int n)
    {
        if (n <= 1)
            return 1;


        int prev = 1, current = 1, next;

        for (int i = 2; i <= n; ++i)
        {
            next = prev + current;
            prev = current;
            current = next;
        }
        return current;
    }
};