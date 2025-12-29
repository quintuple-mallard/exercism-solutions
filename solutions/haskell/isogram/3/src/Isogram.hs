module Isogram (isIsogram) where

import qualified Data.List.NonEmpty as N
import Data.List (sort)
import Data.Char (toUpper)


isIsogram :: String -> Bool
isIsogram xs =  (length . nub) cleaned == length cleaned
    where cleaned = filter (`elem` ['A'..'Z']) . map toUpper $ xs
          nub = map N.head . N.group . sort
