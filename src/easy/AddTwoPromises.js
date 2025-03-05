/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
    const executor = async function(resolve) {
        let val1 = await promise1;
        let val2 = await promise2;
        resolve(val1 + val2);
    }
    return new Promise(executor); 
};

// const addTwoPromises = async function(promise1, promise2) {
//     return Promise.all([promise1,promise2])
//     .then(value => value.reduce((acc,val) => acc+val,0))
// };


let promise1 = new Promise(resolve => setTimeout(() => resolve(2), 20));
let promise2 = new Promise(resolve => setTimeout(() => resolve(5), 60));
addTwoPromises(promise1, promise2).then((value) => console.log(value));

// let promise1 = new Promise(resolve => setTimeout(() => resolve(10), 50));
// let promise2 = new Promise(resolve => setTimeout(() => resolve(-12), 30));
// let result = await addTwoPromises(promise1, promise2);
// console.log(result);
