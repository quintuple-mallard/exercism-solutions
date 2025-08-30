pub fn is_armstrong_number(num: u32) -> bool {
    let str_num = format!("{}", num);
    let num_len: u32 = str_num.len() as u32;
    let mut armstrong_sum: u64 = 0;
    for item in str_num.chars() {
        armstrong_sum += ((item as u32 - '0' as u32).pow(num_len)) as u64;
    }
    armstrong_sum == (num as u64)
}
