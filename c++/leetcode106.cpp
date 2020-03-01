/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return buildTree(inorder, postorder,0,inorder.size()-1,0,postorder.size()-1);
    }
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder,int is,int ie,int ps,int pe){
        if(ps>pe) return nullptr;
        int index=is;
        while(index<=ie && postorder[pe] != inorder[index])
            index++;
        if(index>ie) return nullptr;
        TreeNode* root=new TreeNode(postorder[pe]);
        root->right =  buildTree(inorder, postorder,index+1,ie,ps+index-is,pe-1);
        root->left =  buildTree(inorder, postorder,is,index-1,ps,ps+index-is-1);
        return root;                       
    }
};
