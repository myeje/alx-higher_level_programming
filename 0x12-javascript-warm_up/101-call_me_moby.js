#!/usr/bin/node
exports.callMeMobby = function (x, func) {
	for (let i = 0; i < x; i++) {
		func();
	}
};
