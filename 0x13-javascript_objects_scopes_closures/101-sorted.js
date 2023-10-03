#!/usr/bin/node

const { dict } = require('./101-data.js');

const newDict = {};

for (const user in dict) {
  const occur = dict[user];

  if (newDict[occur] === undefined) {
    newDict[occur] = [user];
  } else {
    newDict[occur].push(user);
  }
}

console.log(newDict);
