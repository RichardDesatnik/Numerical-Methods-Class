// start.cpp
//
// This program performs a series of mathematical operations on a set of integers read in from a file.
// 
//*****************
#include <iostream> // this is a standard C++ header, and should be included in all programs
#include <fstream>
#include <iomanip>
#include <math.h>
#include <time.h>
using namespace std;
//*****************

// declaration of functions/subroutines

int polynomial(int i);	// a polynomial to be evaluated
double dpolynomial(double i);	// a polynomial to be evaluated

// declaration of input and output stream

ifstream data_in("input_start.txt"); // input data
ofstream data_out("output.txt"); // output data


// the main part of the program - should always be type "int"

int main() {
	
	// variable declarations
    int i,j,k; // loop counters
    const int upper = 5; // upper limit on calculation loop, corresponds to number of entries in the input file
    					  // declared as a "const int" so that arrays can be defined with this size
    int numbers[upper]; // array to store numbers, in C++, the array index starts at 0!
    bool sq; // boolean that indicates if the number is a perfect square
    int pol; // value of polynomial function
    double dpol;
    int quotient, divisor, remainder;
    char prime[200], square[200]; // strings for output
    
    // read in data from file
    for(i=0;i<upper;i++) data_in>>numbers[i];
    
    // calculation loop
    
    for(i=0;i<upper;i++){ // the loop will run over the elements in numbers[]
	   
	    // first, determine if the number is a perfect square
	   
	    sprintf(square," is not a perfect square"); //default
	    if(numbers[i]<0) sprintf(square," is negative so that the concept of a perfect square is undefined for real numbers");
		else {
			quotient = numbers[i];
			divisor = 2;
			sq = false;
			while(sq == false && quotient > divisor) {
				quotient  = numbers[i]/divisor;
				remainder = numbers[i]%divisor;
				if (quotient == divisor && remainder == 0) {
					sq = true;
					sprintf(square," is a perfect square"); 
				}	
				else divisor = divisor + 1;
			}
		}
	    
		
	    // second, evaluate the polynomial function
	    
	    pol = polynomial(numbers[i]); // as an integer
	    dpol = dpolynomial(double(numbers[i])); // as a double
	    
	    //third, determine if the number is prime
	    
	    sprintf(prime,"prime"); //default
	    
	    
	    if(numbers[i]<=0) sprintf(prime," is negative or zero, so that the concept of a prime number is undefined");
	    
	    if(numbers[i]>2) { // positive numbers less than 3 are prime
	    
	    	for(j=2;j<=floor(numbers[i]/2);j++) {
		  	  if(numbers[i]%j==0) sprintf(prime,"not prime"); // check if j is a factor
		  	  if(prime == "not prime") break; // exits the j loop once we find a factor
	    	}
    	}
  	    
	    //output the data
	    
	    data_out<<"The number "<<numbers[i]<<square<<", "<<prime<<", and returns a value of "<<dpol<<" when inserted into the function f"<<endl;  
    } 
}	
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
int polynomial(int i) {
    int f, i2;
    
    i2=i*i;
    
    f = -1*i2 + 4*i - 3;
    
    return f;
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
double dpolynomial(double d) {
    double f, d2;
    
    d2=d*d;
    
    f = -1.*d2 + 4.*d - 3.;
    
    return f;
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

