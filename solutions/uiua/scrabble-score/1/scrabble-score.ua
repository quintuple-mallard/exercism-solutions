# Calculate the scrabble score of a word
# Score ? Word
Score ← |1 (
  ⌵                                                             # Capitalize
  ˜⊗"ABCDEFGHIJKLMNOPQRSTUVWXYZ"                                # Indexes of letter in alphabet
  ≡(˜⊡ [1 3 3 2 1 4 2 4 1 8 5 1 3 1 1 3 10 1 1 1 1 4 4 8 4 10]) # Turn into scores
  /+                                                            # Sum
)