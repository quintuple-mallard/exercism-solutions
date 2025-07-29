module Strain (keep, discard) where

discard :: (a -> Bool) -> [a] -> [a]
discard p xs = [ item | item <- xs, not (p item)]

keep :: (a -> Bool) -> [a] -> [a]
keep p xs = [ item | item <- xs, p item]
