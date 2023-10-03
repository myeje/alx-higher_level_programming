#!/usr/bin/node
/**
 * Class Rectangle that defines a rectangle with 2 constructors
 * and an if statement
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
