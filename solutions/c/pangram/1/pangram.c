#include "pangram.h"

int32_t alphabet_index(char c) {
    c = toupper(c);
    return (c >= 'A' && c <= 'Z') ? c - 'A' : INT32_MAX;
}

bool is_pangram(char const* str) {
    if (!str) return false; 

    bool tracker[26] = {0};
    for (uint64_t i = 0; i < strlen(str); ++i) {
        char c = str[i];
        int32_t index = alphabet_index(c);
        if (index != INT32_MAX) { 
            tracker[index] = true;
        }
    }

    uint64_t sum = 0;
    for (uint64_t i = 0; i < 26; ++i) {
        sum += tracker[i];
    }

    return sum == 26;
}
