#!/usr/bin/node

/**
 * function that returns the reversed version of a list
 */
exports.esrever = function (list) {
	let num = list.length - 1;
	const list2 = [];

	for (; num >= 0; num--) {
		list2.push(list[num]);
	}

	return (list2);
};