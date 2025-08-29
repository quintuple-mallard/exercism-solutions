pub fn square(s: u32) -> u128 {
    if !(1..65).contains(&s) {
        panic!();
    }
    1 << (s - 1)
}

pub fn total() -> u128 {
    (1 << 64) - 1
}
