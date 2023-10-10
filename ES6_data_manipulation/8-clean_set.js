export default function cleanSet(set, startString) {
  let cadena = '';
  if (set && startString) {
    set.forEach((elemento) => {
      cadena += `${elemento.replace(startString, '')}-`;
    });
    cadena = cadena.slice(0, -1);
  }
  return cadena;
}
