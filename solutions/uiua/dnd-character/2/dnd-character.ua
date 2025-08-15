# Calculate the modifier of an Ability score
# ModifierValue ? Score
Modifier ← |1 ⌊÷2-10

# Generate a random Ability score
# Score ? 
Ability ← |0 (/+↙3 ⇌⍆+1[⚂₆ ⚂₆ ⚂₆ ⚂₆])

# Generate a random character
# Character ? 
Character ← |0 (⍥Ability6)

# Retrieve the Strength score of a Character
# AbilityValue ? Character
Strength ← |1 ⊡0

# Retrieve the Dexterity score of a Character
# AbilityValue ? Character
Dexterity ← |1 ⊡1

# Retrieve the Constitution score of a Character
# AbilityValue ? Character
Constitution ← |1 ⊡2

# Retrieve the Intelligence score of a Character
# AbilityValue ? Character
Intelligence ← |1 ⊡3

# Retrieve the Wisdom score of a Character
# AbilityValue ? Character
Wisdom ← |1 ⊡4

# Retrieve the Charisma score of a Character
# AbilityValue ? Character
Charisma ← |1 ⊡5

# Retrieve the Hitpoints score of a Character
# AbilityValue ? Character
Hitpoints ← |1 +10 Modifier Constitution
