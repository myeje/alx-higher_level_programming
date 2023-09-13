#!/usr/bin/node

exports.nbOccurrences = function (list, searchElement) {
	let num = 0;
	
	for (let i = 0; i < list.length; i++) {
		num = (list[i] === searchElement ? num + 1 : num);
	}
	return num;
};
