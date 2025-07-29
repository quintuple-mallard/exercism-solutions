module Darts (score) where
-- Calculate the distance of a point (as a pair of Cartesian coordinates) from 0, 0
distance :: Float -> Float -> Float
distance x y = sqrt (x * x + y * y)

score :: Float -> Float -> Int
score x y
  | r <= 1 = 10
  | r <= 5 = 5
  | r <= 10 = 1
  | otherwise = 0
  where r = distance x y
