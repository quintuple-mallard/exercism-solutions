pub fn build_proverb(list: &[&str]) -> String {
    let mut proverb = String::new();
    for (i, item) in list.iter().enumerate() {
        if i + 1 == list.len() {
            proverb.push_str(
                &format!("And all for the want of a {}.", list[0])[..]
                            );
        } else {
            proverb.push_str(
                &format!(
                    "For want of a {} the {} was lost.\n", item, list[i + 1]
                )[..]
            );
        }
    }
    proverb
}
