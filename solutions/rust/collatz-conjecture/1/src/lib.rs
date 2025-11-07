pub fn collatz(n: u64) -> Option<u64> {
    if n < 1 {
        return None
    }
    let mut num = n;
    let mut count = 0;
    while num != 1 {
        num = if (num % 2) == 1 {
            num * 3 + 1
        } else {
            num / 2
        };
        count += 1;
    };
    Some(count)
}
