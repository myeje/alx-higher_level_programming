#!/usr/bin/node
/**
 * function that prints the number of arguments already printed
 * and the new argument value
 */
let num = 0;

exports.logMe = function (item) {
<<<<<<< HEAD
  console.log(`${numArgsPrinted}: ${item}`);
  num++;
};
=======
	console.log(`${num}: ${item}`);
	num++;
};
>>>>>>> 0d434218355a3db8856b4a15553966e34a8eee5a
