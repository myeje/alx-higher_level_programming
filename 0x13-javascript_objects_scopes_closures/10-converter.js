#!/usr/bin/node

exports.converter = function (base) {
  function convert (i) {
    return i.tostring(base);
  }
  return convert;
};
