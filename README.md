# Matrix Inverse Calculator
This Python program computes the inverse of a square matrix using the Gauss-Jordan elimination method. The program prompts the user to enter the number of rows and columns of the matrix, and then asks the user to enter the elements of the matrix row by row.

The program checks if the matrix is square and if not, it prints an error message . If the matrix is square, the program initializes the inverse matrix to the identity matrix and applies the Gauss-Jordan elimination method to transform the matrix to its row echelon form.

The program then applies the Gauss-Jordan elimination method again, but in reverse order, to obtain the reduced row echelon form of the inverse matrix. It divides each row of the inverse matrix by its leading coefficient to obtain the final inverse matrix.\

## Here's a brief description of each function:

* start(): This function prompts the user to enter the number of rows and columns of the matrix. It checks if the matrix is square (i.e., the number of rows and 
  columns are the same). If the matrix is not square, the function prints an error message . Otherwise, it returns the dimensions of the matrix as a tuple.

* inp(r,c): This function prompts the user to enter the elements of the matrix row by row and initializes the inverse matrix to the identity matrix. It returns the 
  matrix and its inverse as two nested lists.

* singular(m): This function checks if the matrix is singular (i.e., has a determinant of zero) by summing the elements in the last row. If the sum is zero, the 
  function prints a message and exits the program.

* position(m,inverse): This function reorders the rows of the matrix and its inverse so that all the leading coefficients (the first non-zero element in each row) 
  are in the upper left corner of the matrix. This is a preprocessing step before applying the Gauss-Jordan elimination method.

* echelon(m,inverse,r): This function applies the Gauss-Jordan elimination method to the matrix and its inverse to transform the matrix to its  row echelon 
  form. It returns the  row echelon form of the matrix and its inverse as two nested lists.

* rrec(m,inverse,r): This function applies the Gauss-Jordan elimination method to the matrix and its inverse again, but in reverse order, to obtain the reduced row 
  echelon form of the inverse matrix. It then divides each row of the inverse matrix by its leading coefficient to obtain the final inverse matrix.

The main program uses these functions to compute the inverse of a matrix entered by the user, and prints the inverse matrix to the console.

Note that the position() function has been modified from the previous version of the code to also reorder the rows of the inverse matrix along with the matrix itself. This ensures that the inverse matrix is correctly transformed throughout the rest of the computation.


