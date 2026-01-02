use std::{
    collections::HashMap,
    thread
};
pub fn frequency(input: &[&str], worker_count: usize) -> HashMap<char, usize> {
    if input.is_empty() {
        return HashMap::new();
    }
    let chunk_size = (input.len() / worker_count) + 1;
    let threads: Vec<_> = input.chunks(chunk_size)
        .map(|chunk| {
            let chunk = chunk.concat();
            thread::spawn(move ||
                chunk.to_lowercase()
                    .chars()
                    .filter(|c| c.is_alphabetic())
                    .fold(HashMap::<char, usize>::new(), |mut hm, c| {
                        *hm.entry(c).or_default() += 1;
                        hm
                    })
            )
        })
        .collect();
    threads.into_iter().fold(HashMap::new(), |mut hm, thread| {
        let hm_thread = thread.join().unwrap();
        hm_thread.into_iter()
            .for_each(|(c, count)| *hm.entry(c).or_default() += count);
        hm
    })
}