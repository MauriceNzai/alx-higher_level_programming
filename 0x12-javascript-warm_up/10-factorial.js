#!/usr/bin/node
let num = isNaN(Number(process.argv[2])) ? 1 : Number(process.argv[2]);
function fact (a) {
	if (a === 0) return 1;
	return (a * fact(a - 1);
}

console.log(fact(num));
