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
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if(t==nullptr && s==nullptr)  return true;
        if(t==nullptr && s!=nullptr)  return false;
        if(s==nullptr) return false;
        if(t->val == s->val) 
            if (issubtree( s->left, t->left) &&issubtree(s->right,  t->right) )
                return true;
        return isSubtree( s->left,  t) ||isSubtree( s->right, t);
    }
    bool issubtree(TreeNode* s, TreeNode* t){
        if(s==nullptr && t==nullptr) return true;
        if(t==nullptr || s==nullptr) return false;
        if(s->val != t->val) return false;
        return issubtree( s->left, t->left) &&issubtree(s->right,  t->right);
        
    }
};
