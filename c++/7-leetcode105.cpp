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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if(preorder.size()==0 ||inorder.size()==0 ||preorder.size() !=inorder.size())
            return nullptr;
        return buildTree(preorder, inorder,0,preorder.size()-1,0,preorder.size()-1);
    }
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder,int ps,int pe,int is,int ie){
        if(ps>pe) return nullptr;
        int index=is;
        while(preorder[ps]!=inorder[index] && index<=ie)
            index++;
        if(index>ie) return nullptr;
        TreeNode* root=new TreeNode(preorder[ps]);
        root->left=buildTree(preorder,inorder,ps+1,ps+index-is,is,index-1);
        root->right=buildTree(preorder,inorder,ps+index-is+1,pe,index+1,ie);
        return root;
        
    }
};
