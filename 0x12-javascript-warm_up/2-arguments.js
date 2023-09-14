#!/usr/bin/node

const args = process.argv.length;

if (args === 1) {
	console.log('Argument found');
} else if (args >= 2) {
	console.log('Arguments found');
} else {
	console.log('No argument');
}
