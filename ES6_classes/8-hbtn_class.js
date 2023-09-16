export default class HolbertonClass {
  constructor(size = 0, location = '') {
    this._size = size;
    this._location = location;
  }

  [Symbol.toPrimitive](dataType) {
    return dataType === 'string' ? `${this._location}` : `${this._size}`;
  }
}
