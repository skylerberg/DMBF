Array.prototype.randomElement = function () {
    return this[Math.floor(Math.random() * this.length)];
}

function raffle (catagory) {
    /*
     * Selects a value from catagory in data.js using a raffle system.
     */
    var roll = Math.floor(Math.random() * data[catagory].total);
    var total = 0; // used to see when we have reached the roll in the raffle
    for (var element in data[catagory]) {
        total += data[catagory][element];
        if (total > roll) {
            return element;
        }
    }
}
