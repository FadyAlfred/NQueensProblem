x = []
solutions = []

def can_place(row, column):
    for i in range(row):
        if x[i] == column or i-x[i] == row-column or i+x[i] == row+column:
            return False
    return True


def place(row, number):
    for column in range(number):
        if can_place(row, column):
            try:
                x[row] = column
            except:
                x.append(column)
            if row == number-1:
                print (x)
                solutions.append(x[:])
                print (solutions)
                #print x
                break
            else:
                place(row+1, number)

def call_place(rows):
    place(0, rows)
    return solutions

