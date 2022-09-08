#!/usr/bin/node
'use strict';
let nextMax = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort((a, b) => a - b);
  nextMax = args[args.length - 2];
}
console.log(nextMax);
