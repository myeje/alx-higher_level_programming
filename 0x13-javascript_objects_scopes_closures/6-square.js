#!/usr/bin/node
/**
 * Class Square that defines a square and inherits square from
 * 5-square.js
 */


const Square1 = require('./5-square');

class Square extends Square1 {
	charPrint(c) {
		if (c === undefined) {
			c = 'X';
		}
		for (let i = 0; i < this.height; i++) {
			let varName = '';
			let j = 0;
			for (; j < this.width; j++) {
				varName += c;
			}
			console.log (varName);
			}
	}
}

module.exports = Square;