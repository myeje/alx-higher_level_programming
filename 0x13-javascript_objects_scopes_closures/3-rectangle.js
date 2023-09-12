#!/usr/bin/node
/**
 * Class Rectangle that defines a rectangle with 2 constructors
 * and an if statement
 * 
 * instance method print that prints out a char
 */

class Rectangle {
	constructor (w, h) {
		if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
			this.width = w;
			this.height = h;
		}
	}

	print() {
		for (let i = 0; i < this.height; i++) {
			let varName = '';
			let j = 0;
			for (; j < this.width; j++) {
				varName += 'X';
			}
			console.log (varName);
			}
		}
	}

module.exports = Rectangle;