/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounterWithClosure = function(init) {
    let val = init
    return {
        increment: () => ++val,
        decrement: () => --val,
        reset: () => {
            val = init;
            return val;
        }
    }   
};

var createCounter = function(init) {
    return {
        val: init,
        increment: function() {return ++this.val},
        decrement: function() {return --this.val},
        reset: function() {
            this.val = init;
            return this.val
        }
    }   
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */