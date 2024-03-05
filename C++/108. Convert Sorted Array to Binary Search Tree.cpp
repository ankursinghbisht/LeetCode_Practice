/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {

    vector<int> nums;

    TreeNode* solve(int a, int b)
    {
        if (a == b)
            return NULL;
        int mid = (a + b) / 2;
        TreeNode* root = new TreeNode(nums[mid]);
        root->left = solve(a, mid);
        root->right = solve(mid + 1, b);
        return root;
    }
public:
    TreeNode* sortedArrayToBST(vector<int>& vec) {
        nums = vec;
        return solve(0, nums.size());
    }
};