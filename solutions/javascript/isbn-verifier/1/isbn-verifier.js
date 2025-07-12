const ALPHABET='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
function clean_up(raw_isbn) {
  let list_isbn = []
  for (const digit of raw_isbn) {
    if (digit === "-") {
      continue
    }
    else {
       list_isbn.push(digit)
    }
  }
  return list_isbn
}
//Separating the functions visually with comments
export function isValid(isbn) {
  let multiplier = 10
  let isbn_actual = clean_up(isbn)
  let sum = 0
  if (isbn_actual.length != 10) {
    return false
  }
  for (let item of isbn_actual) {
    if (item == "X" && multiplier == 1) {
       sum += 10*multiplier
    }
    else if( ALPHABET.includes(item) || (item == "X" && multiplier != 1)) {
      return false
    }
    else {
       sum = sum + Number(item)*multiplier
    }
     multiplier = multiplier - 1
  }
  if (sum % 11 == 0 ){
    return true
  }
  else {
    return false
  }
}