
.name,

# Task 2: replace `null` with the count of the required ingredients.
(.ingredients | length),

# Task 3: replace `null` with the amount of sugar.
(.ingredients | map(select(.item == "sugar")).[] | .amount.quantity),

# Task 4: replace `null` with the mapping of ingredient names with their substitutions
# (no comma after the last filter)
(
  .ingredients + .["optional ingredients"] 
  | map(select(.substitute)) 
  | map({(.item): (.substitute)})
  | add
)
