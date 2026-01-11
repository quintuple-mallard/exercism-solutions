#ifndef PANGRAM_H
#define PANGRAM_H

#include <stdbool.h>
#include <ctype.h>
#include <stdint.h>
#include <string.h>

bool is_pangram(char const*);
int32_t alphabet_index(char);

#endif
