#!/usr/bin/node
const list = require('./100-data.js').list;

const list2 = list.map((value, pos) => value * pos);
console.log(list);
console.log(list2);
