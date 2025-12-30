module Isogram (isIsogram) where

import qualified Data.Set as Set  
import Data.Char (toUpper, isAsciiUpper)


isIsogram :: String -> Bool
isIsogram xs = (Set.size . Set.fromList) cleaned == length cleaned
    where cleaned = filter isAsciiUpper . map toUpper $ xs
          
