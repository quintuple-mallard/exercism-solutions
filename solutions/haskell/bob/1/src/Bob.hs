module Bob (responseFor) where
import qualified Data.Text as T
import           Data.Text (Text, isSuffixOf, strip, toUpper, pack, unpack)
import           Data.Char (isAlpha)


isUpper :: Text -> Bool
isUpper xs = (toUpper xs) == xs && any isAlpha (unpack xs)

responseFor :: Text -> Text
responseFor xs
  | (pack "?" `isSuffixOf` (strip xs)) && (isUpper xs) = pack "Calm down, I know what I'm doing!"
  | (pack "?" `isSuffixOf` (strip xs)) = pack "Sure."
  | (isUpper xs) = pack "Whoa, chill out!"
  | (strip xs) == pack "" = pack "Fine. Be that way!"
  | otherwise = pack "Whatever."