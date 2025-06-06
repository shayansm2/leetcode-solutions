/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {    
    return function(x) {
        functions.reverse().forEach(f => {
            x = f(x); 
        });
        return x;
    }
};


const fn = compose([x => x + 1, x => 2 * x])
console.log(fn(4)) // 9