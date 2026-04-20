class Node:
    def __init__(self, e):
        self.e = e
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size_val = 0

    def size(self):
        return self.size_val

    def is_empty(self):
        return self.head is None

    def create_node(self, e):
        return Node(e)

    def push(self, e):
        n = Node(e)
        if self.head is None:
            self.head = n
        else:
            n.next = self.head
            self.head = n
        self.size_val += 1

    def pop(self):
        if not self.is_empty():
            n = self.head
            self.head = self.head.next
            self.size_val -= 1
            return n.e
        return None

    def peek(self):
        if self.head is not None:
            return self.head.e
        return None


class Move:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def up(self):
        return Move(self.i - 1, self.j)

    def down(self):
        return Move(self.i + 1, self.j)

    def right(self):
        return Move(self.i, self.j + 1)

    def left(self):
        return Move(self.i, self.j - 1)


class Maze:
    def __init__(self):
        self.maze = [
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            [' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', '#'],
            ['#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#'], 
            ['#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#'],
            ['#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
            ['#', '#', ' ', '#', ' ', '#', '#', '#', 'S', '#'], 
            ['#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],  
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
        ]
        
        self.sizex = len(self.maze)
        self.sizey = len(self.maze[0])
        
        self.visited = [[0 for _ in range(self.sizey)] for _ in range(self.sizex)]
        
        self.sx, self.sy = 7, 8
        self.ex, self.ey = 2, 0
        
        self.print_maze()

    def path(self, m, value):
        tmp = self.maze[m.i][m.j]
        self.maze[m.i][m.j] = value
        return tmp

    def print_maze(self):
        for i in range(self.sizex):
            for j in range(self.sizey):
                print(self.maze[i][j], end=" ")
            print()

    def is_in_bounds(self, x, y):
        return 0 <= x < self.sizex and 0 <= y < self.sizey

    def is_available(self, m):
        return self.maze[m.i][m.j] != '#' and self.visited[m.i][m.j] != 1

    def is_found(self, m):
        return m.i == self.ex and m.j == self.ey

    def solve(self):
        stack = Stack()
        stack.push(Move(self.sx, self.sy))
        
        step = None
        tmp = None
        
        while not stack.is_empty():
            tmp = stack.pop()
                
            if self.is_found(tmp):
                break

            self.path(tmp, '.')
            self.maze[self.sx][self.sy] = 'S'
        
            step = tmp.up() 
            if self.is_in_bounds(step.i, step.j) and self.is_available(step): 
                stack.push(step)
                self.visited[step.i][step.j] = 1
                
            step = tmp.right() 
            if self.is_in_bounds(step.i, step.j) and self.is_available(step):
                stack.push(step)
                self.visited[step.i][step.j] = 1
                
            step = tmp.left() 
            if self.is_in_bounds(step.i, step.j) and self.is_available(step):
                stack.push(step)
                self.visited[step.i][step.j] = 1
                
            step = tmp.down() 
            if self.is_in_bounds(step.i, step.j) and self.is_available(step):
                stack.push(step)
                self.visited[step.i][step.j] = 1
           
            print()
            print(f"x:{step.i}  y:{step.j} is visited")
            
        print()
        if not stack.is_empty():
            print("Solved!")
            self.maze[self.ex][self.ey] = '.'
        else: 
            print("Could not solved!")
            
        print()
        self.print_maze()


if __name__ == "__main__":
    maze = Maze()
    maze.solve()
