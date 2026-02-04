module Sublist (sublist) where
slice :: Int -> Int -> [a] -> [a]
slice from to xs = take (to - from + 1) (drop from xs)

chunks :: Int -> [a] -> [[a]]
chunks s xs = [slice x (x + s - 1) xs | x <- [0..(length xs - s)]]

sublist :: (Eq a) => [a] -> [a] -> Maybe Ordering
sublist [] [] = Just EQ
sublist [] _ = Just LT
sublist _ [] = Just GT
sublist xs ys
    | xs == ys = Just EQ
    | xs `elem` (chunks (length xs) ys) = Just LT
    | ys `elem` (chunks (length ys) xs) = Just GT
    | otherwise = Nothing
