use std::{
    collections::{HashMap, hash_map::Entry},
    sync::{Arc, Mutex},
    thread,
};
fn chunk(string: &str, n_chunks: usize) -> Vec<String> {
    let mut chunks: Vec<String> = Vec::new();

    for (i, c) in string.chars().enumerate() {
        if chunks.len() < n_chunks {
            chunks.push(String::new());
        }
        chunks[i % n_chunks].push(c);
    }
    chunks
}
fn normalize(input: &[&str]) -> String {
    input
        .join("")
        .chars()
        .filter(|c| c.is_alphabetic())
        .map(|c| c.to_lowercase().to_string())
        .collect()
}
pub fn frequency(input: &[&str], worker_count: usize) -> HashMap<char, usize> {
    let input = normalize(input);
    let hm = Arc::new(Mutex::new(HashMap::<char, usize>::new()));
    let chunks = chunk(&input, worker_count);
    let mut threads = Vec::new();
    for chunk in chunks.iter() {
        let hm = Arc::clone(&hm);
        let chunk = chunk.clone();
        threads.push(thread::spawn(move || {
            let mut hm = hm.lock().unwrap();
            for c in chunk.chars() {
                if let Entry::Vacant(e) = hm.entry(c) {
                    e.insert(1);
                } else {
                    *hm.get_mut(&c).unwrap() += 1;
                }
            }
        }));
    }
    for thread in threads {
        thread.join().unwrap();
    }
    hm.lock().unwrap().clone()
}
