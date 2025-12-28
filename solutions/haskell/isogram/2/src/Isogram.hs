module Isogram (isIsogram) where

import Data.List (nub)
import Data.Char (toUpper)


isIsogram :: String -> Bool
isIsogram xs =  (length . nub) cleaned == length cleaned
    where cleaned = filter (`elem` ['A'..'Z']) . map toUpper $ xs
