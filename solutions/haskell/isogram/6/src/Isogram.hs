module Isogram (isIsogram) where

import qualified Data.Set as Set  
import Data.Char (toUpper, isAsciiUpper)


isIsogram :: String -> Bool
isIsogram = (==) <$> Set.size . Set.fromList . clean <*> length . clean
    where clean = filter isAsciiUpper . map toUpper
          
