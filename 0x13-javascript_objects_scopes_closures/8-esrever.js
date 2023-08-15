#!/usr/bin/node
// A script that reverses a list
exports.esrever = function (list) {
  const arr = [];

  for (let i = list.length - 1; i >= 0; i--) {
    arr.push(list[i]);
  }
  return arr;
};
