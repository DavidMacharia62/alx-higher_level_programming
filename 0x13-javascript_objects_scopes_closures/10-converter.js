#!/usr/bin/node
// Converts a number from base 10 to arg base passed
exports.converter = function (base) {
  return function (nb) {
    return nb.toString(base);
  };
};
