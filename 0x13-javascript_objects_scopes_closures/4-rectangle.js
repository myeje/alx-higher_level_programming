#!/usr/bin/node
/**
 * Class Rectangle that defines a rectangle with 2 constructors
 * and an if statement
 *
 * instance method print that prints out a char
 * instance method rotate() that exchanges the width and height
 * instance method double() that multiplies the width and height by 2
 */

class Rectangle {
	constructor (w, h) {
		if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
			this.width = w;
			this.height = h;
		}
	}

	print() {
		console.log ("Normal:")
		for (let i = 0; i < this.height; i++) {
			let varName = '';
			let j = 0;
			for (; j < this.width; j++) {
				varName += 'X';
			}
			console.log (varName);
			}
		}

		rotate() {
			let tmp = 0;
			tmp = this.height;
			this.height = this.width;
			this.width = tmp;
		}

		double() {
			this.width *= 2;
			this.height *= 2;
		}
	}

module.exports = Rectangle;