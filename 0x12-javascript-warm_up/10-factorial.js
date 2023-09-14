#!/usr/bin/node
const arg = parseInt(process.argv[2]);

function factorial (i) {
	if (isNaN(i) || i < 0) {
		return 1;
	}
	if (i === 0) {
		return 1;
	}
	return i * factorial(i - 1);
}

console.log(factorial(arg));
