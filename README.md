# List Comprehensions

Instructions: The number of insects in a lab doubles in size every month.
Take the initial number of insects as input and output a list, showing the number of insects for each of the next 12 months, starting with 0, which is the initial value.
So, the resulting list should contain 12 items, each showing the number of insects at the beginning of that month.

Sample Input:
10

Sample Output:
[10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240, 20480]

Create a list comprehension to generate the required list.

Psuedocode:





            BEGIN
            
              INPUT number_of_insects "Please enter number of insects: "

              FOR each in range 12
                PRINT the number_of_insects

                # do the calculations - for each of the index in the range, do this:
                number_of_insects = number_of_insects multiplies to 2

              ENDFOR

            END