#!/usr/bin/node
<<<<<<< HEAD
const Rectangle = require('./1-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

=======

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
>>>>>>> origin/main
