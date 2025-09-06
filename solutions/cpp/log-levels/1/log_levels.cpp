#include <string>
typedef std::string string;
namespace log_line {
string message(string line) {
    return line.substr(line.find(": ") + 2);
}

string log_level(string line) {
    return line.substr(line.find("[") + 1, line.find("]") - 1);
}

string reformat(string line) {
    return message(line) + " (" + log_level(line) + ")";
}
}  // namespace log_line
