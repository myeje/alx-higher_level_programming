#!/usr/bin/node
const num = process.argv[2];

if (parseInt(num)) {
	for (let i = 0; i < num; i++) {
		for (let j = 0; j < num; j++) {
			console.log('X');
		}
	}
} else {
	console.log('Missing size');
}
