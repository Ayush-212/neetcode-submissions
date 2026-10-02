class Solution {
public:

    string encode(vector<string>& strs) {
        std::string res = "";
        for(const std::string &s:strs){
            res += std::to_string(s.length())+"#"+s;
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        size_t i = 0;
        while(i<s.length()){
            size_t j = i;
            while (s[j] != '#'){
                j++;
            }

            int length = stoi(s.substr(i,j-i));

            res.push_back(s.substr(j+1,length));

            i = j+1+length;
        }
        return res;
    }
};
