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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(root==nullptr) return {};
        vector<vector<int>> result;
        deque<TreeNode*> tmp_que;
        tmp_que.push_back(root);
        int level=0;
        int level_count=1;
        int next_level_count=0;
        result.push_back({});
        while(!tmp_que.empty()){
            if(tmp_que.front()->left) {tmp_que.push_back(tmp_que.front()->left);next_level_count++;}
            if(tmp_que.front()->right) {tmp_que.push_back(tmp_que.front()->right);next_level_count++;}
            result[level].push_back(tmp_que.front()->val);
            level_count--;
            tmp_que.pop_front();
            if(level_count==0){
                level_count=next_level_count;
                next_level_count=0;
                level++;
                if(level_count !=0)
                    result.push_back({});
                }
        }
        return result;
    }
};
