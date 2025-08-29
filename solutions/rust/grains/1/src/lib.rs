pub fn square(s: u32) -> u128 {
    if s < 1 || s > 64 {
        panic!();
    }
    1 << (s - 1)
}

pub fn total() -> u128 {
    (1 << 64) - 1
}
