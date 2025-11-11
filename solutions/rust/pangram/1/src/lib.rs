use std::collections::HashSet;

/// Determine whether a sentence is a pangram.
pub fn is_pangram(sentence: &str) -> bool {
    sentence
        .to_lowercase()
        .chars()
        .collect::<HashSet<char>>()
        .iter()
        .filter(|c| c.is_alphabetic())
        .collect::<Vec<&char>>()
        .len() == 26
}
