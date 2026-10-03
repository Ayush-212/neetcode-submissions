class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        std::vector<std::unordered_set<char>>rows(9);
        std::vector<std::unordered_set<char>>columns(9);
        std::vector<std::unordered_set<char>>boxes(9);


        for(int r=0;r<9;r++){
            for(int c= 0;c<9;c++){
                char val = board[c][r];
                if (val=='0' ||val=='.'){
                    continue;
                }

                int box_id = (r/3)*3 + (c/3);

                if(rows[r].count(val) || columns[c].count(val)||boxes[box_id].count(val)){
                    return false;
                }
                rows[r].insert(val);
                columns[c].insert(val);
                boxes[box_id].insert(val);
            }
        }
        return true;
    }
};
