module Pangram (isPangram) where

import Data.Char (toUpper)
import Data.List (nub)

cleanUp :: String -> String
cleanUp text = [toUpper c | c <- text, c `elem` ['a'..'z'] || c `elem` ['A'..'Z'] ]

isPangram :: String -> Bool
isPangram text = (==) 26 . length . nub . cleanUp $ text
