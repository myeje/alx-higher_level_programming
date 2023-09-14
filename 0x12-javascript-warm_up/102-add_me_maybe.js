#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
	const increment = number + 1;
	theFunction(increment);
};
