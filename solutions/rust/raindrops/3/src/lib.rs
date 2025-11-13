const VOWELS: [(&str, u32); 3] = [("i", 3), ("a", 5), ("o", 7)];
pub fn raindrops(n: u32) -> String {
    let sound: String = VOWELS.iter()
        .filter_map(
            |&(v, m)| n
                    .is_multiple_of(m)
                    .then(|| format!("Pl{v}ng"))
        )
        .collect();
    if sound.is_empty() { n.to_string() }
    else { sound }
}
