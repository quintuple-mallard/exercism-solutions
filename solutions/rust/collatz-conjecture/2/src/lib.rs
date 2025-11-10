pub fn collatz(mut n: u64) -> Option<u64> {
    if n < 1 {
        return None
    }
    let mut count = 0;
    while n != 1 {
        n = if (n % 2) == 1 {
            n * 3 + 1
        } else {
            n / 2
        };
        count += 1;
    };
    Some(count)
}
