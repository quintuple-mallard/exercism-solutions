~ "git: github.com/ekgame/uiua-essentials" ~ Trim
IsEmpty     ← ≍ "" Trim
IsUppercase ← *⊃(≍by⌵|notmatfor(≍`byabs|≍by⌵))
IsQuestion  ← ⍣(≍"?"↙1⇌)0
Classify    ← /↥ ?×⇡5 ⊂⊂⊂⊂ ⊃(0|IsEmpty|IsQuestion|IsUppercase|(× IsUppercase⟜IsQuestion))
# Respond to a phrase as Bob would
# Response ? Phrase
HeyBob ← |1 ⨬("Whatever."|"Fine. Be that way!"|"Sure."|"Whoa, chill out!"|"Calm down, I know what I'm doing!") Classify
