export function truncate(post) {
  return [...post].slice(0,5).join("");
}