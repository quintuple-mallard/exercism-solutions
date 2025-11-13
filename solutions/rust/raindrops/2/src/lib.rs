const VOWELS: [(&str, u32); 3] = [("i", 3), ("a", 5), ("o", 7)];
pub fn raindrops(n: u32) -> String {
    let mut sound = String::new();
    for (vowel, number) in VOWELS {
        if n % number == 0 {
            sound.push_str(&format!("Pl{vowel}ng"));
        }
    }
    if sound == String::new() { format!("{n}") }
    else { sound }
}
