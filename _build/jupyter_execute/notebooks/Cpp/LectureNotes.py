#!/usr/bin/env python
# coding: utf-8

# <!-- dom:TITLE: Computational Physics:  Teach yourself C++ -->
# # Computational Physics:  Teach yourself C++
# <!-- dom:AUTHOR: Morten Hjorth-Jensen at Department of Physics, University of Oslo & Department of Physics and Astronomy and National Superconducting Cyclotron Laboratory, Michigan State University -->
# <!-- Author: -->  
# **Morten Hjorth-Jensen**, Department of Physics, University of Oslo and Department of Physics and Astronomy and National Superconducting Cyclotron Laboratory, Michigan State University
# 
# Date: **Aug 19, 2021**
# 
# Copyright 1999-2021, Morten Hjorth-Jensen. Released under CC Attribution-NonCommercial 4.0 license
# 
# 
# 
# 
# ## Getting Started, compiling and linking first
# 
# The programming language C++ is a so-called [compiled language](https://en.wikipedia.org/wiki/Compiled_language). For help on how to use C++, we recommend highly the [cpplus website](http://www.cplusplus.com/). 
# 
# 
# Assume we already have a program file, say **myprogram.cpp**. Note that C++ files have the extension **.cpp**.
# 
# Here we discuss first how to obtain an executable without using IDEs like [QT](https://www.qt.io/) creator or other types of integrated development environments ([Visual Studio](https://www.visualstudio.com/) or other, see [list here](https://sourceforge.net/directory/development/ide/) etc).
# 
# 
# It means that you need to compile the program (translate the human-like instructions into machine code) and link the resulting compiled file (a so-called **object** file) with various libraries in order to obtain an executable file. 
# 
# In order to obtain an executable file for a C++ program, the following
# instructions under Unix/Linux can be used ([similar instructions apply to windows-like environments using DOS](https://msdn.microsoft.com/en-us/library/ms235639.aspx)).
# 
# First you need to open a terminal on your Unix/Linux PC/laptop. You need also to have a C++ compiler installed. To check on Unix/Linux whether a C++ is installed or not simply type (in the terminal window)

#         which c++
# 

# If you get something like

#         Mortens-MacBook-Pro:~ hjensen$ which c++
#         /usr/bin/c++
# 

# you are ok. 
# Then compile and link your program as

#         c++ -c -Wall myprogram.cpp
#         c++ -o myprogram.exe  myprogram.o
# 

# where the compiler is called through the command c++/g++. The compiler
# option -Wall means that a warning is issued in case of non-standard
# language. The executable file is in this case **myprogram.exe**. The option
# `-c` is for compilation only, where the program is translated into machine code,
# while the `-o` option links the produced object file **myprogram.o** with other libraries 
# and produces the executable **myprogram.exe**.
# 
# You can skip the first step by simply writing

#         c++ -o myprogram.exe  myprogram.cpp
# 

# Also, to speed up the code use compile options like (compiler flags will be dealt with later)

#         c++ -O3 -c -Wall myprogram.cpp
# 

# To run your program, simply write

#         myprogram.exe
# 

# or if you wish to avoid creating executables which by accident have the same name as operating system commands (with sometime fatal consequences) write

#         ./myprogram.exe
# 

# Here, using . denotes the current directory. Since you want to run a file in your current directory and that directory is not in your $PATH, you need the ./ bit to tell the shell where the executable is.
# 
# 
# 
# Under Linux/Unix it is often convenient to create a
# so-called makefile, which is a script which includes possible
# compiling commands.  By clicking on the link here you can see examples of [makefiles](https://www.gnu.org/software/make/manual/make.html). 
# 
# 
# If you name your file for **makefile**, simply type the command
# **make** and Linux/Unix executes all possible statements included in your makefile. 
# 
# When you use an IDE like Qt, it creates automatically something similar to a makefile for you and you don't need to hardcode the above statements. 
# 
# 
# 
# 
# Our first program is the classic [Hello World](https://github.com/CompPhysics/ComputationalPhysicsMSU/blob/master/doc/Programs/LecturePrograms/programs/IntroProgramming/cpp/hellow.cpp).
# 
# Here we present the C++ version using **namespace**, see shortly below here for an explanation.

#         // A comment line begins like this in C++ programs
#         // Standard ANSI-C++ include files
#         #include <cstdlib> // atof function 
#         #include <iostream>   // input and output
#         #include <cmath>      // math functions
#         using namespace std;
#         int main (int argc, char* argv[])
#         {
#           // convert the text argv[1] to double using atof:
#           double r = atof(argv[1]);  // convert the text argv[1] to double
#           double s = sin(r);
#           cout << "Hello, World! sin(" << r << ") =" << s << endl;
#           return 0;           // success execution of the program 
#         }
# 

# The compiler must see a declaration of a function before you can
# call it (the compiler checks the argument and return types).
# The declaration of library functions appears
# in so-called "header files" that must be included in the program, as an example the following statement includes the so-called **Standard Library Functions**

#            #include <cstdlib> // atof function 
# 

# We call three functions (atof, sin, cout)
# and these are declared in three different header files. These declarations should come first. The **cout** function is included in the **isostream**. In C++, input and output (I/O) operations  are performed by using so-called streams which a *stream of data* where a  stream is an object with properties that are defined by a class. Global objects are predefined for the standard I/O channels.   The **sin** function is defined by the **cmath** library and its header file and needs to be included. For those of you familiar with **Python** this is similar to

# In[1]:


from math import sin


# [The main program is a function called main](http://en.cppreference.com/w/cpp/language/return)
# with a return value set to an integer, int (0 if success).
# The operating system stores the return value,
# and other programs/utilities can check whether
# the execution was successful or not. The main program has thus to be declared as **int main()** in standard C++. 
# The command-line arguments are transferred to the main function through

#            int main (int argc, char* argv[])
# 

# The command-line arguments are transferred to the main function through

#            int main (int argc, char* argv[])
# 

# The integer **argc** is the number  of command-line arguments (two in our case) while
# **argv** is a vector of strings containing the command-line arguments
# with _argv[0]_ containing  the name of the program
# and _argv[1]_, _argv[2]_, ... are the command-line args, i.e., the number of
# arguments that are  inputs to the program.
# 
# We define floating point variables, see also below,
# through the keywords **float** for single precision real numbers and
# **double** for double precision real numbers. The function
# **atof** transforms a text string to a float, either single or double precision.
# The **sine** function is declared in **cmath**, a library which
# is not automatically included and needs to be linked when computing
# and producing the  executable file. Note that arrays in C++ begin by default with $0$. The first element is here _argv[0]_. 
# 
# A one-dimensional array like **argv** can be defined statically or dynamically. To reserve space in memory statically means defining a variable of this type as

#         char argv[10]; 
# 

# which contains in this case ten elements. Each element has a specific address in memory, see the discussions below on pointers. We anticipate partly the discussion here by declaring a pointer variable and allocating memory dynamically. In C++ this is done as

#         char *argv;  // declaring first a pointer
#         argv = new char[10];   // Now reserving space for  ten elements in memory for a character variable (4 bytes or 32 bits).
# 

# For a floating point variable of  8 bytes or 64 bits we would declare a similar array as

#         double *argv;  // declaring first a pointer
#         argv = new double[10];   // Now reserving space for  ten elements in memory for a character variable (4 bytes or 32 bits).
# 

# In similar ways we can declare integer variable, single precisions floats etc.
# We can write the above in one line as

#         double *argv = new double[10];   
# 

# After having compiled this program as

#         c++ -o hw.exe hellowd.cpp
# 

# we can run the executable and obtain

#         Mortens-MacBook-Pro:cpp hjensen$ ./hw.exe 0.5
#         Hello, World! sin(0.5) =0.479426
# 

# If we do not write the value of $x$ on the command line we would get

#         Mortens-MacBook-Pro:cpp hjensen$ ./hw.exe 
#         Segmentation fault: 11
# 

# In this case, since reading from the command line with a number of arguments defined by the number of elements in the array _argv[]_, trying to access _argv[1]_ results in a segmentation fault. In the last case there is only one command line argument, the name of the executable program. It means that we have only the array element _argv[0]_. The element _argv[1]_ is not defined and we are trying to access something which is outside the memory slots reserved for _argv[]_. 
# 
# We can rewrite our [Hello World without the namespace usage](https://github.com/CompPhysics/ComputationalPhysicsMSU/blob/master/doc/Programs/LecturePrograms/programs/IntroProgramming/cpp/hellownonamespace.cpp). 
# 
# Namespaces provide a method for preventing name conflicts in large projects and 
# symbols declared inside a namespace block are placed in a named scope that prevents them from being mistaken for identically-named symbols in other scopes.
# Multiple namespace blocks with the same name are allowed. All declarations within those blocks are declared in the named scope.  This author likes to limit the usage of namespace to some few libraries, like the standard C library **csdtlib**. 
# 
# 
# Here we present the C++ version without using namespace.

#         // A comment line begins like this in C++ programs
#         // Standard ANSI-C++ include files
#         #include <cstdlib> // atof function 
#         #include <iostream>   // input and output
#         #include <cmath>      // math functions
#         
#         int main (int argc, char* argv[])
#         {
#           // convert the text argv[1] to double using atof:
#           double r = atof(argv[1]);  // convert the text argv[1] to double
#           double s = sin(r);
#           // Note std::cout and std::endl
#           std::cout << "Hello, World! sin(" << r << ") =" << s << std::endl;
#           return 0;           // success execution of the program 
#         }
# 

# I personally tend to use **namespace** for input and output as I feel it increases the readability of my codes. Thus, all examples from here and on will have a statement like

#         using namespace std;
# 

# ## Brief summary
# 
#   * A C/C++ program begins with include statements of header files (libraries,intrinsic functions etc). This is similar to the **import** statement in Python.
# 
#   * Functions which are used are normally defined at the top (details below)
# 
#   * The main program is declared as an integer, it returns 0 (everything correct) or 1 (something went wrong)
# 
#   * Standard `if`, `while` and `for` statements as in Java, Fortran, Python...
# 
#   * A C/C++ array begins by indexing at 0!
# 
#   * Array allocations are done by size, not by the final index value.If you allocate an array with 10 elements, you should index them from $0,1,\dots, 9$.
# 
#   * Initialize always an array before a computation.
# 
# ### From decimal to binary representation
# 
# Let us now write a program which translates an integer in the decimal representation to one in the binary representation. The mathematical formula for this is given by

# $$
# a_n2^n+a_{n-1}2^{n-1}  +a_{n-2}2^{n-2}  +\dots +a_{0}2^{0}.
# $$

# In binary notation we have thus $(417)_{10} =(110110001)_2$
# since we have

# $$
# \begin{align*}
# (110100001)_2
# &=1\times2^8+1\times 2^{7}+0\times 2^{6}+1\times 2^{5}+0\times 2^{4}+0\times 2^{3}\\
# &+0\times 2^{2}+0\times 2^{2}+0\times 2^{1}+1\times 2^{0}.
# \end{align*}
# $$

# To see this, we have performed the following divisions by 2
# 
# <table border="1">
# <tr></tr>
# <tbody>
# <tr><td align="center">   417/2=208    </td> <td align="center">   remainder 1    </td> <td align="center">   coefficient of $2^{0}$ is 1    </td> </tr>
# <tr><td align="center">   208/2=104    </td> <td align="center">   remainder 0    </td> <td align="center">   coefficient of $2^{1}$ is 0    </td> </tr>
# <tr><td align="center">   104/2=52     </td> <td align="center">   remainder 0    </td> <td align="center">   coefficient of $2^{2}$ is 0    </td> </tr>
# <tr><td align="center">   52/2=26      </td> <td align="center">   remainder 0    </td> <td align="center">   coefficient of $2^{3}$ is 0    </td> </tr>
# <tr><td align="center">   26/2=13      </td> <td align="center">   remainder 1    </td> <td align="center">   coefficient of $2^{4}$ is 0    </td> </tr>
# <tr><td align="center">   13/2= 6      </td> <td align="center">   remainder 1    </td> <td align="center">   coefficient of $2^{5}$ is 1    </td> </tr>
# <tr><td align="center">   6/2= 3       </td> <td align="center">   remainder 0    </td> <td align="center">   coefficient of $2^{6}$ is 0    </td> </tr>
# <tr><td align="center">   3/2= 1       </td> <td align="center">   remainder 1    </td> <td align="center">   coefficient of $2^{7}$ is 1    </td> </tr>
# <tr><td align="center">   1/2= 0       </td> <td align="center">   remainder 1    </td> <td align="center">   coefficient of $2^{8}$ is 1    </td> </tr>
# </tbody>
# </table>
# 
# Let us now look at the [code which takes as input from the command line a number in the decimal representation and converts it into the binary representation](https://github.com/CompPhysics/ComputationalPhysicsMSU/blob/master/doc/Programs/LecturePrograms/programs/IntroProgramming/cpp/program2.cpp)

#         #include <iostream>
#         #include <cmath>
#         #include <cstdio>
#         #include <cstdlib>
#         using namespace std;
#         int main (int argc, char* argv[])
#         {
#           int terms[32]; // storage of a0, a1, etc, up to 32 bits
#           int number = atoi(argv[1]); 
#           // initialise the term a0, a1 etc
#           for (int i=0; i < 32 ; i++) terms[i] = 0;
#           for (int i=0; i < 32 ; i++){ 
#             terms[i] = number%2;   // modulo division done by %
#             number /= 2; 
#           }
#           // write out results
#           cout << "Number of bytes used= " << sizeof(number) << endl;
#           for (i=0; i < 32 ; i++){ 
#             cout << " Term nr: " << i << "Value= " << terms[i];
#             cout << endl;
#           }
#           return 0;  
#         }
# 

# To be noted here is the way we define a loop in C++. Our first encounter is

#           for (i=0; i < 32 ; i++){ terms[i] = 0;}
# 

# The loop starts with the **for** declaration, followed by a parenthesis hwere we declare the starting values (**i=0**) and the end value
# (**i < 32**). What would have happened if we declared the endpoint as **i <=32**?  
# 
# This loop is just a oneliner that serves to initialize the array _terms[]_ to zero. Note the way we can write increment by one via **i++**.
# 
# Our next loop

#           for (int i=0; i < 32 ; i++){ 
#             terms[i] = number%2;   // modulo division done by %
#             number /= 2; 
#           }
# 

# contains the actual algorithm for the translation of an integer in the decimal representation to an integer in the binary representation. We note the way we use the curly parentheses to mark where the content inside a loop starts and where it ends. It is useful to introduce some indentation (many text editors do this automatically for you when the file ends with **.cpp**) in order to increase readability.
# 
# The function **sizeof()** tells how many bytes are used to store a given variable. An integer is by default defined in terms of four bytes or 32 bits. 
# 
# Our next example is a program that calculates the second derivative numerically  of a function (the exponential function here) and writes the result to a file declared by the user. The first thing to notice is declaration of the object **ofile** which inherits all functionality from the **ofstream** class. [This class](http://www.cplusplus.com/reference/fstream/ofstream/) (to be discussed later below in connection with classes) overloads functions like writing to file, opening files, closing files etc. A similar class exists, the **ifstream** class, for input variables. 
# Adding the header file **fstream** gives us access to the functionality of the **ofstream** class. 
# The **iomanip** header files allows to format our output with functions like **setprecision**, **setw** etc.

#         #include <iostream>
#         #include <cmath>
#         #include <fstream>
#         #include <iomanip>
#         // output file as global variable
#         ofstream ofile;
#         
#         // Begin of main program
#         
#         int main(int argc, char* argv[])
#         {
#           char *outfilename;
#           // Read in output file, abort if there are too few command-line arguments
#           if( argc <= 3 ){
#             cout << "Bad Usage: " << argv[0] <<
#               " read also output file, number of integration points and the final x values  on same line, four variables in total" << std::endl;
#             exit(1);
#           }
#           else{
#             outfilename=argv[1];
#           }
#           //  opening a file for the program
#           ofile.open(outfilename);
#           // extracting number of mesh points
#           int i = atoi(argv[2]);
#           double x = atof(argv[3]);  // reading x-value
#           double h = 1.0/((double) i); // setting up step size
#           double Derivative = (exp(x+h)-2.*exp(x)+exp(x-h))/(h*h);
#           double RelativeError = log10(fabs(Derivative-exp(x))/exp(x));
#           ofile <<  setw(15) << setprecision(8) << "relative error=" << RelativeError << endl;
#           ofile.close();  // close output file
#           return 0;
#         }
# 

# We have in addition included some safety valves here. In case we have less than four variables on the command line, the program aborts.
# After having read the name of the output file we open the file  and by default we can write to it via the statement

#           ofile.open(outfilename);
# 

# and we close it at the end by

#           ofile.close();
# 

# We have also defined how to write to file our result in a formatted way via the statement

#           ofile <<  setw(15) << setprecision(8) << "relative error=" << RelativeError << endl;
# 

# where we reserve a field width of 15 characters and a precision of eight leading digits after the decimal point.
# 
# The above example represents our first simple case where we write our results to file. Before we proceed now, we need to say something more about pointers. 
# 
# ## Technical Matter in C/C++: Pointers
# 
# Variables are stored in the memory of a computer and each location in memory is defined by a unique address. How is memory management done?
# 
# The main memory contains the program data
# * Cache memory contains a copy of the main memory data
# 
# * Cache is faster but consumes more space and power. It is normally assumed to be much faster than main memory
# 
# * Registers contain working data only
# 
#  * Modern CPUs perform most or all operations only on data in register
# 
# 
# * Multiple Cache memories contain a copy of the main memory data
# 
#  * Cache items accessed by their address in main memory
# 
#  * L1 cache is the fastest but has the least capacity
# 
#  * L2, L3 provide intermediate performance/size tradeoffs
# 
# 
# Loads and stores to memory can be as important as floating point operations when we measure performance.
# 
# 
# * Most communication in a computer is carried out in chunks, blocks of bytes of data that move together
# 
# * In the memory hierarchy, data moves between memory and cache, and between different levels of cache, in groups called lines
# 
#  * Lines are typically 64-128 bytes, or 8-16 double precision words
# 
#  * Even if you do not use the data, it is moved and occupies space in the cache
# 
# 
# * This performance feature is not captured in most programming languages
# 
# When we store variables in memory, each memory location is identified and referenced with an address (like a house number specifies where a particular family resides on a street).
# Pointers play a central role in understanding memory management in C++. A pointer is just another name for an address and a pointer specifies where a value resides in the computer's memory. 
# 
# A pointer points to an address not to a data container of any kind! It is a variable (with its own address in memory) whose value is the address of some other memory location. C++ as programming language offers several operations that allow us to access say elements of an array in an efficient way by accessing data by their addresses.
# 
# Let us look at some simple example declarations. We define four variables and each of them is storeed in memory schematically as shown here (think of every box as a slot in memory of say 32 bits or more for each slot)
# <table border="1">
# <thead>
# <tr><th align="center">int a</th> <th align="center">int b</th> <th align="center">double c</th> <th align="center">int d</th> <th align="center">double e</th> </tr>
# </thead>
# <tbody>
# <tr><td align="center">   112      </td> <td align="center">   -1       </td> <td align="center">   3.14        </td> <td align="center">   ?        </td> <td align="center">   ?           </td> </tr>
# </tbody>
# </table>
# We have put questions marks for the values of the variables **d** and **e**. 
# In the program here we define **a** and **b** as integers and **c** as a double. The variables **d** and **e** are declared as pointers.

#         #include <iostream>
#         using namespace std;
#         //  Declare functions before main
#         int main(int argc, char *argv[])
#         {
#           int a =112, b = -1;
#           double c = 3.14;
#           int *d = &a;
#           double  *e = &c;
#         
#           cout << "Address of the integer variable a :" << &a <<endl;
#           cout << "Value of the integer pointer variable d:" << d << endl;
#           cout << "Value which pointer d is pointing at :" << *d << endl;
#           cout << "Address of the double variable c :" << &c <<endl;
#           cout << "Value of the integer pointer variable e:" << e << endl;
#           cout << "Value which pointer e is pointing at :" << *e << endl;
#         
#         
#           return 0;
#         } // End: function main()
# 

# Running this [program](https://github.com/CompPhysics/ComputationalPhysicsMSU/blob/master/doc/Programs/LecturePrograms/programs/IntroProgramming/cpp/program11.cpp) we get the following

#         Address of the integer variable a :0x7fff56966a7c
#         Value of the integer pointer variable d:0x7fff56966a7c
#         Value which pointer d is pointing at :112
#         Address of the double variable c :0x7fff56966a70
#         Value of the integer pointer variable e:0x7fff56966a70
#         Value which pointer e is pointing at :3.14
# 

# we see that the value of **d** is the address of **a** and it points to the value $112$ stored in the memory slot reserved for **a**. Similarly, **e** is a pointer and gets as value the address of **c**, which is $0x7fff56966a70$ which points to the value of $3.14$. The operation

#           int *d = &a;
# 

# is called dereferencing. We could alternatively have written

#           int *d;
#           d = &a;
# 

# where the latter means that **d** gets as value the address of **a**. The print statement

#           cout << "Value which pointer d is pointing at :" << *d << endl;
# 

# then prints the actual number it points at, that is the vaue of the variable **a**.
# 
# [ Another pPointer example ](https://github.com/CompPhysics/ComputationalPhysicsMSU/blob/master/doc/Programs/LecturePrograms/programs/IntroProgramming/cpp/program7.cpp) is the following program

#         int main()
#         {
#           int var;
#           int *p;
#           p = &var;
#           var  = 421;
#           printf("Address of integer variable var : %p\n",&var);
#           printf("Its value: %d\n", var);
#           printf("Value of integer pointer p : %p\n",p);
#           printf("The value p points at :  %d\n",*p);
#           printf("Address of the pointer p : %p\n",&p);
#           return 0;
#         }
# 

# Dissecting it we have (now with the **printf** function from standard C)

#         int main()
#         {
#           int var;     // Define an integer variable var
#           int *p;      // Define a pointer to an integer
#           p = &var;    // Extract the address of var
#           var = 421;   // Change content of var
#           printf("Address of integer variable var : %p\n", &var);
#           printf("Its value: %d\n", var);  // 421
#           printf("Value of integer pointer p : %p\n", p);  // = &var
#           // The content of the variable pointed to by p is *p
#           printf("The value p points at :  %d\n", *p);
#           // Address where the pointer is stored in memory
#           printf("Address of the pointer p : %p\n", &p);
#           return 0;
#         }
# 

# and running the code we get

#         Address of integer variable var : 0x7fff5cfe6ae8
#         Its value: 421
#         Value of integer pointer p : 0x7fff5cfe6ae8
#         The value p points at :  421
#         Address of the pointer p : 0x7fff5cfe6ae0
# 

# We see again that the value of the pointer **p** is the address of the variable **var**. 
# 
# [The next pointer example](https://github.com/CompPhysics/ComputationalPhysicsMSU/blob/master/doc/Programs/LecturePrograms/programs/IntroProgramming/cpp/program8.cpp) deals with arrays and how to access array elements with pointer operations.

#         int matr[2];    // Define integer array with two elements
#         int *p;         // Define pointer to integer
#         p = &matr[0];   // Point to the address of the first element in matr
#         matr[0] = 321;  // Change the first element
#         matr[1] = 322;  // Change the second element
#         printf("\nAddress of matrix element matr[1]: %p", &matr[0]);
#         printf("\nValue of the  matrix element  matr[1]; %d", matr[0]);
#         printf("\nAddress of matrix element matr[2]: %p", &matr[1]);
#         printf("\nValue of the matrix element  matr[2]: %d\n", matr[1]);
#         printf("\nValue of the pointer p: %p", p);
#         printf("\nThe value p points to: %d", *p);
#         printf("\nThe value that (p+1) points to  %d\n", *(p+1));
#         printf("\nAddress of pointer p : %p\n", &p);
# 

# Here we define an array with two elements. The pointer **p** gets as value the address of the first element. The output of this program is

#         Address of the matrix element matr[1]: 0xbfffef70
#         Value of the  matrix element  matr[1]; 321
#         Address of the matrix element matr[2]: 0xbfffef74
#         Value of the matrix element  matr[2]: 322
#         Value of the pointer: 0xbfffef70
#         The value pointer points at: 321
#         The value that (pointer+1) points at:  322
#         Address of the pointer variable : 0xbfffef6c
# 

# We note that the operation

#         printf("\nThe value that (p+1) points to  %d\n", *(p+1));
# 

# allows us to print the address of the second array element. This is the way we can use pointers to access array elements.
# 
# Let us now discuss another subtle issue, that is transfer of data using call by value and call by reference, shown in the [program here](https://github.com/CompPhysics/ComputationalPhysicsMSU/blob/master/doc/Programs/LecturePrograms/programs/Classes/cpp/program6.cpp).

#         #include <iostream>
#         using namespace std;
#         //  Declare functions before main
#         void func(int, int*);
#         int main(int argc, char *argv[]) 
#         {
#           int a; 
#           int *b;
#           a = 10;
#           b = new int[10];
#           for(int i = 0; i < 10; i++) {
#             b[i] = i;
#             cout <<  b[i] << endl;
#           }
#           // the variable a is transferred by call by value. This means
#           //  that the function func cannot change a in the calling function
#           func( a,b);
#           
#           delete [] b ; 
#           return 0;
#         } // End: function main()
#         
#         void func( int x, int *y) 
#         {
#           // a becomes locally x  and it can be changed locally
#           x+=7;
#           //  func gets the address of the first element of y (b)
#           // it changes y[0] to 10 and when returning control to main
#           // it changes also b[0]. Call by reference
#           *y += 10;  //  *y = *y+10;
#           //  explicit element 
#           y[6] += 10;
#           //   in this function y[0]  and y[6] have been changed and when returning 
#           // control to main  this means that b[0] and b[6] are changed.  
#           return;
#         } // End: function func()
#         
# 

# There are several things to notice here. First, we have now declared a function **func**. This declaration is placed before the main function. If we don't do that the main function does not know how this function is to be used. The function takes as input an integer and an integer pointer defined by the asterix in

#         void func(int, int*);
# 

# This means that we transfer an address (in this case the address of the first element of the pointer **b**). This is called **call by reference**.
# It means that the function **func** can change the value of **b** upon returning the instruction pointer to the main program (or calling function).
# The other variable is transferred through what we label as  **call by value**. In this case the called function can change the value of **a** locally but cannot change the value of this variable in the calling function.
# The function **func** func gets the address of the first element of y (b) and changes y[0] to 10 and when returning control to main
# it changes also b[0]. This is done via

#           *y += 10;  
# 

# This changes only the first element. To change another element, we would write (unless we use pointer operations)

#           y[6] += 10;
# 

# which changes $\mathbf{y[6]}$  to $16$, since its orginal value was $6$, as defined in the main function. Using pointer operations we could write this as

#           *(y+6) += 10;
# 

# and it produces the same result. It states that the value of the element which resides in $\mathbf{y[6]}$ is to be changed to $16$. 
# 
# 
# C++ allows the programmer to use solely call by reference (note that call by reference is implemented as pointers). To see the difference between C and C++, consider the following simple examples.
# In C we would write

#            int n; n =8;
#            func(&n); /* &n is a pointer to n */
#            ....
#            void func(int *i)
#            {
#              *i = 10; /* n is changed to 10 */
#              ....
#            }
# 

# whereas in C++ we would write

#            int n; n =8;
#            func(n); // just transfer n itself
#            ....
#            void func(int& i)
#            {
#              i = 10; // n is changed to 10
#              ....
#            }
# 

# The reason why we emphasize the difference between call by value and call
# by reference is that it allows the programmer to avoid pitfalls
# like unwanted changes of variables. However, many people feel that this
# reduces the readability of the code.
# 
# 
# 
# 
# Let us look at further Example codes in C++, with writing to file and [dynamic allocation for arrays](https://github.com/CompPhysics/ComputationalPhysicsMSU/blob/master/doc/Programs/LecturePrograms/programs/Classes/cpp/program5.cpp)

#         #include <iostream>
#         #include <cmath>
#         #include <fstream>
#         #include <iomanip>
#         using namespace std; 
#         
#         // output file as global variable
#         
#         ofstream ofile;  
#         
#         // Begin of main program   
#         
#         int main(int argc, char* argv[])
#         {
#           char *outfilename;
#           // Read in output file, abort if there are too few command-line arguments
#           if( argc <= 2 ){
#             cout << "Bad Usage: " << argv[0] << 
#               " read also output file and number of elements on same line" << endl;
#             exit(1);
#           }
#           else{
#             outfilename=argv[1];
#           }
#         
#           //  opening a file for the program
#           ofile.open(outfilename); 
#           int i = atoi(argv[2]); 
#          /* we can define it as 
#           int *a;
#           a = new int[i];
#           or as
#          */
#           double *a = new double[i]; 
#           cout << " bytes for i=" << sizeof(i) << endl;
#           for (int j = 0; j < i; j++) {
#             a[j] = j*exp(2.0);
#             // ofile instead of cout
#             ofile << setw(15) << setprecision(8) << "a=" << a[j] << endl;
#           }
#           delete [] a; // free memory
#           ofile.close();  // close output file
#           return 0;
#         }
#         
# 

# Here we read from the command line the number of elements **i** via

#           int i = atoi(argv[2]); 
# 

# and allocate memory dynamically by declaring a pointer array (a vector here) **a** using

#           double *a = new double[i];
# 

# Using dynamic memory allocation we actually allow  memory to be more flexibly and explicitly managed.
# When the memory is no longer needed, the pointer is passed to free which deallocates the memory so that it can be used for other purposes. This is done by the **delete** statement

#           delete [] a; // free memory
# 

# In the loop

#           for (int j = 0; j < i; j++) {
#             a[j] = j*exp(2.0);
#             // ofile instead of cout
#             ofile << setw(15) << setprecision(8) << "a=" << a[j] << endl;
#           }
# 

# we assign a specific value to each array element and print to file. 
# 
# If we wish to time our function, the following [program](https://github.com/CompPhysics/ComputationalPhysicsMSU/blob/master/doc/Programs/LecturePrograms/programs/Classes/cpp/program7.cpp) gives a typical example.

#         #include <cstdlib>
#         #include <iostream>
#         #include <cmath>
#         #include <iomanip> 
#         #include "time.h"   // Not the use time.h
#         
#         using namespace std; // note use of namespace                                       
#         int main (int argc, char* argv[])
#         {
#           int i = atoi(argv[1]); 
#           double *a, *b, *c;
#           a = new double[i]; 
#           b = new double[i]; 
#           c = new double[i]; 
#         
#           clock_t start, finish;
#           start = clock();
#           for (int j = 0; j < i; j++) {
#             a[j] = cos(j*1.0);
#             b[j] = sin(j+3.0);
#             c[j] = 0.0;
#           }
#           for (int j = 0; j < i; j++) {
#             c[j] = a[j]+b[j];
#           }
#           finish = clock();
#           double timeused = (double) (finish - start)/(CLOCKS_PER_SEC );
#           cout << setiosflags(ios::showpoint | ios::uppercase);
#           cout << setprecision(10) << setw(20) << "Time used  for vector addition=" << timeused  << endl;
#           delete [] a;
#           delete [] b;
#           delete [] c;
#           return 0;           /* success execution of the program */
#         }
# 

# When timing the program, you should carefully plan what to time. Here we calculate the time difference from the point where we start filling in the three arrays **a**, **b** and **c** defining the starting time as

#           clock_t start, finish;
#           start = clock();
#           for (int j = 0; j < i; j++) {
# 

# The final time is when all operations we are interested in are concluded, namely at

#           for (int j = 0; j < i; j++) {
#             c[j] = a[j]+b[j];
#           }
#           finish = clock();
# 

# The time difference from start to end, with its granularity is defined as

#           double timeused = (double) (finish - start)/(CLOCKS_PER_SEC );
# 

# When timing a program you should pay attention to the following:
# 1. Timers are not infinitely accurate
# 
# 2. All clocks have a granularity, the minimum time that they can measure
# 
# 3. The error in a time measurement, even if everything is perfect, may be the size of this granularity (sometimes called a clock tick)
# 
# 4. Always know what your clock granularity is
# 
# 5. Ensure that your measurement is for a long enough duration (say 100 times the **tick**)
# 
# What happens when the code is executed? The assumption is that the code is ready to
# execute. But
# 1. Code may still be on disk, and not even read into memory.
# 
# 2. Data may be in slow memory rather than fast (which may be wrong or right for what you are measuring)
# 
# 3. Multiple tests often necessary to ensure that cold start effects are not present
# 
# 4. Special effort often required to ensure data in the intended part of the memory hierarchy.
# 
# You should thus think of a numerical calculation as an experiment. To provide benchmark times you should thus run the timing measurement several times and then take the average over a series of simulations. 
# 
# 
# ## Using **strings** instead of characters
# 
# Till now we have used character variables when declaring for example filenames for output or input files. C++ offers a compact and flexible way of dealing with text strings through the **string** class. In the program below we wish for example to define several output files for our calculations byapending  to a basename read in on the command line various endings. These endings can then be used to recognize a specific calculation.
# Here we read the basic name of an ouput file and add to it the actual exponent used in a calculation by appending it to the file name. We show only the relevant parts

#         #include <iostream>
#         #include <fstream>
#         #include <iomanip>
#         #include <cmath>
#         #include <string>
#         // use namespace for output and input
#         using namespace std;
#         
#         // object for output files
#         ofstream ofile;
#         
#         
#         // Begin main program
#         int main(int argc, char *argv[]){
#           int exponent; 
#             string filename;
#             // We read also the basic name for the output file and the highest power of 10^n we want
#             if( argc <= 1 ){
#                   cout << "Bad Usage: " << argv[0] <<
#                       " read also file name on same line and max power 10^n" << endl;
#                   exit(1);
#             }
#                 else{
#                 filename = argv[1]; // first command line argument after name of program
#                 exponent = atoi(argv[2]);
#             }
#             // Loop over powers of 10
#             for (int i = 1; i <= exponent; i++){
#               int  n = (int) pow(10.0,i);
#               // Declare new file name
#               string fileout = filename;
#               // Convert the power 10^i to a string
#               string argument = to_string(i);
#               // Final filename as filename-i- by appending the power of 10
#               fileout.append(argument);
#               ofile.open(fileout);
#               ofile << setiosflags(ios::showpoint | ios::uppercase);
#               //   Do something 
#               ofile.close();  // close output file wth given ending
#             }
#             return 0;
#         }
# 

# Instead of our earlier definition

#           char *outfilename;
# 

# we define now the same output file via the **string** statement, inheriting thus all functionality of the **string** class by writing

#             string filename;
# 

# In the statement

#             filename = argv[1]; 
# 

# the variable **filename** gets the name of file we declared on the command line.
# A new file for the specific calculation is then established via

#               // Declare new file name
#               string fileout = filename;
#               // Convert the power 10^i to a string
#               string argument = to_string(i);
#               // Final filename as filename-i- by appending the power of 10
#               fileout.append(argument);
#               ofile.open(fileout);  // then open
# 

# We recommend using the **string** class, it gives ou much more flexibility in handling strings. 
# 
# ## Matrices in C++
# Another quantity we end up using again and again are matrices.
# We have  an $N\times N$ matrix A  with $N=100$
# In C/C++ this would be  defined as

#            int N = 100;
#            double A[100][100];
#            //   initialize all elements to zero
#            for(i=0 ; i < N ; i++) {
#               for(j=0 ; j < N ; j++) {
#                  A[i][j] = 0.0;
#         
# 

# Note the way the matrix is organized, row-major order.
# 
# We have  $N\times N$ matrices A, B and C and we wish to
# evaluate $A=B+C$.

# $$
# \mathbf{A}= \mathbf{B}\pm\mathbf{C}  \Longrightarrow a_{ij} = b_{ij}\pm c_{ij},
# $$

# In C/C++ this would be coded like

#            for(i=0 ; i < N ; i++) {
#               for(j=0 ; j < N ; j++) {
#                  a[i][j] = b[i][j]+c[i][j]
#         
# 

# We have  $N\times N$ matrices A, B and C and we wish to
# evaluate $A=BC$.

# $$
# \mathbf{A}=\mathbf{BC}   \Longrightarrow a_{ij} = \sum_{k=1}^{n} b_{ik}c_{kj},
# $$

# In C/C++ this would be coded like

#            for(i=0 ; i < N ; i++) {
#               for(j=0 ; j < N ; j++) {
#                  for(k=0 ; k < N ; k++) {
#                     a[i][j]+=b[i][k]*c[k][j];
#         
# 

# The above matrices were all declared statically.
# For dynamic memory allocation in C++ there are 
# several  possibilities
# 
#   * Do it yourself
# 
#   * Use the functions provided in the library package [lib.cpp](https://github.com/CompPhysics/ComputationalPhysics/blob/master/doc/Programs/LecturePrograms/programs/cppLibrary/lib.cpp)
# 
#   * Use Armadillo <http://arma.sourceforgenet> (a C++ linear algebra library, discussion both here and at lab). 
# 
#   * Write yur own matrix-vector class (to be discussed later.
# 
# A matrix in C++ is a double pointer, a pointer to a pointer. Here is how you would do it yourself.

#         int N;
#         double **  A;
#         A = new double*[N]
#         for ( i = 0; i < N; i++)
#             A[i] = new double[N];
# 

# Always free space when you don't need an array anymore.

#         for ( i = 0; i < N; i++)
#             delete[] A[i];
#         delete[] A;
# 

# Before we discuss a library like Armadillo (see below) and classes (we will discuss how to write our own matrix-vector class) it is instructive to look at the following two examples. The first program is an example of a single **main** function where we allocate and deallocate memory for three matrices using what we will call the basic C++ way of allocating and deallocating matrices. 
# "The first program[:](https://github.com/CompPhysics/ComputationalPhysicsMSU/blob/master/doc/Programs/LecturePrograms/programs/Classes/cpp/program9.cpp) is listed here. Both programs  compute the Froebenius norm of a matrix given by

# 4
#  
# <
# <
# <
# !
# !
# M
# A
# T
# H
# _
# B
# L
# O
# C
# K

#         #include <cstdlib>
#         #include <iostream>
#         #include <cmath>
#         #include <iomanip>
#         #include "time.h"
#         
#         using namespace std; // note use of namespace
#         int main (int argc, char* argv[])
#         {
#           // read in dimension of square matrix
#           int n = atoi(argv[1]);
#           double s = 1.0/sqrt( (double) n);
#           double **A, **B, **C;
#           // Start timing
#           clock_t start, finish;
#           start = clock();
#           // Allocate space for the three matrices
#           A = new double*[n]; B = new double*[n]; C = new double*[n];
#           for (int i = 0; i < n; i++){
#             A[i] = new double[n];
#             B[i] = new double[n];
#             C[i] = new double[n];
#           }
#           // Set up values for matrix A and B and zero matrix C
#           for (int i = 0; i < n; i++){
#             for (int j = 0; j < n; j++) {
#               double angle = 2.0*M_PI*i*j/ (( double ) n);
#               A[i][j] = s * ( sin ( angle ) + cos ( angle ) );
#               B[j][i] =  A[i][j];
#             }
#           }
#           // Then perform the matrix-matrix multiplication
#           for (int i = 0; i < n; i++){
#             for (int j = 0; j < n; j++) {
#               double sum = 0.0;
#                for (int k = 0; k < n; k++) {
#                    sum += B[i][k]*A[k][j];
#                }
#                C[i][j] = sum;
#             }
#           }
#           // Compute now the Frobenius norm
#           double Fsum = 0.0;
#           for (int i = 0; i < n; i++){
#             for (int j = 0; j < n; j++) {
#               Fsum += C[i][j]*C[i][j];
#             }
#           }
#           Fsum = sqrt(Fsum);
#           finish = clock();
#           double timeused = (double) (finish - start)/(CLOCKS_PER_SEC );
#           cout << setiosflags(ios::showpoint | ios::uppercase);
#           cout << setprecision(10) << setw(20) << "Time used  for matrix-matrix multiplication=" << timeused  << endl;
#           cout << "  Frobenius norm  = " << Fsum << endl;
#           // Free up space
#           for (int i = 0; i < n; i++){
#             delete[] A[i];
#             delete[] B[i];
#             delete[] C[i];
#           }
#           delete[] A;
#           delete[] B;
#           delete[] C;
#           return 0;
#         }
# 

# Here we have defined three different matrices which we have declared as double pointers

#           // Allocate space for the three matrices
#           A = new double*[n]; B = new double*[n]; C = new double*[n];
#           for (int i = 0; i < n; i++){
#             A[i] = new double[n];
#             B[i] = new double[n];
#             C[i] = new double[n];
#           }
#         ....
#         // and finally we free space
#           // Free up space
#           for (int i = 0; i < n; i++){
#             delete[] A[i];
#             delete[] B[i];
#             delete[] C[i];
#           }
#           delete[] A;
#           delete[] B;
#           delete[] C;
# 

# The matrices are defined as real $n\times n$ matrices. It is easy to imagine that if we are to need many more matrices either in the main function or other user defined functions, we would have to write these operations again and again. This is something which can easily lead to errors. In the [next program](https://github.com/CompPhysics/ComputationalPhysicsMSU/blob/master/doc/Programs/LecturePrograms/programs/Classes/cpp/program10.cpp)  we have written four functions that allow us to hide these operations. 
# Two of the functions allocate and deallocate memory for a matrix declared as a floating point variable, while the other two functions do the same for an integer type matrix. The allocation functions for the doubles and integers are practically identical except for the the matrices being either doubles or integer. This is not a very elegant way of programming. 
# With classes we can generalize these operations to just two functions, as well as being able to add much more functionality. 
# We will come back to this below. Our new program

#         // This program uses its own function for allocating and freeing memory for matrices
#         // It can be seen as an intermediate step towards the construction of a more general 
#         // matrix vector class
#         
#         #include <cstdlib>
#         #include <iostream>
#         #include <cmath>
#         #include <iomanip>
#         #include "time.h"
#         
#         //  Declaring functions to allocate and free space for a matrix
#         
#         double ** CreateMatrix(int m, int n);
#         void DestroyMatrix(double ** mat, int m, int n); 
#         
#         int ** ICreateMatrix(int m, int n);
#         void IDestroyMatrix(int ** mat, int m, int n);
#         
#         
#         using namespace std; // note use of namespace
#         int main (int argc, char* argv[])
#         {
#           // read in dimension of square matrix
#           int n = atoi(argv[1]);
#           double s = 1.0/sqrt( (double) n);
#           double **A, **B, **C;
#           // Start timing
#           clock_t start, finish;
#           start = clock();
#           // Allocate space for the three matrices
#           A = CreateMatrix(n, n);
#           B = CreateMatrix(n, n);
#           C = CreateMatrix(n, n);
#           // Set up values for matrix A and B and zero matrix C
#           for (int i = 0; i < n; i++){
#             for (int j = 0; j < n; j++) {
#               double angle = 2.0*M_PI*i*j/ (( double ) n);
#               A[i][j] = s * ( sin ( angle ) + cos ( angle ) );
#               B[j][i] =  A[i][j];
#             }
#           }
#           // Then perform the matrix-matrix multiplication
#           for (int i = 0; i < n; i++){
#             for (int j = 0; j < n; j++) {
#               double sum = 0.0;
#                for (int k = 0; k < n; k++) {
#                    sum += B[i][k]*A[k][j];
#                }
#                C[i][j] = sum;
#             }
#           }
#           // Compute now the Frobenius norm
#           double Fsum = 0.0;
#           for (int i = 0; i < n; i++){
#             for (int j = 0; j < n; j++) {
#               Fsum += C[i][j]*C[i][j];
#             }
#           }
#           Fsum = sqrt(Fsum);
#           finish = clock();
#           double timeused = (double) (finish - start)/(CLOCKS_PER_SEC );
#           cout << setiosflags(ios::showpoint | ios::uppercase);
#           cout << setprecision(10) << setw(20) << "Time used  for matrix-matrix multiplication=" << timeused  << endl;
#           cout << "  Frobenius norm  = " << Fsum << endl;
#           // Free up space
#           DestroyMatrix(A, n, n);   DestroyMatrix(B, n, n);   DestroyMatrix(C, n, n);
#           return 0;
#         }
#         
#         
#         //  Allocating space for a double type matrix
#         double ** CreateMatrix(int m, int n){
#           double ** mat;
#           mat = new double*[m];
#           for(int i=0;i<m;i++){
#             mat[i] = new double[n];
#             for(int j=0;j<m;j++)
#               mat[i][j] = 0.0;
#           }
#           return mat;
#         }
#         
#         //  Allocating space for an integer type  matrix
#         int ** ICreateMatrix(int m, int n){
#           int ** mat;
#           mat = new int*[m];
#           for(int i=0;i<m;i++){
#             mat[i] = new int[n];
#             for(int j=0;j<m;j++)
#               mat[i][j] = 0;
#           }
#           return mat;
#         }
#         
#         // Freeing space for a double type matrix 
#         void DestroyMatrix(double ** mat, int m, int n){
#           for(int i=0;i<m;i++)
#             delete[] mat[i];
#           delete[] mat;
#         }
#         
#         // Freeing space for an integer type matrix 
#         void IDestroyMatrix(int ** mat, int m, int n){
#           for(int i=0;i<m;i++)
#             delete[] mat[i];
#           delete[] mat;
#         }
# 

# has now the desired functionality. A simple call like

#           A = CreateMatrix(n, n);
# 

# allocates now space for matrix $\hat{A}$ of dimensionality $n\ times n$. This increases the readibility of the program and makes easier to declare and delete matrices.  In order to allocated memory for a floating point variable matrix we have defined the function

#         //  Allocating space for a double type matrix
#         double ** CreateMatrix(int m, int n){
#           double ** mat;
#           mat = new double*[m];
#           for(int i=0;i<m;i++){
#             mat[i] = new double[n];
#             for(int j=0;j<m;j++)
#               mat[i][j] = 0.0;
#           }
#           return mat;
#         }
# 

# Note that here we initialize the matrix elements to zero. We always recommend to initialize variables in order to avoid random initialization values. Similarly, we free memory by

#         // Freeing space for a double type matrix 
#         void DestroyMatrix(double ** mat, int m, int n){
#           for(int i=0;i<m;i++)
#             delete[] mat[i];
#           delete[] mat;
#         }
# 

# Before we venture into the world of object orientation, we would like to introduce to you the popular  linear algebra library
# [Armadillo](http://arma.sourceforge.net/).
# 
#   * Armadillo is a C++ linear algebra library (matrix maths) aiming towards a good balance between speed and ease of use. The syntax is deliberately similar to Matlab.
# 
#   * Integer, floating point and complex numbers are supported, as well as a subset of trigonometric and statistics functions. Various matrix decompositions are provided through optional integration with LAPACK, or one of its high performance drop-in replacements (such as the multi-threaded MKL or ACML libraries).
# 
#   * A delayed evaluation approach is employed (at compile-time) to combine several operations into one and reduce (or eliminate) the need for temporaries. This is accomplished through recursive templates and template meta-programming.
# 
#   * Useful for conversion of research code into production environments, or if C++ has been decided as the language of choice, due to speed and/or integration capabilities.
# 
#   * The library is open-source software, and is distributed under a license that is useful in both open-source and commercial/proprietary contexts.
# 
# Here are simple examples.

#         #include <iostream>
#         #include <armadillo>
#         
#         using namespace std;
#         using namespace arma;
#         
#         int main(int argc, char** argv)
#           {
#           mat A = randu<mat>(5,5);
#           mat B = randu<mat>(5,5);
#         
#           cout << A*B << endl;
#         
#           return 0;
#         
# 

# For people using Ubuntu, Debian, Linux Mint, simply go to the synaptic package manager and install
# armadillo from there.
# You may have to install Lapack as well.
# For Mac and Windows users, follow the instructions from the webpage
# <http://arma.sourceforge.net>.  For MacOSX users we strongly recommend using [Brew](https://brew.sh/)  to install additional software.
# To compile, use for example (linux/ubuntu)

#         c++ -O2 -o program.x program.cpp  -larmadillo -llapack -lblas
# 

# where the `-l` option indicates the library you wish to link to.
# 
# For OS X users you may have to declare the paths to the include files and the libraries as

#         c++ -O2 -o program.x program.cpp  -L/usr/local/lib -I/usr/local/include -larmadillo -llapack -lblas
# 

#         #include <iostream>
#         #include "armadillo"
#         using namespace arma;
#         using namespace std;
#         
#         int main(int argc, char** argv)
#           {
#           // directly specify the matrix size (elements are uninitialised)
#           mat A(2,3);
#           // .n_rows = number of rows    (read only)
#           // .n_cols = number of columns (read only)
#           cout << "A.n_rows = " << A.n_rows << endl;
#           cout << "A.n_cols = " << A.n_cols << endl;
#           // directly access an element (indexing starts at 0)
#           A(1,2) = 456.0;
#           A.print("A:");
#           // scalars are treated as a 1x1 matrix,
#           // hence the code below will set A to have a size of 1x1
#           A = 5.0;
#           A.print("A:");
#           // if you want a matrix with all elements set to a particular value
#           // the .fill() member function can be used
#           A.set_size(3,3);
#           A.fill(5.0);  A.print("A:");
#           mat B;
#         
#           // endr indicates "end of row"
#           B << 0.555950 << 0.274690 << 0.540605 << 0.798938 << endr
#             << 0.108929 << 0.830123 << 0.891726 << 0.895283 << endr
#             << 0.948014 << 0.973234 << 0.216504 << 0.883152 << endr
#             << 0.023787 << 0.675382 << 0.231751 << 0.450332 << endr;
#         
#           // print to the cout stream
#           // with an optional string before the contents of the matrix
#           B.print("B:");
#         
#           // the << operator can also be used to print the matrix
#           // to an arbitrary stream (cout in this case)
#           cout << "B:" << endl << B << endl;
#           // save to disk
#           B.save("B.txt", raw_ascii);
#           // load from disk
#           mat C;
#           C.load("B.txt");
#           C += 2.0 * B;
#           C.print("C:");
#           // submatrix types:
#           //
#           // .submat(first_row, first_column, last_row, last_column)
#           // .row(row_number)
#           // .col(column_number)
#           // .cols(first_column, last_column)
#           // .rows(first_row, last_row)
#         
#           cout << "C.submat(0,0,3,1) =" << endl;
#           cout << C.submat(0,0,3,1) << endl;
#         
#           // generate the identity matrix
#           mat D = eye<mat>(4,4);
#         
#           D.submat(0,0,3,1) = C.cols(1,2);
#           D.print("D:");
#         
#           // transpose
#           cout << "trans(B) =" << endl;
#           cout << trans(B) << endl;
#         
#           // maximum from each column (traverse along rows)
#           cout << "max(B) =" << endl;
#           cout << max(B) << endl;
#         
#           // maximum from each row (traverse along columns)
#           cout << "max(B,1) =" << endl;
#           cout << max(B,1) << endl;
#           // maximum value in B
#           cout << "max(max(B)) = " << max(max(B)) << endl;
#           // sum of each column (traverse along rows)
#           cout << "sum(B) =" << endl;
#           cout << sum(B) << endl;
#           // sum of each row (traverse along columns)
#           cout << "sum(B,1) =" << endl;
#           cout << sum(B,1) << endl;
#           // sum of all elements
#           cout << "sum(sum(B)) = " << sum(sum(B)) << endl;
#           cout << "accu(B)     = " << accu(B) << endl;
#           // trace = sum along diagonal
#           cout << "trace(B)    = " << trace(B) << endl;
#           // random matrix -- values are uniformly distributed in the [0,1] interval
#           mat E = randu<mat>(4,4);
#           E.print("E:");
#         
#           // row vectors are treated like a matrix with one row
#           rowvec r;
#           r << 0.59499 << 0.88807 << 0.88532 << 0.19968;
#           r.print("r:");
#         
#           // column vectors are treated like a matrix with one column
#           colvec q;
#           q << 0.81114 << 0.06256 << 0.95989 << 0.73628;
#           q.print("q:");
#         
#           // dot or inner product
#           cout << "as_scalar(r*q) = " << as_scalar(r*q) << endl;
#         
#             // outer product
#           cout << "q*r =" << endl;
#           cout << q*r << endl;
#         
#         
#           // sum of three matrices (no temporary matrices are created)
#           mat F = B + C + D;
#           F.print("F:");
#         
#             return 0;
#         
# 

#         #include <iostream>
#         #include "armadillo"
#         using namespace arma;
#         using namespace std;
#         
#         int main(int argc, char** argv)
#           {
#           cout << "Armadillo version: " << arma_version::as_string() << endl;
#         
#           mat A;
#         
#           A << 0.165300 << 0.454037 << 0.995795 << 0.124098 << 0.047084 << endr
#             << 0.688782 << 0.036549 << 0.552848 << 0.937664 << 0.866401 << endr
#             << 0.348740 << 0.479388 << 0.506228 << 0.145673 << 0.491547 << endr
#             << 0.148678 << 0.682258 << 0.571154 << 0.874724 << 0.444632 << endr
#             << 0.245726 << 0.595218 << 0.409327 << 0.367827 << 0.385736 << endr;
#         
#           A.print("A =");
#         
#           // determinant
#           cout << "det(A) = " << det(A) << endl;
#           // inverse
#           cout << "inv(A) = " << endl << inv(A) << endl;
#           double k = 1.23;
#         
#           mat    B = randu<mat>(5,5);
#           mat    C = randu<mat>(5,5);
#         
#           rowvec r = randu<rowvec>(5);
#           colvec q = randu<colvec>(5);
#         
#         
#           // examples of some expressions
#           // for which optimised implementations exist
#           // optimised implementation of a trinary expression
#           // that results in a scalar
#           cout << "as_scalar( r*inv(diagmat(B))*q ) = ";
#           cout << as_scalar( r*inv(diagmat(B))*q ) << endl;
#         
#           // example of an expression which is optimised
#           // as a call to the dgemm() function in BLAS:
#           cout << "k*trans(B)*C = " << endl << k*trans(B)*C;
#         
#             return 0;
#         
# 

# ## [How to use the Library functions](https://github.com/CompPhysics/ComputationalPhysicsMSU/tree/master/doc/Programs/LecturePrograms/programs/cppLibrary)
# 
# Standard C/C++: fetch the files `lib.cpp` and `lib.h`. You can make a directory where you store
# these files, and eventually its compiled version lib.o. The example here is [program1.cpp from chapter 6](https://github.com/CompPhysics/ComputationalPhysicsMSU/blob/master/doc/Programs/LecturePrograms/programs/LinAlgebra/cpp/program1.cpp) and performs the matrix inversion.

#         //  Simple matrix inversion example
#         #include <iostream>
#         #include <new>
#         #include <cstdio>
#         #include <cstdlib>
#         #include <cmath>
#         #include <cstring>
#         #include "lib.h"
#         
#         using namespace std;
#         
#         /* function declarations */
#         
#         void inverse(double **, int);
#         
#         void inverse(double **a, int n)
#         {
#           int          i,j, *indx;
#           double       d, *col, **y;
#           // allocate space in memory
#           indx = new int[n];
#           col  = new double[n];
#           y    = (double **) matrix(n, n, sizeof(double));
#           ludcmp(a, n, indx, &d);   // LU decompose  a[][]
#           printf("\n\nLU form of matrix of a[][]:\n");
#           for(i = 0; i < n; i++) {
#             printf("\n");
#             for(j = 0; j < n; j++) {
#               printf(" a[%2d][%2d] = %12.4E",i, j, a[i][j]);
#           // find inverse of a[][] by columns
#           for(j = 0; j < n; j++) {
#             // initialize right-side of linear equations
#             for(i = 0; i < n; i++) col[i] = 0.0;
#             col[j] = 1.0;
#             lubksb(a, n, indx, col);
#             // save result in y[][]
#             for(i = 0; i < n; i++) y[i][j] = col[i];
#           }   //j-loop over columns
#           // return the inverse matrix in a[][]
#           for(i = 0; i < n; i++) {
#             for(j = 0; j < n; j++) a[i][j] = y[i][j];
#         
#           free_matrix((void **) y);     // release local memory
#           delete [] col;
#           delete []indx;
#         }  // End: function inverse()
# 

# ## [Using Armadillo to perform an LU decomposition](https://github.com/CompPhysics/ComputationalPhysicsMSU/blob/master/doc/Programs/CppQtCodesLectures/MatrixTest/main.cpp)

#         #include <iostream>
#         #include "armadillo"
#         using namespace arma;
#         using namespace std;
#         
#         int main()
#           {
#            mat A = randu<mat>(5,5);
#            vec b = randu<vec>(5);
#         
#           A.print("A =");
#           b.print("b=");
#           // solve Ax = b
#           vec x = solve(A,b);
#           // print x
#           x.print("x=");
#           // find LU decomp of A, if needed, P is the permutation matrix
#           mat L, U;
#           lu(L,U,A);
#           // print l
#           L.print(" L= ");
#           // print U
#           U.print(" U= ");
#           //Check that A = LU
#           (A-P*L*U).print("Test of LU decomposition");
#             return 0;
#           }
# 

# ## Optimization and profiling
# 
# Till now we have not paid much attention to speed and possible optimization possibilities
# inherent in the various compilers. We have compiled and linked as

#         c++  -c  mycode.cpp
#         c++  -o  mycode.exe  mycode.o
# 

# For Fortran replace with for example **gfortran** or **ifort**.
# This is what we call a flat compiler option and should be used when we develop the code.
# It produces normally a very large and slow code when translated to machine instructions.
# We use this option for debugging and for establishing the correct program output because
# every operation is done precisely as the user specified it.
# 
# It is instructive to look up the compiler manual for further instructions by writing

#         man c++
# 

# We have additional compiler options for optimization. These may include procedure inlining where 
# performance may be improved, moving constants inside loops outside the loop, 
# identify potential parallelism, include automatic vectorization or replace a division with a reciprocal
# and a multiplication if this speeds up the code.

#         c++  -O3 -c  mycode.cpp
#         c++  -O3 -o  mycode.exe  mycode.o
# 

# This (other options are -O2 or -Ofast) is the recommended option. 
# 
# 
# It is also useful to profile your program under the development stage.
# You would then compile with

#         c++  -pg -O3 -c  mycode.cpp
#         c++  -pg -O3 -o  mycode.exe  mycode.o
# 

# After you have run the code you can obtain the profiling information via

#         gprof mycode.exe >  ProfileOutput
# 

# When you have profiled properly your code, you must take out this option as it 
# slows down performance.
# For memory tests use [valgrind](http://www.valgrind.org). An excellent environment for all these aspects, and much  more, is  Qt creator.
# 
# 
# Adding debugging options is a very useful alternative under the development stage of a program.
# You would then compile with

#         c++  -g -O0 -c  mycode.cpp
#         c++  -g -O0 -o  mycode.exe  mycode.o
# 

# This option generates debugging information allowing you to trace for example if an array is properly allocated. Some compilers work best with the no optimization option **-O0**. 
# 
# 
# Depending on the compiler, one can add flags which generate code that catches integer overflow errors. 
# The flag **-ftrapv** does this for the CLANG compiler on OS X operating systems.   
# 
# In general, irrespective of compiler options, it is useful to
# * avoid if tests or call to functions inside loops, if possible. 
# 
# * avoid multiplication with constants inside loops if possible
# 
# Here is an example of a part of a program where specific operations lead to a slower code

#         k = n-1;
#         for (i = 0; i < n; i++){
#             a[i] = b[i] +c*d;
#             e = g[k];
#         }
# 

# A better code is

#         temp = c*d;
#         for (i = 0; i < n; i++){
#             a[i] = b[i] + temp;
#         }
#         e = g[n-1];
# 

# Here we avoid a repeated multiplication inside a loop. 
# Most compilers, depending on compiler flags, identify and optimize such bottlenecks on their own, without requiring any particular action by the programmer. However, it is always useful to single out and avoid code examples like the first one discussed here.
# 
# 
# ## Vectorization and the basic idea behind parallel computing
# 
# Present CPUs are highly parallel processors with varying levels of parallelism. The typical situation can be described via the following three statements.
# * Pursuit of shorter computation time and larger simulation size gives rise to parallel computing.
# 
# * Multiple processors are involved to solve a global problem.
# 
# * The essence is to divide the entire computation evenly among collaborative processors.  Divide and conquer.
# 
# Before we proceed with a more detailed discussion of topics like vectorization and parallelization, we need to remind ourselves about some basic features of different hardware models. We have
# 
# 
# * Conventional single-processor computers are named SISD (single-instruction-single-data) machines.
# 
# * SIMD (single-instruction-multiple-data) machines incorporate the idea of parallel processing, using a large number of processing units to execute the same instruction on different data.
# 
# * Modern parallel computers are so-called MIMD (multiple-instruction-multiple-data) machines and can execute different instruction streams in parallel on different data.
# 
# ## What is vectorization?
# 
# Vectorization is a special
# case of **Single Instructions Multiple Data** (SIMD) to denote a single
# instruction stream capable of operating on multiple data elements in
# parallel. 
# We can think of vectorization as the unrolling of loops accompanied with SIMD instructions.
# 
# Vectorization is the process of converting an algorithm that performs scalar operations
# (typically one operation at the time) to vector operations where a single operation can refer to many simultaneous operations.
# Consider the following example

#         for (i = 0; i < n; i++){
#             a[i] = b[i] + c[i];
#         }
# 

# If the code is not vectorized, the compiler will simply start with the first element and 
# then perform subsequent additions operating on one address in memory at the time. 
# 
# 
# A SIMD instruction can operate  on multiple data elements in one single instruction.
# It uses the so-called 128-bit SIMD floating-point register. 
# In this sense,vectorization adds some form of parallelism since one instruction is applied  
# to many parts of say a vector.
# 
# The number of elements which can be operated on in parallel
# range from four single-precision floating point data elements in so-called 
# Streaming SIMD Extensions and two double-precision floating-point data
# elements in Streaming SIMD Extensions 2 to sixteen byte operations in
# a 128-bit register in Streaming SIMD Extensions 2. Thus, vector-length
# ranges from 2 to 16, depending on the instruction extensions used and
# on the data type. 
# 
# 
# We start with the simple scalar operations given by

#         for (i = 0; i < n; i++){
#             a[i] = b[i] + c[i];
#         }
# 

# If the code is not vectorized  and we have a 128-bit register to store a 32 bits floating point number,
# it means that we have $3\times 32$ bits that are not used. For the first element we have
# 
# 
# <table border="1">
# <thead>
# <tr><th align="center">  0  </th> <th align="center">   1    </th> <th align="center">   2    </th> <th align="center">   3    </th> </tr>
# </thead>
# <tbody>
# <tr><td align="center">   a[0]=    </td> <td align="center">   not used    </td> <td align="center">   not used    </td> <td align="center">   not used    </td> </tr>
# <tr><td align="center">   b[0]+    </td> <td align="center">   not used    </td> <td align="center">   not used    </td> <td align="center">   not used    </td> </tr>
# <tr><td align="center">   c[0]     </td> <td align="center">   not used    </td> <td align="center">   not used    </td> <td align="center">   not used    </td> </tr>
# </tbody>
# </table>
# We have thus unused space in our SIMD registers. These registers could hold three additional integers.
# 
# 
# 
# If we vectorize the code, we can perform, with a 128-bit register four simultaneous operations, that is
# we have

#         for (i = 0; i < n; i+=4){
#             a[i] = b[i] + c[i];
#             a[i+1] = b[i+1] + c[i+1];
#             a[i+2] = b[i+2] + c[i+2];
#             a[i+3] = b[i+3] + c[i+3];
#         }
# 

# displayed here as
# 
# <table border="1">
# <thead>
# <tr><th align="center">  0  </th> <th align="center">  1  </th> <th align="center">  2  </th> <th align="center">  3  </th> </tr>
# </thead>
# <tbody>
# <tr><td align="center">   a[0]=    </td> <td align="center">   a[1]=    </td> <td align="center">   a[2]=    </td> <td align="center">   a[3]=    </td> </tr>
# <tr><td align="center">   b[0]+    </td> <td align="center">   b[1]+    </td> <td align="center">   b[2]+    </td> <td align="center">   b[3]+    </td> </tr>
# <tr><td align="center">   c[0]     </td> <td align="center">   c[1]     </td> <td align="center">   c[2]     </td> <td align="center">   c[3]     </td> </tr>
# </tbody>
# </table>
# Four additions are now done in a single step.
# 
# 
# ## [A simple test case with and without vectorization](https://github.com/CompPhysics/ComputationalPhysicsMSU/blob/master/doc/Programs/LecturePrograms/programs/Classes/cpp/program7.cpp)
# We implement these operations in a simple c++ program as

#         #include <cstdlib>
#         #include <iostream>
#         #include <cmath>
#         #include <iomanip>
#         #include "time.h" 
#         
#         using namespace std; // note use of namespace                                       
#         int main (int argc, char* argv[])
#         {
#           int i = atoi(argv[1]); 
#           double *a, *b, *c;
#           a = new double[i]; 
#           b = new double[i]; 
#           c = new double[i]; 
#           for (int j = 0; j < i; j++) {
#             a[j] = 0.0;
#             b[j] = cos(j*1.0);
#             c[j] = sin(j*3.0);
#           }
#           clock_t start, finish;
#           start = clock();
#           for (int j = 0; j < i; j++) {
#             a[j] = b[j]+b[j]*c[j];
#           }
#           finish = clock();
#           double timeused = (double) (finish - start)/(CLOCKS_PER_SEC );
#           cout << setiosflags(ios::showpoint | ios::uppercase);
#           cout << setprecision(10) << setw(20) << "Time used  for vector addition and multiplication=" << timeused  << endl;
#           delete [] a;
#           delete [] b;
#           delete [] c;
#           return 0;     
#         }
# 

# We can compile and link without vectorization

#         c++ -o novec.x vecexample.cpp
# 

# vand with vectorization (and additional optimizations)

#         c++ -O3 -o  vec.x vecexample.cpp 
# 

# The speedup depends on the size of the vectors. In the example here we have run with $10^7$ elements.
# The example here was run on a PC with ubuntu 14.04 as operating system and an Intel i7-4790 CPU running at 3.60 GHz.

#         Compphys:~ hjensen$ ./vec.x 10000000
#         Time used  for vector addition = 0.0100000
#         Compphys:~ hjensen$ ./novec.x 10000000
#         Time used  for vector addition = 0.03000000000
# 

# This particular C++ compiler speeds up the above loop operations with a factor of 3. 
# Performing the same operations for $10^8$ elements results only in a factor $1.4$.
# The result will however vary from compiler to compiler. In general however, with optimization flags like $-O3$ or $-Ofast$, we gain a considerable speedup if our code can be vectorized. Many of these operations can be done automatically by your compiler. These automatic or near automatic compiler techniques improve performance considerably. 
# 
# 
# Not all loops can be vectorized, as discussed in [Intel's guide to vectorization](https://software.intel.com/en-us/articles/a-guide-to-auto-vectorization-with-intel-c-compilers)
# 
# An important criteria is that the loop counter $n$ is known at the entry of the loop.

#           for (int j = 0; j < n; j++) {
#             a[j] = cos(j*1.0);
#           }
# 

# The variable $n$ does need to be known at compile time. However, this variable must stay the same for the entire duration of the loop. It implies that an exit statement inside the loop cannot be data dependent.
# 
# 
# An exit statement should in general be avoided. 
# If the exit statement contains data-dependent conditions, the loop cannot be vectorized. 
# The following is an example of a non-vectorizable loop

#           for (int j = 0; j < n; j++) {
#             a[j] = cos(j*1.0);
#             if (a[j] < 0 ) break;
#           }
# 

# Avoid loop termination conditions and opt for a single entry loop variable $n$. The lower and upper bounds have to be kept fixed within the loop. 
# 
# SIMD instructions perform the same type of operations multiple times. 
# A **switch** statement leads thus to a non-vectorizable loop since different statemens cannot branch.
# The following code can however be vectorized since the **if** statement is implemented as a masked assignment.

#           for (int j = 0; j < n; j++) {
#             double x  = cos(j*1.0);
#             if (x > 0 ) {
#                a[j] =  x*sin(j*2.0); 
#             }
#             else {
#                a[j] = 0.0;
#             }
#           }
# 

# These operations can be performed for all data elements but only those elements which the mask evaluates as true are stored. In general, one should avoid branches such as **switch**, **go to**, or **return** statements or **if** constructs that cannot be treated as masked assignments. 
# 
# 
# 
# 
# Only the innermost loop of the following example is vectorized

#           for (int i = 0; i < n; i++) {
#               for (int j = 0; j < n; j++) {
#                    a[i][j] += b[i][j];
#               }  
#           }
# 

# The exception is if an original outer loop is transformed into an inner loop as the result of compiler optimizations.
# 
# 
# 
# Calls to programmer defined functions ruin vectorization. However, calls to intrinsic functions like
# $\sin{x}$, $\cos{x}$, $\exp{x}$ etc are allowed since they are normally efficiently vectorized. 
# The following example is fully vectorizable

#           for (int i = 0; i < n; i++) {
#               a[i] = log10(i)*cos(i);
#           }
# 

# Similarly, **inline** functions defined by the programmer, allow for vectorization since the function statements are glued into the actual place where the function is called. 
# 
# 
# 
# One has to keep in mind that vectorization changes the order of operations inside a loop. A so-called
# read-after-write statement with an explicit flow dependency cannot be vectorized. The following code

#           double b = 15.;
#           for (int i = 1; i < n; i++) {
#               a[i] = a[i-1] + b;
#           }
# 

# is an example of flow dependency and results in wrong numerical results if vectorized. For a scalar operation, the value $a[i-1]$ computed during the iteration is loaded into the right-hand side and the results are fine. In vector mode however, with a vector length of four, the values $a[0]$, $a[1]$, $a[2]$ and $a[3]$ from the previous loop will be loaded into the right-hand side and produce wrong results. That is, we have

#            a[1] = a[0] + b;
#            a[2] = a[1] + b;
#            a[3] = a[2] + b;
#            a[4] = a[3] + b;
# 

# and if the two first iterations are  executed at the same by the SIMD instruction, the value of say $a[1]$ could be used by the second iteration before it has been calculated by the first iteration, leading thereby to wrong results.
# 
# 
# On the other hand,  a so-called 
# write-after-read statement can be vectorized. The following code

#           double b = 15.;
#           for (int i = 1; i < n; i++) {
#               a[i-1] = a[i] + b;
#           }
# 

# is an example of flow dependency that can be vectorized since no iteration with a higher value of $i$
# can complete before an iteration with a lower value of $i$. However, such code leads to problems with parallelization.
# 
# 
# 
# For C++ programmers  it is also worth keeping in mind that an array notation is preferred to the more compact use of pointers to access array elements. The compiler can often not tell if it is safe to vectorize the code. 
# 
# When dealing with arrays, you should also avoid memory stride, since this slows down considerably vectorization. When you access array element, write for example the inner loop to vectorize using unit stride, that is, access successively the next array element in memory, as shown here

#           for (int i = 0; i < n; i++) {
#               for (int j = 0; j < n; j++) {
#                    a[i][j] += b[i][j];
#               }  
#           }
# 

# We can compile and link without vectorization using the clang c++ (on OSX for example) compiler

#         clang -o novec.x vecexample.cpp
# 

# and with vectorization (and additional optimizations)

#         clang++ -O3 -Rpass=loop-vectorize -o  vec.x vecexample.cpp 
# 

# The speedup depends on the size of the vectors. In the example here we have run with $10^7$ elements.
# The example here was run on an IMac17.1 with OSX El Capitan (10.11.4) as operating system and an Intel i5 3.3 GHz CPU.

#         Compphys:~ hjensen$ ./vec.x 10000000
#         Time used  for norm computation=0.04720500000
#         Compphys:~ hjensen$ ./novec.x 10000000
#         Time used  for norm computation=0.03311700000
# 

# This particular C++ compiler speeds up the above loop operations with a factor of 1.5 
# Performing the same operations for $10^9$ elements results in a smaller speedup since reading from main memory is required. The non-vectorized code is seemingly faster.

#         Compphys:~ hjensen$ ./vec.x 1000000000
#         Time used  for norm computation=58.41391100
#         Compphys:~ hjensen$ ./novec.x 1000000000
#         Time used  for norm computation=46.51295300
# 

# We will discuss these issues below.
# 
# We can compile and link without vectorization with clang compiler

#         clang++ -o -fno-vectorize novec.x vecexample.cpp
# 

# and with vectorization

#         clang++ -O3 -Rpass=loop-vectorize -o  vec.x vecexample.cpp 
# 

# We can also add vectorization analysis, see for example

#         clang++ -O3 -Rpass-analysis=loop-vectorize -o  vec.x vecexample.cpp 
# 

# or figure out if vectorization was missed

#         clang++ -O3 -Rpass-missed=loop-vectorize -o  vec.x vecexample.cpp 
# 

# ## Measuring performance
# 
# How do we measure erformance? What is wrong with this code to time a loop?

#           clock_t start, finish;
#           start = clock();
#           for (int j = 0; j < i; j++) {
#             a[j] = b[j]+b[j]*c[j];
#           }
#           finish = clock();
#           double timeused = (double) (finish - start)/(CLOCKS_PER_SEC );
# 

# ## Problems with measuring time
# 1. Timers are not infinitely accurate
# 
# 2. All clocks have a granularity, the minimum time that they can measure
# 
# 3. The error in a time measurement, even if everything is perfect, may be the size of this granularity (sometimes called a clock tick)
# 
# 4. Always know what your clock granularity is
# 
# 5. Ensure that your measurement is for a long enough duration (say 100 times the **tick**)
# 
# ## Problems with cold start
# 
# What happens when the code is executed? The assumption is that the code is ready to
# execute. But
# 1. Code may still be on disk, and not even read into memory.
# 
# 2. Data may be in slow memory rather than fast (which may be wrong or right for what you are measuring)
# 
# 3. Multiple tests often necessary to ensure that cold start effects are not present
# 
# 4. Special effort often required to ensure data in the intended part of the memory hierarchy.
# 
# ## Problems with smart compilers
# 
# 1. If the result of the computation is not used, the compiler may eliminate the code
# 
# 2. Performance will look impossibly fantastic
# 
# 3. Even worse, eliminate some of the code so the performance looks plausible
# 
# 4. Ensure that the results are (or may be) used.
# 
# ## Problems with interference
# 1. Other activities are sharing your processor
# 
#   * Operating system, system demons, other users
# 
#    * Some parts of the hardware do not always perform with exactly the same performance
# 
# 
# 
# 2. Make multiple tests and report
# 
# 3. Easy choices include
# 
#   * Average tests represent what users might observe over time
# 
# 
# ## Problems with measuring performance
# 1. Accurate, reproducible performance measurement is hard
# 
# 2. Think carefully about your experiment:
# 
# 3. What is it, precisely, that you want to measure
# 
# 4. How representative is your test to the situation that you are trying to measure?
# 
# ## Thomas algorithm for tridiagonal linear algebra equations

# $$
# \left( \begin{array}{ccccc}
#         b_0 & c_0 &        &         &         \\
# 	a_0 &  b_1 &  c_1    &         &         \\
# 	   &    & \ddots  &         &         \\
# 	      &	    & a_{m-3} & b_{m-2} & c_{m-2} \\
# 	         &    &         & a_{m-2} & b_{m-1}
#    \end{array} \right)
# \left( \begin{array}{c}
#        x_0     \\
#        x_1     \\
#        \vdots  \\
#        x_{m-2} \\
#        x_{m-1}
#    \end{array} \right)=\left( \begin{array}{c}
#        f_0     \\
#        f_1     \\
#        \vdots  \\
#        f_{m-2} \\
#        f_{m-1} \\
#    \end{array} \right)
# $$

# The first step is to multiply the first row by $a_0/b_0$ and subtract it from the second row.  This is known as the forward substitution step. We obtain then

# $$
# a_i = 0,
# $$

# $$
# b_i = b_i - \frac{a_{i-1}}{b_{i-1}}c_{i-1},
# $$

# and

# $$
# f_i = f_i - \frac{a_{i-1}}{b_{i-1}}f_{i-1}.
# $$

# At this point the simplified equation, with only an upper triangular matrix takes the form

# $$
# \left( \begin{array}{ccccc}
#     b_0 & c_0 &        &         &         \\
#        & b_1 &  c_1    &         &         \\
#           &    & \ddots &         &         \\
# 	     &     &        & b_{m-2} & c_{m-2} \\
# 	        &    &        &         & b_{m-1}
#    \end{array} \right)\left( \begin{array}{c}
#        x_0     \\
#        x_1     \\
#        \vdots  \\
#        x_{m-2} \\
#        x_{m-1}
#    \end{array} \right)=\left( \begin{array}{c}
#        f_0     \\
#        f_1     \\
#        \vdots  \\
#        f_{m-2} \\
#        f_{m-1} \\
#    \end{array} \right)
# $$

# The next step is  the backward substitution step.  The last row is multiplied by $c_{N-3}/b_{N-2}$ and subtracted from the second to last row, thus eliminating $c_{N-3}$ from the last row.  The general backward substitution procedure is

# $$
# c_i = 0,
# $$

# and

# $$
# f_{i-1} = f_{i-1} - \frac{c_{i-1}}{b_i}f_i
# $$

# All that remains to be computed is the solution, which is the very straight forward process of

# $$
# x_i = \frac{f_i}{b_i}
# $$

# <table border="1">
# <thead>
# <tr><th align="center">   Operation   </th> <th align="center">Floating Point</th> </tr>
# </thead>
# <tbody>
# <tr><td align="center">   Memory Reads       </td> <td align="center">   $14(N-2)$         </td> </tr>
# <tr><td align="center">   Memory Writes      </td> <td align="center">   $4(N-2)$          </td> </tr>
# <tr><td align="center">   Subtractions       </td> <td align="center">   $3(N-2)$          </td> </tr>
# <tr><td align="center">   Multiplications    </td> <td align="center">   $3(N-2)$          </td> </tr>
# <tr><td align="center">   Divisions          </td> <td align="center">   $4(N-2)$          </td> </tr>
# </tbody>
# </table>

#         // Forward substitution    
#         // Note that we can simplify by precalculating a[i-1]/b[i-1]
#           for (int i=1; i < n; i++) {
#              b[i] = b[i] - (a[i-1]*c[i-1])/b[i-1];
#              f[i] = g[i] - (a[i-1]*f[i-1])/b[i-1];
#           }
#           x[n-1] = f[n-1] / b[n-1];
#           // Backwards substitution                                                           
#           for (int i = n-2; i >= 0; i--) {
#              f[i] = f[i] - c[i]*f[i+1]/b[i+1];
#              x[i] = f[i]/b[i];
#           }
# 

# ## [The specialized Thomas algorithm (Project 1)](https://github.com/CompPhysics/ComputationalPhysics/blob/master/doc/Projects/2016/Project1/Examples/TridiagonalTiming.cpp)
# 
# 
# <table border="1">
# <thead>
# <tr><th align="center">  Operation  </th> <th align="center">Floating Point</th> </tr>
# </thead>
# <tbody>
# <tr><td align="center">   Memory Reads     </td> <td align="center">   $6(N-2)$          </td> </tr>
# <tr><td align="center">   Memory Writes    </td> <td align="center">   $2(N-2)$          </td> </tr>
# <tr><td align="center">   Additions        </td> <td align="center">   $2(N-2)$          </td> </tr>
# <tr><td align="center">   Divisions        </td> <td align="center">   $2(N-2)$          </td> </tr>
# </tbody>
# </table>

#               // Forward substitution cannot be vectorized
#               for (int i = 2; i < n; i++) b[i] = b[i] + b[i-1]/d[i-1];
#               // Backward substitution  cannot be vectorized
#               solution[n-1] = b[n-1]/d[n-1];
#               for (int i = n-2; i > 0; i--) solution[i] = (b[i]+solution[i+1])/d[i];
# 

# ## [Example: Transpose of a matrix](https://github.com/CompPhysics/ComputationalPhysicsMSU/blob/master/doc/Programs/LecturePrograms/programs/Classes/cpp/program8.cpp)

#         #include <cstdlib>
#         #include <iostream>
#         #include <cmath>
#         #include <iomanip>
#         #include "time.h"
#         
#         using namespace std; // note use of namespace
#         int main (int argc, char* argv[])
#         {
#           // read in dimension of square matrix
#           int n = atoi(argv[1]);
#           double **A, **B;
#           // Allocate space for the two matrices
#           A = new double*[n]; B = new double*[n];
#           for (int i = 0; i < n; i++){
#             A[i] = new double[n];
#             B[i] = new double[n];
#           }
#           // Set up values for matrix A
#           for (int i = 0; i < n; i++){
#             for (int j = 0; j < n; j++) {
#               A[i][j] =  cos(i*1.0)*sin(j*3.0);
#             }
#           }
#           clock_t start, finish;
#           start = clock();
#           // Then compute the transpose
#           for (int i = 0; i < n; i++){
#             for (int j = 0; j < n; j++) {
#               B[i][j]= A[j][i];
#             }
#           }
#         
#           finish = clock();
#           double timeused = (double) (finish - start)/(CLOCKS_PER_SEC );
#           cout << setiosflags(ios::showpoint | ios::uppercase);
#           cout << setprecision(10) << setw(20) << "Time used  for setting up transpose of matrix=" << timeused  << endl;
#         
#           // Free up space
#           for (int i = 0; i < n; i++){
#             delete[] A[i];
#             delete[] B[i];
#           }
#           delete[] A;
#           delete[] B;
#           return 0;
#         }
#         
# 

# ## [Matrix-matrix multiplication](https://github.com/CompPhysics/ComputationalPhysicsMSU/blob/master/doc/Programs/LecturePrograms/programs/Classes/cpp/program9.cpp)
# This the matrix-matrix multiplication code with plain c++ memory allocation. It computes at the end the Frobenius norm.

#         #include <cstdlib>
#         #include <iostream>
#         #include <cmath>
#         #include <iomanip>
#         #include "time.h"
#         
#         using namespace std; // note use of namespace
#         int main (int argc, char* argv[])
#         {
#           // read in dimension of square matrix
#           int n = atoi(argv[1]);
#           double s = 1.0/sqrt( (double) n);
#           double **A, **B, **C;
#           // Start timing
#           clock_t start, finish;
#           start = clock();
#           // Allocate space for the two matrices
#           A = new double*[n]; B = new double*[n]; C = new double*[n];
#           for (int i = 0; i < n; i++){
#             A[i] = new double[n];
#             B[i] = new double[n];
#             C[i] = new double[n];
#           }
#           // Set up values for matrix A and B and zero matrix C
#           for (int i = 0; i < n; i++){
#             for (int j = 0; j < n; j++) {
#               double angle = 2.0*M_PI*i*j/ (( double ) n);
#               A[i][j] = s * ( sin ( angle ) + cos ( angle ) );
#               B[j][i] =  A[i][j];
#             }
#           }
#           // Then perform the matrix-matrix multiplication
#           for (int i = 0; i < n; i++){
#             for (int j = 0; j < n; j++) {
#               double sum = 0.0;
#                for (int k = 0; k < n; k++) {
#                    sum += B[i][k]*A[k][j];
#                }
#                C[i][j] = sum;
#             }
#           }
#           // Compute now the Frobenius norm
#           double Fsum = 0.0;
#           for (int i = 0; i < n; i++){
#             for (int j = 0; j < n; j++) {
#               Fsum += C[i][j]*C[i][j];
#             }
#           }
#           Fsum = sqrt(Fsum);
#           finish = clock();
#           double timeused = (double) (finish - start)/(CLOCKS_PER_SEC );
#           cout << setiosflags(ios::showpoint | ios::uppercase);
#           cout << setprecision(10) << setw(20) << "Time used  for matrix-matrix multiplication=" << timeused  << endl;
#           cout << "  Frobenius norm  = " << Fsum << endl;
#           // Free up space
#           for (int i = 0; i < n; i++){
#             delete[] A[i];
#             delete[] B[i];
#             delete[] C[i];
#           }
#           delete[] A;
#           delete[] B;
#           delete[] C;
#           return 0;
#         }
# 

# ## How do we define speedup? Simplest form
# 
# * Speedup(code,sys,p) = $T_b/T_p$
# 
# * Speedup measures the ratio of performance between two objects
# 
# * Versions of same code, with different number of processors
# 
# * Serial and vector versions
# 
# * Try different programing languages, C++ and Fortran
# 
# * Two algorithms computing the **same** result 
# 
# The key is choosing the correct baseline for comparison
# * For our serial vs. vectorization examples, using compiler-provided vectorization, the baseline is simple; the same code, with vectorization turned off
# 
#  * For parallel applications, this is much harder:
# 
#   * Choice of algorithm, decomposition, performance of baseline case etc.
# 
# 
# 
# ## Object orientation
# 
# Why object orientation?
# 
#   * Three main topics: objects, class hierarchies and polymorphism
# 
#   * The aim here is to be to be able to write a more general code which can easily be tailored to new situations.
# 
#   * **Polymorphism** is a term used in software development to describe a variety of techniques employed by programmers to create flexible and reusable software components. The term is Greek and it loosely translates to "many forms". Strategy: try to single out the variables needed to describe a given system and those needed to describe a given solver. 
# 
# In programming languages, a polymorphic object is an entity, such as a variable or a procedure, that can hold or operate on values of differing types during the program's execution. Because a polymorphic object can operate on a variety of values and types, it can also be used in a variety of programs, sometimes with little or no change by the programmer. The idea of write once, run many, also known as code reusability, is an important characteristic to the programming paradigm known as Object-Oriented Programming (OOP).
# 
# OOP describes an approach to programming where a program is viewed as a collection of interacting, but mostly independent software components. These software components are known as objects in OOP and they are typically implemented in a programming language as an entity that encapsulates both data and procedures.
# 
# 
# 
# In Fortran a vector or matrix start with $1$, but it is easy
# to change a vector so that it starts with zero or even a negative number.
# If we have a double precision Fortran vector  which starts at $-10$ and ends at $10$, we could declare it as
# `REAL(KIND=8) ::  vector(-10:10)`. Similarly, if we want to start at zero and end at 10 we could write
# `REAL(KIND=8) ::  vector(0:10)`.
# We have also seen that Fortran  allows us to write a matrix addition $\mathbf{A} = \mathbf{B}+\mathbf{C}$ as
# `A = B + C`.  This means that we have overloaded the addition operator so that it translates this operation into
# two loops and an addition of two matrix elements $a_{ij} = b_{ij}+c_{ij}$.
# 
# 
# 
# The way the matrix addition is written is very close to the way we express this relation mathematically. The benefit for the
# programmer is that our code is easier to read. Furthermore, such a way of coding makes it  more likely  to spot eventual
# errors as well.
# 
# In Ansi C and C++ arrays start by default from $i=0$.  Moreover, if we  wish to add two matrices we need to explicitely write out
# the two loops as

#            for(i=0 ; i < n ; i++) {
#               for(j=0 ; j < n ; j++) {
#                  a[i][j]=b[i][j]+c[i][j]
#         
# 

# However,
# the strength of C++ is the possibility
# to define new data types, tailored to some particular problem.
# Via new data types and overloading of operations such as addition and subtraction, we can easily define
# sets of operations and data types which allow us to write a matrix addition in exactly the same
# way as we would do in Fortran.  We could also change the way we declare a C++ matrix elements $a_{ij}$, from  $a[i][j]$
# to say $a(i,j)$, as we would do in Fortran. Similarly, we could also change the default range from $0:n-1$ to $1:n$.
# 
# To achieve this we need to introduce two important entities in C++ programming, classes and templates.
# 
# 
# 
# The function and class declarations are fundamental concepts within C++.  Functions are abstractions
# which encapsulate an algorithm or parts of it and perform specific tasks in a program.
# We have already met several examples on how to use  functions.
# Classes can be defined as abstractions which encapsulate
# data and operations on these data.
# The data can be very complex data structures  and the class can contain particular functions
# which operate on these data. Classes allow therefore for a higher level of abstraction in computing.
# The elements (or components) of the data
# type are the class data members, and the procedures are the class
# member functions.
# 
# 
# 
# Classes are user-defined tools used to create multi-purpose software which can be reused by other classes or functions.
# These user-defined data types contain data (variables) and
# functions operating on the data.
# 
# A simple example is that of a point in two dimensions.
# The data could be the $x$ and $y$ coordinates of a given  point. The functions
# we define could be simple read and write functions or the possibility to compute the distance between two points.
# 
# 
# 
# C++ has a class complex in its standard
# template library (STL). The standard usage in a given function could then look like

#         // Program to calculate addition and multiplication of two complex numbers
#         using namespace std;
#         #include <iostream>
#         #include <cmath>
#         #include <complex>
#         int main()
#         {
#           complex<double> x(6.1,8.2), y(0.5,1.3);
#           // write out x+y
#           cout << x + y << x*y  << endl;
#           return 0;
#         
# 

# where we add and multiply two complex numbers $x=6.1+\imath 8.2$ and $y=0.5+\imath 1.3$ with the obvious results
# $z=x+y=6.6+\imath 9.5$ and $z=x\cdot y= -7.61+\imath 12.03$.
# 
# 
# 
# We proceed by  splitting our task in three files.
# 
# We define first a header file complex.h  which contains the declarations of
# the class. The header file contains the class declaration (data and
# functions), declaration of stand-alone functions, and all inlined
# functions, starting as follows

#         #ifndef Complex_H
#         #define Complex_H
#         //   various include statements and definitions
#         #include <iostream>          // Standard ANSI-C++ include files
#         #include <new>
#         #include ....
#         
#         class Complex
#         {...
#         definition of variables and their character
#         };
#         //   declarations of various functions used by the class
#         ...
#         #endif
# 

# Next we provide a file complex.cpp where the code and algorithms of
# different functions (except inlined functions) declared within the
# class are written.  The files `complex.h` and `complex.cpp` are normally
# placed in a directory with other classes and libraries we have
# defined.
# 
# Finally, we discuss here an example of a main program which uses this
# particular class.  An example of a program which uses our complex
# class is given below. In particular we would like our class to perform
# tasks like declaring complex variables, writing out the real and
# imaginary part and performing algebraic operations such as adding or
# multiplying two complex numbers.

#         #include "Complex.h"
#         ...  other include and declarations
#         int main ()
#         {
#           Complex a(0.1,1.3);    // we declare a complex variable a
#           Complex b(3.0), c(5.0,-2.3);  // we declare  complex variables b and c
#           Complex d = b;         //  we declare  a new complex variable d
#           cout << "d=" << d << ", a=" << a << ", b=" << b << endl;
#           d = a*c + b/a;  //   we add, multiply and divide two complex numbers
#           cout << "Re(d)=" << d.Re() << ", Im(d)=" << d.Im() << endl;  // write out of the real and imaginary parts
#         
# 

# We include the header file complex.h and define four different complex variables. These
# are $a=0.1+\imath 1.3$, $b=3.0+\imath 0$ (note that if you don't define a value for the imaginary part  this is set to
# zero), $c=5.0-\imath 2.3$ and $d=b$.  Thereafter we have defined standard algebraic operations and the member functions
# of the class which allows us to print out the real and imaginary part of a given variable.

#         class Complex
#         {
#         private:
#            double re, im; // real and imaginary part
#         public:
#            Complex ();                              // Complex c;
#            Complex (double re, double im = 0.0); // Definition of a complex variable;
#            Complex (const Complex& c);              // Usage: Complex c(a);   // equate two complex variables
#            Complex& operator= (const Complex& c); // c = a;   //  equate two complex variables, same as previous
#         ....
#         
# 

#           ~Complex () {}                        // destructor
#            double   Re () const;        // double real_part = a.Re();
#            double   Im () const;        // double imag_part = a.Im();
#            double   abs () const;       // double m = a.abs(); // modulus
#            friend Complex operator+ (const Complex&  a, const Complex& b);
#            friend Complex operator- (const Complex&  a, const Complex& b);
#            friend Complex operator* (const Complex&  a, const Complex& b);
#            friend Complex operator/ (const Complex&  a, const Complex& b);
#         };
# 

# The class is defined via the statement `class Complex`. We must first use the key word
# `class`, which in turn is followed by the user-defined variable name  `Complex`.
# The body of the class, data and functions, is encapsulated  within the parentheses `{...}`.
# 
# 
# Data and specific functions can be private, which means that they cannot be accessed from outside the class.
# This means also that access cannot be inherited by other functions outside the class. If we use `protected`
# instead of `private`, then data and functions can be inherited outside the class.
# 
# 
# The key word `public` means  that data and functions can be accessed from outside the class.
# Here we have defined several functions  which can be accessed by functions outside the class.
# The declaration `friend` means that stand-alone functions can work on privately declared  variables  of the type
# `(re, im)`.  Data members of a class should be declared as private variables.
# 
# 
# 
# The first public function we encounter is a so-called
# constructor, which  tells how we declare a variable of type `Complex`
# and how this variable is initialized. We have chose  three possibilities in the example above:
# 
# A declaration like `Complex c;` calls the member function `Complex()` which can have the following implementation

#         Complex:: Complex () { re = im = 0.0; }
# 

# meaning that it sets the real and imaginary parts to zero. Note the
# way a member function is defined. The constructor is the first
# function that is called when an object is instantiated.
# 
# 
# Another possibility is

#         Complex:: Complex () {}
# 

# which means that there is no initialization of the real and imaginary parts. The drawback is that a given compiler can then assign random values to a given variable.
# 
# A call like `Complex a(0.1,1.3);` means that we could call the member function `Complex(double, double)`as

#         Complex:: Complex (double re_a, double im_a) {
#             re = re_a; im = im_a; }
# 

# The simplest member function are those we defined to extract
# the real and imaginary part of a variable. Here you have to recall that these are private data,
# that is they invisible for users of the class.  We obtain a copy of these variables by defining the
# functions

#         double Complex:: Re () const { return re; }} //  getting the real part
#         double Complex:: Im () const { return im; }  //   and the imaginary part
# 

# Note that we have introduced   the declaration  `const`.  What does it mean?
# This declaration means that a variabale cannot be changed within  a called function.
# 
# 
# If we define a variable as
# `const double p = 3;` and then try to change its value, we will get an error when we
# compile our program. This means that constant arguments in functions cannot be changed.

#         // const arguments (in functions) cannot be changed:
#         void myfunc (const Complex& c)
#         { c.re = 0.2; /* ILLEGAL!! compiler error... */  }
# 

# If we declare the function and try to change the value to $0.2$, the compiler will complain by sending
# an error message.
# 
# 
# If we define a function to compute the absolute value of complex variable like

#         double Complex:: abs ()  { return sqrt(re*re + im*im);}
# 

# without the constant declaration  and define thereafter a function
# `myabs` as

#         double myabs (const Complex& c)
#         { return c.abs(); }   // Not ok because c.abs() is not a const func.
# 

# the compiler would not allow the c.abs() call in myabs
# since `Complex::abs` is not a constant member function.
# 
# 
# 
# Constant functions cannot change the object's state.
# To avoid this we declare the function `abs` as

#         double Complex:: abs () const { return sqrt(re*re + im*im); }
# 

# ## Overloading operators
# 
# C++ (and Fortran) allow for overloading of operators. That means we
# can define algebraic operations on for example vectors or any
# arbitrary object.  As an example, a vector addition of the type 
# $\mathbf{c} = \mathbf{a} + \mathbf{b}$ means that we need to write a small part of
# code with a for-loop over the dimension of the array.  We would rather
# like to write this statement as `c = a+b;` as this makes the code much
# more readable and close to eventual equations we want to code.  To
# achieve this we need to extend the definition of operators.
# 
# 
# 
# Let us study the declarations in our complex class.
# In our main function we have a statement like `d = b;`, which means
# that we call `d.operator= (b)` and we have defined a so-called assignment operator
# as a part of the class defined as

#         Complex& Complex:: operator= (const Complex& c)
#         {
#            re = c.re;
#            im = c.im;
#            return *this;
#         }
# 

# With this function, statements like
# `Complex d = b;` or `Complex d(b);`
# make a new object $d$, which becomes a copy of $b$.
# We can make simple implementations in terms of the assignment

#         Complex:: Complex (const Complex& c)
#         { *this = c; }
# 

# which  is a pointer to "this object", `*this` is the present object,
# so `*this = c;` means setting the present object equal to $c$, that is
# `this->operator= (c);`.
# 
# 
# The meaning of the addition operator $+$ for Complex objects is defined in the
# function
# `Complex operator+ (const Complex& a, const Complex& b); // a+b`
# The compiler translates `c = a + b;` into `c = operator+ (a, b);`.
# Since this implies the call to function, it brings in an additional overhead. If speed
# is crucial and this function call is performed inside a loop, then it is more difficult for a
# given compiler to perform optimizations of a loop.
# 
# 
# 
# The solution to this is to inline functions.   We discussed inlining in chapter
# 2 of the lecture notes.
# Inlining means that the function body is copied directly into
# the calling code, thus avoiding calling the function.
# Inlining is enabled by the inline keyword

#         inline Complex operator+ (const Complex& a, const Complex& b)
#         { return Complex (a.re + b.re, a.im + b.im); }
# 

# Inline functions, with complete bodies must be written in the header file  complex.h.
# 
# 
# 
# Consider  the case `c = a + b;`
# that is,  `c.operator= (operator+ (a,b));`
# If `operator+`, `operator=` and the constructor `Complex(r,i)` all
# are inline functions, this transforms to

#         c.re = a.re + b.re;
#         c.im = a.im + b.im;
# 

# by the compiler, i.e., no function calls
# 
# 
# 
# The stand-alone function `operator+` is a friend of the Complex  class

#         class Complex
#         {
#            ...
#            friend Complex operator+ (const Complex& a, const Complex& b);
#            ...
#         };
# 

# so it can read (and manipulate) the private data parts $re$ and
# $im$ via

#         inline Complex operator+ (const Complex& a, const Complex& b)
#         { return Complex (a.re + b.re, a.im + b.im); }
# 

# Since we do not need to alter the re and im variables, we can
# get the values by Re() and Im(), and there is no need to be a
# friend function

#         inline Complex operator+ (const Complex& a, const Complex& b)
#         { return Complex (a.Re() + b.Re(), a.Im() + b.Im()); }
# 

# The multiplication functionality can now be extended to imaginary numbers by the following code

#         inline Complex operator* (const Complex& a, const Complex& b)
#         {
#           return Complex(a.re*b.re - a.im*b.im, a.im*b.re + a.re*b.im);
#         
# 

# It will be convenient to inline all functions used by this operator.
# 
# 
# 
# To inline the complete expression `a*b;`, the constructors and
# `operator=`  must also be inlined.  This can be achieved via the following piece of code

#         inline Complex:: Complex () { re = im = 0.0; }
#         inline Complex:: Complex (double re_, double im_)
#         { ... }
#         inline Complex:: Complex (const Complex& c)
#         { ... }
#         inline Complex:: operator= (const Complex& c)
#         { ... }
# 

#         // e, c, d are complex
#         e = c*d;
#         // first compiler translation:
#         e.operator= (operator* (c,d));
#         // result of nested inline functions
#         // operator=, operator*, Complex(double,double=0):
#         e.re = c.re*d.re - c.im*d.im;
#         e.im = c.im*d.re + c.re*d.im;
# 

# The definitions `operator-` and `operator/` follow the same set up.
# 
# 
# 
# Finally, if we wish to write to file or another device a complex number using the simple syntax
# `cout << c;`, we obtain this by defining
# the effect of $<<$ for a Complex object as

#         ostream& operator<< (ostream& o, const Complex& c)
#         { o << "(" << c.Re() << "," << c.Im() << ") "; return o;}
# 

# ## Templates
# 
# What if we wanted to make a class which takes integers
# or floating point numbers with single precision?
# A simple way to achieve this is copy and paste our class and replace `double` with for
# example `int`.
# 
# C++  allows us to do this automatically via the usage of templates, which
# are the C++ constructs for parameterizing parts of
# classes. Class templates  is a template for producing classes. The declaration consists
# of the keyword `template` followed by a list of template arguments enclosed in brackets.
# 
# 
# 
# We can therefore make a more general class by rewriting our original example as

#         template<class T>
#         class Complex
#         {
#         private:
#            T re, im; // real and imaginary part
#         public:
#            Complex ();                              // Complex c;
#            Complex (T re, T im = 0); // Definition of a complex variable;
#            Complex (const Complex& c);              // Usage: Complex c(a);   // equate two complex variables
#            Complex& operator= (const Complex& c); // c = a;   //  equate two complex variables, same as previous
#           ~Complex () {}                        // destructor
#            T   Re () const;        // T real_part = a.Re();
#            T   Im () const;        // T imag_part = a.Im();
#            T   abs () const;       // T m = a.abs(); // modulus
#            friend Complex operator+ (const Complex&  a, const Complex& b);
#            friend Complex operator- (const Complex&  a, const Complex& b);
#            friend Complex operator* (const Complex&  a, const Complex& b);
#            friend Complex operator/ (const Complex&  a, const Complex& b);
#         };
# 

# What it says is that `Complex` is a parameterized type with $T$ as a parameter and $T$ has to be a type such as double
# or float.
# The class complex is now a class template
# and we would define variables in a code as

#         Complex<double> a(10.0,5.1);
#         Complex<int> b(1,0);
# 

# Member functions of our class are defined by preceding the name of the function with the `template` keyword.
# Consider the function we defined as `Complex:: Complex (double re_a, double im_a)`.
# We would rewrite this function as

#         template<class T>
#         Complex<T>:: Complex (T re_a, T im_a)
#         { re = re_a; im = im_a; }
# 

# The member functions  are otherwise defined following ordinary member function definitions.
# 
# 
# 
# Here follows a very simple first class in the file squared.h

#         // Not all declarations here
#         // Class to compute the square of a number
#         template<class T>
#         class Squared{
#           public:
#             // Default constructor, not used here
#             Squared(){}
#         
#             // Overload the function operator()
#             T operator()(T x){return x*x;}
#         
#         };
# 

# and we would use it as

#         #include <iostream>
#         #include "squared.h"
#         using namespace std;
#         
#         int main(){
#           Squared<double> s;
#           cout << s(3) << endl;
#         
# 

# ## A matrix-vector class, first its usage

#         #include <cmath>
#         #include <iostream>
#         #include <fstream>
#         #include <iomanip>
#         #include "/Users/hjensen/Teaching/fys4411/programs/cgm/vectorclass.h"
#         
#         using namespace  std;
#         
#           Vector ConjugateGradient(Matrix A, Vector b, Vector x0){
#           int dim = x0.Dimension();
#           const double tolerance = 1.0e-14;
#           Vector x(dim),r(dim),v(dim),z(dim);
#           double c,t,d;
#         
#           x = x0;
#           r = b - A*x;
#           v = r;
#           c = dot(r,r);
#           for(int i=0;i<dim;i++){
#             if(sqrt(dot(v,v))<tolerance){
#               cerr << "An error has occurred in ConjugateGradient: execution of function terminated" << endl;
#               break;
#             }
#             z = A*v;
#             t = c/dot(v,z);
#             x = x + t*v;
#             r = r - t*z;
#             d = dot(r,r);
#             if(sqrt(d) < tolerance)
#               break;
#             v = r + (d/c)*v;
#             c = d;
#           }
#           return x;
#         }
#         
#         
#         Vector SteepestDescent(Matrix A, Vector b, Vector x0){
#           int IterMax, i;
#           int dim = x0.Dimension();
#           const double tolerance = 1.0e-14;
#           Vector x(dim),f(dim),z(dim);
#           double c,alpha,d;
#           IterMax = 30;
#           x = x0;
#           f = A*x-b;
#           i = 0;
#           while (i <= IterMax || sqrt(dot(f,f)) < tolerance ){
#             if(sqrt(dot(f,f))<tolerance){
#                cerr << "An error has occurred: execution of function terminated" << endl;
#                break;
#             }
#             z = A*f;
#             c = dot(f,f);
#             alpha = c/dot(f,z);
#             x = x - alpha*f;
#             f =  A*x-b;
#             if(sqrt(dot(f,f)) < tolerance) break;
#             i++;
#           }
#           return x;
#         }
#         
#         //   Main function begins here
#         int main(int  argc, char * argv[]){
#           int dim = 2;
#           Vector x(dim),xsd(dim), b(dim),x0(dim);
#           Matrix A(dim,dim);
#         
#           // Set our initial guess
#           x0(0) = x0(1) = 0;
#           // Set the matrix
#           A(0,0) =  3;    A(1,0) =  2;   A(0,1) =  2;   A(1,1) =  6;
#         
#           cout << "The Matrix A that we are using: " << endl;
#           A.Print();
#           cout << endl;
#         
#           Vector y(dim);
#           y(0) = 2.;
#           y(1) = -2.;
#         
#           cout << "The exact solution is: " << endl;
#           y.Print();
#           cout << endl;
#           b = A*y;
#         
#           cout << "The right hand side, b, of the expression Ax=b: " << endl;
#           b.Print();
#           cout << endl;
#         
#           x = ConjugateGradient(A,b,x0);
#         
#           xsd = SteepestDescent(A,b,x0);
#         
#           cout << "The approximate solution using Conjugate Gradient is: " << endl;
#           x.Print();
#           cout << endl;
#         
#           cout << "The approximate solution using Steepest Descent is: " << endl;
#           xsd.Print();
#           cout << endl;
#         }
# 

# ## A matrix-vector class, the class definitions themselves

#         #ifndef _vectorclass
#         #define _vectorclass
#         
#         
#         #include <cmath>
#         #include <iostream>
#         using namespace  std;
#         
#         
#         
#         class Point;
#         class Vector;
#         class Matrix;
#         
#         
#         /********************************/
#         /*        Point Class        */
#         /********************************/
#         
#         class Point{
#          private:
#           int   dimension;
#           double *data;
#           
#          public:
#           Point(int dim);
#           Point(const Point& v);
#           ~Point();
#           
#           int    Dimension() const;
#         
#           //************************
#           // User Defined Operators
#           //************************
#           int operator==(const Point& v) const;
#           int operator!=(const Point& v) const;
#           Point & operator=(const Point& v);
#         
#           double  operator()(const int i) const;
#           double& operator()(const int i);
#         
#           void Print() const;
#         };
#         
#         
#         
#         /********************************/
#         /*        Vector Class        */
#         /********************************/
#         
#         class Vector{
#          private:
#           int   dimension;
#           double *data;
#           
#          public:
#           Vector();
#           Vector(int dim);
#           Vector(const Vector& v);
#           Vector(int col, const Matrix &A);
#           ~Vector();
#           
#           void Initialize(int dim);
#           int    Dimension() const;
#           double Length();     /* Euclidean Norm of the Vector */
#           void   Normalize();
#         
#           double Norm_l1();
#           double Norm_l2();
#           double Norm_linf();
#           double MaxMod();
#           double ElementofMaxMod();
#           int MaxModindex();
#           
#           //************************
#           // User Defined Operators
#           //************************
#           int operator==(const Vector& v) const;
#           int operator!=(const Vector& v) const;
#           Vector & operator=(const Vector& v);
#         
#           double  operator()(const int i) const;
#           double& operator()(const int i);
#         
#           void Print() const;
#           void Initialize(double a);
#           void Initialize(double *v);
#         };
#         
#         
#         
#         /********************************/
#         /*        Matrix Class        */
#         /********************************/
#         
#         class Matrix {
#         private:
#           int rows, columns;
#           double **data;
#           
#         public:
#         
#           Matrix(int dim);
#           Matrix(int rows1, int columns1);
#           Matrix(const Matrix& m);
#           Matrix(int num_vectors, const Vector * q);
#           Matrix(int rows1, int columns1, double **rowptrs);
#           ~Matrix();
#         
#           int Rows() const;
#           int Columns() const;
#           double ** GetPointer();
#           void GetColumn(int col, Vector &x);
#           void GetColumn(int col, Vector &x, int rowoffset);
#           void PutColumn(int col, const Vector &x);
#           double Norm_l1();
#           double Norm_linf();
#         
#           //************************
#           // User Defined Operators
#           //************************
#           Matrix& operator=(const Matrix& m);
#           double operator()(const int i, const int j) const;
#           double& operator()(const int i, const int j);
#         
#           double MaxModInRow(int row);
#           double MaxModInRow(int row, int starting_column);
#           int MaxModInRowindex(int row);
#           int MaxModInRowindex(int row, int starting_column);
#          
#           double MaxModInColumn(int column);
#           double MaxModInColumn(int column, int starting_row);
#           int MaxModInColumnindex(int column);
#           int MaxModInColumnindex(int column, int starting_row);
#         
#           void RowSwap(int row1, int row2);
#         
#           void Print() const;
#         
#         };
#         
#         
#         /********************************/
#         /*   Operator Declarations      */
#         /********************************/
#         
#         // Unitary operator -
#         Vector operator-(const Vector& v);
#         
#         // Binary operator +,-
#         Vector operator+(const Vector& v1, const Vector& v2);
#         Vector operator-(const Vector& v1, const Vector& v2);
#         
#         // Vector Scaling (multiplication by a scaler : defined commutatively)
#         Vector operator*(const double s, const Vector& v);
#         Vector operator*(const Vector& v, const double s);
#         
#         // Vector Scaling (division by a scaler)
#         Vector operator/(const Vector& v, const double s);
#         
#         Vector operator*(const Matrix& A, const Vector& x); 
#         
#         
#         /********************************/
#         /*   Function Declarations      */
#         /********************************/
#         
#         int min_dimension(const Vector& u, const Vector& v);
#         double dot(const Vector& u, const Vector& v); 
#         double dot(int N, double *a, double *b);
#         double dot(int N, const Vector &u, const Vector &v); 
#         void Swap(double &a, double &b);
#         double Sign(double x);
#         
#         /* Misc. useful functions to have */
#         double log2(double x);
#         double GammaF(double x);
#         int Factorial(int n);
#         double ** CreateMatrix(int m, int n);
#         void DestroyMatrix(double ** mat, int m, int n); 
#         
#         int ** ICreateMatrix(int m, int n);
#         void IDestroyMatrix(int ** mat, int m, int n);
#         
#         #endif
# 

# ## A matrix-vector class, and finally all its functions

#         #include "vectorclass.h"
#         
#         Point::Point(int dim){
#           dimension = dim;
#           data = new double[dimension];
#         
#           for(int i=0;i<dimension;i++)
#             data[i] = 0.0;
#         }
#         
#         
#         Point::Point(const Point &v){
#           dimension = v.Dimension();
#           data = new double[dimension];
#         
#           for(int i=0;i<dimension;i++)
#             data[i] = v.data[i];
#         }
#         
#         
#         Point::~Point(){
#           dimension = 0;
#           delete[] data;
#           data = NULL;
#         }
#         
#         
#         int Point::Dimension() const{
#           return(dimension);
#         }
#         
#         
#         double Point::operator()(const int i) const{
#           if(i>=0 && i<dimension)
#             return data[i];
#         
#           cerr << "Point::Invalid index " << i << " for Point of dimension " << dimension << endl;
#           return(0);
#         }
#         
#         
#         
#         double& Point::operator()(const int i){
#           if(i>=0 && i<dimension)
#             return data[i];
#         
#           cerr << "Point::Invalid index " << i << " for Point of dimension " << dimension << endl;
#           return(data[0]);
#         }
#         
#         
#         Point& Point::operator=(const Point &v) {
#           dimension = v.Dimension();
#           for(int i=0;i<dimension;i++)
#             data[i] = v.data[i];
#           return *this;
#         };
#         
#         void Point::Print() const{
#           cout << endl;
#           cout << "[ ";
#           if(dimension>0)
#             cout << data[0];
#           for(int i=1;i<dimension;i++)
#             cout << "; " << data[i];
#           cout << " ]" << endl;
#         }
#         
#         Vector::Vector(){
#           dimension = 0;
#           data = NULL;
#         }
#         
#         
#         Vector::Vector(int dim){
#           dimension = dim;
#           data = new double[dimension];
#         
#           for(int i=0;i<dimension;i++)
#             data[i] = 0.0;
#         }
#         
#         
#         Vector::Vector(const Vector &v){
#           dimension = v.Dimension();
#           data = new double[dimension];
#         
#           for(int i=0;i<dimension;i++)
#             data[i] = v.data[i];
#         }
#         
#         
#         Vector::Vector(int col, const Matrix &A){
#           dimension = A.Rows();
#         
#           data = new double[dimension];
#           
#           for(int i=0;i<A.Rows();i++)
#             data[i] = A(i,col);
#         
#         }
#         
#         
#         Vector::~Vector(){
#           dimension = 0;
#           delete[] data;
#           data = NULL;
#         }
#         
#         
#         void Vector::Initialize(int dim){
#           if(dimension!=0)
#             delete[] data;
#         
#           dimension = dim;
#           data = new double[dimension];
#           
#           for(int i=0;i<dimension;i++)
#             data[i] = 0.0;
#         }
#         
#         
#         int Vector::Dimension() const{
#           return(dimension);
#         }
#         
#         
#         double Vector::operator()(const int i) const{
#           if(i>=0 && i<dimension)
#             return data[i];
#         
#           cerr << "Vector::Invalid index " << i << " for Vector of dimension " << dimension << endl;
#           return(0);
#         }
#         
#         
#         
#         double& Vector::operator()(const int i){
#           if(i>=0 && i<dimension)
#             return data[i];
#         
#           cerr << "Vector::Invalid index " << i << " for Vector of dimension " << dimension << endl;
#           return(data[0]);
#         }
#         
#         
#         Vector& Vector::operator=(const Vector &v) {
#           dimension = v.Dimension();
#           for(int i=0;i<dimension;i++)
#             data[i] = v.data[i];
#           return *this;
#         };
#         
#         void Vector::Print() const{
#           cout << endl;
#           cout << "[ ";
#           if(dimension>0)
#             cout << data[0];
#           for(int i=1;i<dimension;i++)
#             cout << "; " << data[i];
#           cout << " ]" << endl;
#         }
#         
#         
#         double Vector::Norm_l1(){
#           double sum = 0.0;
#           for(int i=0;i<dimension;i++)
#             sum += fabs(data[i]);
#           return(sum);
#         }
#         
#         
#         double Vector::Norm_l2(){
#           double sum = 0.0;
#           for(int i=0;i<dimension;i++)
#             sum += data[i]*data[i];
#           return(sqrt(sum));
#         }
#         
#         void Vector::Normalize(){
#           double tmp = 1.0/Norm_l2();
#           for(int i=0;i<dimension;i++)
#             data[i] = data[i]*tmp;
#         }
#         
#         
#         double Vector::Norm_linf(){
#           double maxval = 0.0,tmp;
#           
#           for(int i=0;i<dimension;i++){
#             tmp = fabs(data[i]);
#             maxval = (maxval > tmp)?maxval:tmp;
#           }
#           return(maxval);
#         }
#         
#         double Vector::MaxMod(){
#           double maxm = -1.0e+10;
#         
#           for(int i=0; i<dimension; i++)
#             maxm = (maxm > fabs(data[i]))?maxm:fabs(data[i]);
#           
#           return maxm;
#         }
#         
#         double Vector::ElementofMaxMod(){
#           return(data[MaxModindex()]);
#         }
#         
#         
#         int Vector::MaxModindex(){
#           double maxm = -1.0e+10;
#           int maxmindex = 0;
#         
#           for(int i=0; i<dimension; i++){
#             if(maxm<fabs(data[i])){
#               maxm = fabs(data[i]);
#               maxmindex = i;
#             }
#           }
#           
#           return maxmindex;
#         }
#         
#         void Vector::Initialize(double a){
#           for(int i=0; i<dimension; i++)
#             data[i] = a;
#         }
#         
#         void Vector::Initialize(double *v){
#           for(int i=0; i<dimension; i++)
#             data[i] = v[i];
#         }
#         
#         Matrix::Matrix(int dim){
#           rows = dim;
#           columns = dim;
#           data = new double*[rows];
#           for(int i=0;i<rows;i++){
#             data[i] = new double[columns];
#             for(int j=0;j<columns;j++)
#               data[i][j] = 0.0;
#           }
#         }
#         
#           
#         Matrix::Matrix(int rows1, int columns1){
#           rows = rows1;
#           columns = columns1;
#         
#           data = new double*[rows];
#           for(int i=0;i<rows;i++){
#             data[i] = new double[columns];
#             for(int j=0;j<columns;j++)
#               data[i][j] = 0.0;
#           }
#         }
#         
#         Matrix::Matrix(const Matrix& m){
#           rows = m.rows;
#           columns = m.columns;
#         
#           data = new double*[rows];
#         
#           for(int i=0;i<rows;i++){
#             data[i] = new double[columns];
#             for(int j=0; j<columns; j++)
#               data[i][j] = m.data[i][j];
#           }
#         }
#         
#         Matrix::Matrix(int num_Vectors, const Vector * q){
#           rows = q[0].Dimension();
#           columns = num_Vectors;
#         
#           data = new double*[rows];
#         
#           for(int i=0;i<rows;i++){
#             data[i] = new double[columns];
#             for(int j=0; j<columns; j++)
#               data[i][j] = q[j](i);
#           }
#         }
#         
#         Matrix::Matrix(int rows1, int columns1, double **rowptrs){
#           rows = rows1;
#           columns = columns1;
#         
#           data = new double*[rows];
#         
#           for(int i=0;i<rows;i++)
#             data[i] = rowptrs[i];
#         }
#         
#         
#         Matrix::~Matrix(){
#           for(int i=0;i<rows;i++)
#             delete[] data[i];
#         
#           rows = 0;
#           columns = 0;
#           delete[] data;
#         }
#         
#         int Matrix::Rows() const{
#           return(rows);
#         }  
#         
#         int Matrix::Columns() const{
#           return(columns);
#         }  
#         
#         
#         double **Matrix::GetPointer(){
#           return(data);
#         }
#         
#         void Matrix::GetColumn(int col, Vector &x){
#           x.Initialize(0.0);
#           for(int i=0;i<rows;i++)
#             x(i) = data[i][col];
#         }
#         
#         void Matrix::GetColumn(int col, Vector &x, int rowoffset){
#           x.Initialize(0.0);
#           for(int i=0;i<rows-rowoffset;i++)
#             x(i) = data[i+rowoffset][col];
#         }
#         
#         void Matrix::PutColumn(int col, const Vector &x){
#           for(int i=0;i<rows;i++)
#             data[i][col] = x(i);
#         }
#         
#         
#         double Matrix::Norm_linf(){
#           double maxval = 0.0,sum;
#           
#           for(int i=0;i<rows;i++){
#             sum = 0.0;
#             for(int j=0;j<columns;j++)
#               sum += fabs(data[i][j]);
#             maxval = (maxval > sum)?maxval:sum;
#           }
#           return(maxval);
#         }
#         
#         
#         double Matrix::Norm_l1(){
#           double maxval = 0.0,sum;
#         
#           for(int j=0;j<columns;j++){
#             sum = 0.0;
#             for(int i=0;i<rows;i++)
#               sum += fabs(data[i][j]);
#             maxval = (maxval > sum)?maxval:sum;
#           }
#           return(maxval);
#         }
#         
#         
#         
#         Matrix& Matrix::operator=(const Matrix &m){
#           if( (rows == m.rows) && (columns == m.columns)){
#             for(int i=0; i<rows; i++)
#               for(int j=0;j<columns;j++){
#         	data[i][j] = m.data[i][j];
#               }
#           }
#           else
#             cerr << "Matrix Error: Cannot equate matrices of different sizes\n";
#           return *this;
#         }
#         
#           
#         double Matrix::operator()(const int i, const int j) const {
#           if( (i>=0) && (j>=0) && (i<rows) && (j<columns))
#             return(data[i][j]);  
#           else
#             cerr << "Matrix Error: Invalid Matrix indices (" << i << "," << j << 
#               "), for Matrix of size " << rows << " X " << columns << endl;
#           return((double)0);
#         }
#           
#         
#         double& Matrix::operator()(const int i, const int j) {
#           if( (i>=0) && (j>=0) && (i<rows) && (j<columns))
#             return(data[i][j]);  
#           else
#             cerr << "Matrix Error: Invalid Matrix indices (" << i << "," << j << 
#               "), for Matrix of size " << rows << " X " << columns << endl;;
#           return(data[0][0]);
#         }
#         
#         
#         void Matrix::Print() const{
#           cout << endl;
#         
#         
#           cout << "[ ";
#           for(int i=0;i<rows;i++){
#             cout << data[i][0];
#             for(int j=1;j<columns;j++)
#               cout << " " << data[i][j];
#             if(i!=(rows-1))
#               cout << ";\n";
#           }
#           cout << " ]" << endl;
#         }
#         
#         
#         double Matrix::MaxModInRow(int row){
#           double maxv = -1.0e+10;
#           for(int i=0;i<columns;i++)
#             maxv = (fabs(data[row][i])>maxv)?fabs(data[row][i]):maxv;
#         
#           return maxv;
#         }
#         
#         double Matrix::MaxModInRow(int row, int starting_column){
#           double maxv = -1.0e+10;
#           for(int i=starting_column;i<columns;i++)
#             maxv = (fabs(data[row][i])>maxv)?fabs(data[row][i]):maxv;
#         
#           return maxv;
#         }
#         
#         int Matrix::MaxModInRowindex(int row){
#           int maxvindex = 0;
#           double maxv = -1.0e+10;
#           
#           for(int i=0;i<columns;i++){
#             if(maxv < fabs(data[row][i])){
#               maxv = fabs(data[row][i]);
#               maxvindex = i;
#             }
#           }
#         
#           return maxvindex;
#         }
#         
#         int Matrix::MaxModInRowindex(int row, int starting_column){
#           int maxvindex = 0;
#           double maxv = -1.0e+10;
#         
#           for(int i=starting_column;i<columns;i++){
#             if(maxv < fabs(data[row][i])){
#               maxv = fabs(data[row][i]);
#               maxvindex = i;
#             }
#           }
#           
#           return maxvindex;
#         }
#         
#         double Matrix::MaxModInColumn(int column){
#           double maxv = -1.0e+10;
#           for(int i=0;i<rows;i++)
#             maxv = (fabs(data[i][column])>maxv)?fabs(data[i][column]):maxv;
#         
#           return maxv;
#         }
#         
#         double Matrix::MaxModInColumn(int column, int starting_row){
#           double maxv = -1.0e+10;
#           for(int i=starting_row;i<rows;i++)
#             maxv = (fabs(data[i][column])>maxv)?fabs(data[i][column]):maxv;
#         
#           return maxv;
#         }
#         
#         int Matrix::MaxModInColumnindex(int column){
#           int maxvindex = 0;
#           double maxv = -1.0e+10;
#           
#           for(int i=0;i<rows;i++){
#             if(maxv < fabs(data[i][column])){
#               maxv = fabs(data[i][column]);
#               maxvindex = i;
#             }
#           }
#         
#           return maxvindex;
#         }
#         
#         int Matrix::MaxModInColumnindex(int column, int starting_column){
#           int maxvindex = 0;
#           double maxv = -1.0e+10;
#         
#           for(int i=starting_column;i<rows;i++){
#             if(maxv < fabs(data[i][column])){
#               maxv = fabs(data[i][column]);
#               maxvindex = i;
#             }
#           }
#           
#           return maxvindex;
#         }
#         
#         void Matrix::RowSwap(int row1, int row2){
#           double * tmp = data[row1];
#           data[row1] = data[row2];
#           data[row2] = tmp;
#         }
#         
#         
#         
#         /****************************************************************/
#         /*                 Operator Definitions                         */
#         /****************************************************************/
#         
#         
#         Vector operator-(const Vector& v){
#           Vector x(v.Dimension());
#           for(int i=0;i<v.Dimension();i++)
#             x(i) = -v(i);
#           return x;
#         }
#         
#         
#         Vector operator+(const Vector& v1, const Vector& v2){
#           int min_dim = min_dimension(v1,v2);
#           Vector x(min_dim);
#           for(int i=0;i<min_dim;i++)
#             x(i) = v1(i) + v2(i);
#           return x;
#         }
#         
#         
#         Vector operator-(const Vector& v1, const Vector& v2){
#           int min_dim = min_dimension(v1,v2);
#           Vector x(min_dim);
#           for(int i=0;i<min_dim;i++)
#             x(i) = v1(i) - v2(i);
#           return x;
#         }
#         
#         
#         Vector operator/(const Vector& v, const double s) {
#           Vector x(v.Dimension());
#           for(int i=0;i<v.Dimension();i++)
#             x(i) = v(i)/s;
#           return x;
#         }
#         
#         
#         
#         Vector operator*(const double s, const Vector &v) {
#           Vector x(v.Dimension());
#           for(int i=0;i<v.Dimension();i++)
#             x(i) = s*v(i);
#           return x;
#         }
#         
#         
#         Vector operator*(const Vector& v, const double s) {
#           Vector x(v.Dimension());
#           for(int i=0;i<v.Dimension();i++)
#             x(i) = s*v(i);
#           return x;
#         }
#         
#         Vector operator*(const Matrix& A, const Vector& x){
#           int rows = A.Rows(), columns = A.Columns();
#           int dim = x.Dimension();
#           Vector b(dim);
#           
#           if(columns != dim){
#             cerr << "Invalid dimensions given in matrix-vector multiply" << endl;
#             return(b);
#           }
#           
#           for(int i=0;i<rows;i++){
#             b(i) = 0.0;
#             for(int j=0;j<columns;j++){
#               b(i) += A(i,j)*x(j);
#             }
#           }
#           
#           return b;
#         }
#         
#         
#         /****************************************************************/
#         /*                 Function Definitions                         */
#         /****************************************************************/
#         
#         int min_dimension(const Vector& v1, const Vector& v2){
#           int min_dim = (v1.Dimension()<v2.Dimension())?v1.Dimension():v2.Dimension();
#           return(min_dim);
#         }
#         
#         
#         double dot(const Vector& u, const Vector& v){
#           double sum = 0.0;
#           int min_dim = min_dimension(u,v);
#         
#           for(int i=0;i<min_dim;i++)
#             sum += u(i)*v(i);
#           
#           return sum; 
#         }
#         
#         
#         double dot(int N, const Vector& u, const Vector& v){
#           double sum = 0.0;
#         
#           for(int i=0;i<N;i++)
#             sum += u(i)*v(i);
#           
#           return sum;
#         }
#         
#         
#         double dot(int N, double *a, double *b){
#           double sum = 0.0;
#           
#           for(int i=0;i<N;i++)
#             sum += a[i]*b[i];
#         
#           return sum;
#         }
#         
#         
#         /*******************************/
#         /*   Log base 2 of a number    */
#         /*******************************/
#         
#         double log2(double x){
#           return(log(x)/log(2.0));
#         }
#         
#         void Swap(double &a, double &b){
#           double tmp = a;
#           a = b;
#           b = tmp;
#         }
#         
#         double Sign(double x){
#           double xs;
#         
#           xs = (x>=0.0)?1.0:-1.0;
#         
#           return xs;
#         }
#         
#         //GammaF function valid for x integer, or x (integer+0.5)
#         double GammaF(double x){
#           double gamma = 1.0;
#           
#           if (x == -0.5) 
#             gamma = -2.0*sqrt(M_PI);
#           else if (!x) return gamma;
#           else if ((x-(int)x) == 0.5){ 
#             int n = (int) x;
#             double tmp = x;
#             
#             gamma = sqrt(M_PI);
#             while(n--){
#               tmp   -= 1.0;
#               gamma *= tmp;
#             }
#           }
#           else if ((x-(int)x) == 0.0){
#             int n = (int) x;
#             double tmp = x;
#             
#             while(--n){
#               tmp   -= 1.0;
#               gamma *= tmp;
#             }
#           }  
#           
#           return gamma;
#         }
#         
#         
#         int Factorial(int n){
#           int value=1;
#           for(int i=n;i>0;i--)
#             value = value*i;
#         
#           return value;
#         }
#         
#         double ** CreateMatrix(int m, int n){
#           double ** mat;
#           mat = new double*[m];
#           for(int i=0;i<m;i++){
#             mat[i] = new double[n];
#             for(int j=0;j<m;j++)
#               mat[i][j] = 0.0;
#           }
#           return mat;
#         }
#         
#         int ** ICreateMatrix(int m, int n){
#           int ** mat;
#           mat = new int*[m];
#           for(int i=0;i<m;i++){
#             mat[i] = new int[n];
#             for(int j=0;j<m;j++)
#               mat[i][j] = 0;
#           }
#           return mat;
#         }
#         
#         void DestroyMatrix(double ** mat, int m, int n){
#           for(int i=0;i<m;i++)
#             delete[] mat[i];
#           delete[] mat;
#         }
#         
#         void IDestroyMatrix(int ** mat, int m, int n){
#           for(int i=0;i<m;i++)
#             delete[] mat[i];
#           delete[] mat;
#         }
#         
#         
#         
#         
#         
#         
#         
#         
# 
