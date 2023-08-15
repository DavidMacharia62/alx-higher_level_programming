#!/usr/bin/node
// A script that imports an array and computes a new one
const list = require('./100-data').list;

const newArray = [];
list.map((item, index) => newArray.push(item * index));

console.log(list);
console.log(newArray);
