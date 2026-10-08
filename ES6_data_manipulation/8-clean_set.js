export default function cleanSet(set, startString) {
  if (!(set instanceof Set) || typeof startString !== 'string' || startString === '') {
    return '';
  }
  const parts = [];
  set.forEach((value) => {
    if (typeof value === 'string' && value.startsWith(startString)) {
      parts.push(value.slice(startString.length));
    }
  });
  return parts.join('-');
}
