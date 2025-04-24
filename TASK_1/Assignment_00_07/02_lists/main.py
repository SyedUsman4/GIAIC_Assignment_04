import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40

def create_grid(canvas):

    cells = []
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        row_cells = []
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            rect = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")
            row_cells.append(rect)
        cells.append(row_cells)
    return cells 


def erase(event):
    x, y = event.x, event.y
    row = y // CELL_SIZE
    col = x // CELL_SIZE

    if 0 <= row < len(gird) and 0 <= col < len(gird[0]):
     canvas.itemconfig(gird[row][col], fill="white")


def main():
    global canvas, gird 
    root = tk.Tk()
    root.title("Grid Erase Canvas")

    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.bind("<B1-Motion>", erase)  
    canvas.pack()

    gird = create_grid(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()    


