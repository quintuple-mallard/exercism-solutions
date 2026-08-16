# Encode a string using run-length encoding
# Ciphertext ? Plaintext
Encode ← |1 ⍣(⊂""|"")/◇⊂▽¬⊸∊{"0""1"}/⊂⍉⊟°⋕°▽

# Decode a string encoded with run-length encoding
# Plaintext ? Ciphertext
Decode ← |1 ⍣(⊂""|"")/◇⊂⍚(⊂▽⊙⊃↙₁↘₁)⍣⋕1∩⌟⊜□⟜¬⊸∊+@0⇡10
