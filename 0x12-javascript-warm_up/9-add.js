#!/usr/bin/node
// A script that adds two integers from arguments 1 & 2
const argv = require('process').argv;

function add (a, b) {
  return a + b;
}

const a = Number(argv[2]);
const b = Number(argv[3]);

console.log(add(a, b));
