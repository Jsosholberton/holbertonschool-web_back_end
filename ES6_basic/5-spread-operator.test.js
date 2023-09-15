import concatArrays from './5-spread-operator.js';

test('returns the array', () => {
  expect(concatArrays(['a', 'b'], ['c', 'd'], 'Hello')).toEqual(["a", "b", "c", "d", "H", "e", "l", "l", "o"]);
});
