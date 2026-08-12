const drawingCanvas = document.getElementById("drawingCanvas");
const context = drawingCanvas.getContext("2d");
const clearButton = document.getElementById("clearButton");

console.log(drawingCanvas);
console.log(clearButton);

let isDrawing = false;
drawingCanvas.addEventListener("mousedown", function() {
    isDrawing = true;
});
drawingCanvas.addEventListener("mouseup", function() {
    isDrawing = false;
});
drawingCanvas.addEventListener("mousemove", function(event) {
    if (!isDrawing) {return;}

    const cellSize = 10;

    const x = event.offsetX; // gets the position of the mouse
    const y = event.offsetY;

    const column = Math.floor(x / cellSize); // calculates the coords of the "cell"
    const row = Math.floor(y / cellSize);

    const cellX = column * cellSize; // converts the cell into coordinates
    const cellY = row * cellSize;

    context.fillStyle = "black";
    context.fillRect(cellX, cellY, cellSize, cellSize);
});
clearButton.addEventListener("click", function() {
    context.fillStyle = "white";
    context.fillRect(0, 0, drawingCanvas.clientWidth, drawingCanvas.clientHeight)
})