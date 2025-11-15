#[macro_export]
macro_rules! hashmap {
    (,) => (compile_error!());
    ( $( $k:expr => $v:expr),* $(,)?) => {
        {
            let mut hm = ::std::collections::HashMap::new();
            $(
                hm.insert($k, $v);
            )*
            hm
        }
    };
}