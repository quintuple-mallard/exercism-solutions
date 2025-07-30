module CollatzConjecture (collatz) where

collatz :: Integer -> Maybe Integer
collatz n
  | n == 1 = Just 0
  | n <= 0 = Nothing
  | n `mod` 2 == 0 = fmap (+1) (collatz (n `div` 2))
  | otherwise = fmap (+1) (collatz (n * 3 + 1))
