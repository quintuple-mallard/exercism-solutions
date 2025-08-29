pub fn sum_of_multiples(limit: u32, factors: &[u32]) -> u32 {
    let mut multiples = Vec::new();
    for n in 1..limit {
        for factor in factors {
            if n == 0 || factor == &0 {
                continue;
            }
            if (n % factor) == 0 {
                if !multiples.contains(&n){
                    multiples.push(n);
                }
            }
        }
    }
    multiples.iter().sum()
}
