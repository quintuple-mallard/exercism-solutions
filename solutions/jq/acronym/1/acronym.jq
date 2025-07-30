.
| .phrase
| split("")
| map(select(test("^[a-z -]"; "gi")))
| add
| gsub("-"; " ")
| split(" ")
| map(.[0:1])
| add
| ascii_upcase