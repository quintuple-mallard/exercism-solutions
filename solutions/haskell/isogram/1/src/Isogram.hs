module Isogram (isIsogram) where

import Data.List (nub)
import Data.Char (toUpper)


isIsogram :: String -> Bool
isIsogram xs =  (length . nub $ clean xs) == (length $ clean xs)
    where clean = filter (`elem` ['A'..'Z']) . map toUpper
