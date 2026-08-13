const drawingCanvas = document.getElementById("drawingCanvas");
const context = drawingCanvas.getContext("2d");
const clearButton = document.getElementById("clearButton");
const startButton = document.getElementById("startButton");
const digitInput = document.getElementById("digitInput");

const cellSize = 10;

let isDrawing = false;
drawingCanvas.addEventListener("mousedown", function() {
    isDrawing = true;
});
drawingCanvas.addEventListener("mouseup", function() {
    isDrawing = false;
});
drawingCanvas.addEventListener("mousemove", function(event) {
    if (!isDrawing) {return;}

    const x = event.offsetX;
    const y = event.offsetY;

    const column = Math.floor(x / cellSize);
    const row = Math.floor(y / cellSize);

    const cellX = column * cellSize;
    const cellY = row * cellSize;

    context.fillStyle = "black";
    context.fillRect(cellX, cellY, cellSize, cellSize);
});
clearButton.addEventListener("click", function() {
    context.fillStyle = "white";
    context.fillRect(0, 0, drawingCanvas.clientWidth, drawingCanvas.clientHeight);
});
startButton.addEventListener("click", function() {
    const gridData = [];

    for (let row = 0; row < 40; row++) { // "++" short for +1
        for (let column = 0; column < 40; column++) { // (startvalue, endvalue, indexnumber)
            const sampleX = (column * cellSize) + (cellSize / 2);
            const sampleY = (row * cellSize) + (cellSize / 2);

            const pixel = context.getImageData(sampleX, sampleY, 1, 1).data;

            const r = pixel[0];
            const g = pixel[1];
            const b = pixel[2];
            const a = pixel[3];
            let value = 0;

            if (a > 0 && r === 0 && g === 0 && b === 0) {
                value = 1;
            }
            gridData.push(value);
        }
    }

    const correctValue = Number(digitInput.value);
    if (digitInput.value === "") {
    return;
    }
    if (correctValue < 0 || correctValue > 9) {
    return;
    }

    fetch("/train", {
        method: "POST",
    
        headers: {
            "Content-Type": "application/json"
        },
    
        body: JSON.stringify({
            inputs: gridData,
            correctNumber: correctValue
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    });

    //console.log(gridData);
    //console.log(gridData.length);
    //console.log(correctValue);
});