#!/usr/bin/node
'use strict';
let nextMax = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  let newArgs = args.map(el => parseInt(el));
  newArgs.sort();
  nextMax = newArgs[newArgs.length - 2];
}
console.log(nextMax);
