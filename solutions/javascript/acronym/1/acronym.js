export const parse = phrase => {
  phrase=phrase.replace(/[^a-zA-Z- ]/,'').replace('-',' ').split(/\s+/)
  let acronym=''
  for (const word of phrase){
    acronym+=word[0].toUpperCase()
  }
  return acronym
}