pub fn square(s: u32) -> u128 {
    assert!((1..=64).contains(&s));
    1 << (s - 1)
}

pub fn total() -> u128 {
    (1 << 64) - 1
}
