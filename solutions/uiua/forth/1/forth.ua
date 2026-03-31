Assert₂ ← ⨬(⍤"empty stack"0|⍤"only one value on the stack"0|)↧2⊸⧻
Assert₁ ← ⨬(⍤"empty stack"0|)↧1⊸⧻

O! ← ⊂^0⊃↙↘2
Perform ← (
  ⍣(⍩⊂ ⋕
  | O!/+⍩Assert₂°"+"
  | O!/-⍩Assert₂°"-"
  | O!/×⍩Assert₂°"*"
  | O!(⌊/÷)⍩(⍤"divide by zero"≠0⊸⊢Assert₂)°"/"
  | ⊂⊸⊢⍩Assert₁ °"DUP"
  | ↘₁⍩Assert₁ °"DROP"
  | O!⇌⍩Assert₂°"SWAP"
  | O!(⊂⊸⊣)⍩Assert₂ °"OVER"
  | ∘
  ) °□
)
Evaluate ← |1 ⇌˜∧(Perform) []⊜□⊸≠@ ⌵
