#!/usr/bin/node

exports.converter = function (base) {
	if (base <= 1 || base > 36) {
		return null;
	}

	function convert (i) {
		return i.tostring(base);
	}
	return convert;
};