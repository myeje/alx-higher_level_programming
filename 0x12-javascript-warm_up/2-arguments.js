#!/usr/bin/node

const args = process.argv.slice(2);

if (args > 2) {
	console.log('Argument found');
} else if (args > 3) {
	console.log('Arguments found');
} else {
	console.log('No argument');
}
