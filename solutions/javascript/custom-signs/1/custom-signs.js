// @ts-check
export function buildSign(occasion, name) {
  return `Happy ${occasion} ${name}!`;
}
export function buildBirthdaySign(age) {
  return `Happy Birthday! What a ${age>=50 ? 'mature':'young'} fellow you are.`;
}
export function graduationFor(name, year) {
  return `Congratulations ${name}!\nClass of ${year}`;
}


export function costOf(sign, currency) {
  return `Your sign costs ${20+sign.length*2}.00 ${currency}.`;
}