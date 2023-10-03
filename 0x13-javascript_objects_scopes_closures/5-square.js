#!/usr/bin/node
/**
 * Class Square that defines a square and inherits Rectangle from
 * 4-rectangle.js
 */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
