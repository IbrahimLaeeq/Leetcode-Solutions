/**
 * @param {number[]} arr
 * @return {number}
 */
var findLucky = function(arr) {
    arr = arr.sort((a, b) => a-b);
    let stack = arr[arr.length - 1];
    let count = 0;
    for (let i = arr.length - 1; i >= 0; i--) {
        let num = arr[i];
        if (num == stack) {
            ++count;
        } 
        if (num !== stack) {
            if (count === stack) {
                return count;
            }
            count = 1;
            stack = num;
        }
    }
    
    if (count === stack) {
        return count;
    }
    
    return -1;
};