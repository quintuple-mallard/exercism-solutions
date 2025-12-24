module Pangram (isPangram) where

import Data.Char (toUpper)
import Data.List (nub)



cleanUp :: String -> String
cleanUp = filter (`elem` ['A'..'Z']) . map toUpper 

isPangram :: String -> Bool
isPangram = (==) 26 . length . nub . cleanUp 
