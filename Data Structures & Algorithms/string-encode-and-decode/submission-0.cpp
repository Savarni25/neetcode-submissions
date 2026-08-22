#include <vector>
#include <string>

class Solution {
public:
    // Encodes a list of strings to a single string.
    std::string encode(const std::vector<std::string>& strs) {
        std::string encoded = "";
        for (const std::string& s : strs) {
            encoded += std::to_string(s.length()) + '#' + s;
        }
        return encoded;
    }

    // Decodes a single string to a list of strings.
    std::vector<std::string> decode(const std::string& s) {
        std::vector<std::string> decoded;
        size_t i = 0;
        
        while (i < s.length()) {
            size_t delim_pos = s.find('#', i);
            int len = std::stoi(s.substr(i, delim_pos - i));
            
            size_t start = delim_pos + 1;
            decoded.push_back(s.substr(start, len));
            
            i = start + len;
        }
        
        return decoded;
    }
};