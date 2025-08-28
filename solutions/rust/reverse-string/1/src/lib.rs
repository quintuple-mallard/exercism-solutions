pub fn reverse(input: &str) -> String {
    let mut reversed = String::new();
    for char in input.chars() {
        reversed = format!("{}{}", char.to_string(), reversed);
    }
    reversed
}