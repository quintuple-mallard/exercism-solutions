# Determine if a year is a leap year
# IsLeapYear ? Year
OR  ← >0 +
AND ← ×
NOT ← = 0
Leap ← (
  =0◿4_100_400
  ⊡0⤙⊡1⤙⊡2
  OR AND ⊙NOT
)