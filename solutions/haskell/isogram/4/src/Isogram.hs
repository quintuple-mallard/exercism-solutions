module Isogram (isIsogram) where

import qualified Data.Set as Set  
import Data.Char (toUpper)


isIsogram :: String -> Bool
isIsogram xs = (length . Set.fromList) cleaned == length cleaned
    where cleaned = filter (`elem` ['A'..'Z']) . map toUpper $ xs
          
