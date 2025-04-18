// NM_Hmk3.cpp
//
//Andrew ID: rdesatni
//Name: Richard Desatnik 
//Homework: Problem 3
// 
/************************ 
Assignment
Problem 1 (20 points) Write a program to find the roots of a single non-linear equation. For a
given function, your program should be able to:
v Identify bracketed regions that enclose a root so as to generate initial guesses.
v Iterate using Newton's method to the root to within a given tolerance.
v Find all roots in one execution.
Use your program to find the real roots of the following two equations to within 10-6. Submit your
code and the generated output.
*/
//*****************
#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
#include <time.h>
#include <stdio.h>
using namespace std;
//*****************
// declaration of functions/subroutines
double New_Meth(double x);	//Newtons Method function, returns roots
ofstream data_out("C:/Users/rdesa/NM/output_hmk5.txt"); // output data
// the main part of the program - should always be type "int"
int main() {
	// variable declarations
    int i,j,k; //Loop varibles
    const int n = 200; // Size of Vector
    const int m = 5;
    double LowerBound_i = -2.; // Lowest x value for sin(x)+ln(x) - 1 (cannot go below zero)
    double UpperBound_i = 2.;// Highest x value for sin(x)+ln(x) - 1
    double LowerBound_ii = -2.; // Lowest x value for e^x + x^2 + 3x - 2 
    double UpperBound_ii = 2.;// Highest x value for e^x + x^2 + 3x - 2

    double deltax = 0.1; // Change in x over loop
    double guess;
    double root;
    double New_Meth(int func, double guess);

    //changing parameters based on function 1 or 2
    int func1;
    int func2;
    int func3;
    int func4;
    int func5;
    
    int func;

    double x1i[n]; //range of x values to run function 1  
    double x1ii[n]; //range of x values to run function 2 
    double y1[n]; //output of sin(x)+ln(x) - 1 
    double y2[n]; //output of e^x + x^2 + 3x - 2
    double y3[n];
    double y4[n];
    double y5[n];
    //bracket vector for "Identify bracketed regions that enclose a root so as to generate initial guesses."
    double brackets1_low[m]; 
    double brackets1_high[m]; 
    double brackets2_low[m]; 
    double brackets2_high[m]; 
    double brackets3_low[m]; 
    double brackets3_high[m]; 
    double brackets4_low[m]; 
    double brackets4_high[m]; 
    double brackets5_low[m]; 
    double brackets5_high[m]; 

	// generate x vectors for both functions
	for(i=0;i<n;i++) {
		x1i[i] = LowerBound_i + (deltax * i);
	}

    for(i=0;i<n;i++) {
		x1ii[i] = LowerBound_ii + (deltax * i);
	}
    

    // generate y1 vector for function f(x) = sin(x)+ln(x) - 1
    for(i=0;i<n;i++) {
		//y1[i] = std::sin(x1i[i]) + std::log(x1i[i]) - 1;
        y1[i] = ((3./2.)*(pow(x1i[i],2))) - 0.5;
	}
    // generate y2 vector for function e^x + x^2 + 3x - 2
    for(i=0;i<n;i++) {
		y2[i] = ((5./2.)*(pow(x1ii[i],3))) - ((3./2.)*(x1ii[i]));
	}
    for(i=0;i<n;i++) {
		y3[i] = ((35./8.)*(pow(x1i[i],4))) - ((30./8.)*(pow(x1i[i],2))) + (3./8.);
	}
    for(i=0;i<n;i++) {
		y4[i] = ((63./8.)*(pow(x1i[i],5))) - ((70./8.)*(pow(x1i[i],3))) + ((15./8.)*(x1i[i]));
	}
    for(i=0;i<n;i++) {
		y5[i] = ((231./16.)*(pow(x1i[i],6))) - ((315./16.)*(pow(x1i[i],4))) + ((105./16.)*(pow(x1i[i],2))) - (5./16.);
	}

    k = 0;
    for(i=1;i<n-1;i++) { //generate bracketed regions based on change in sign from function. For function: f(x) = sin(x)+ln(x) - 1
        //check change in sign of f(x)
        if (std::signbit(y1[i]) != std::signbit(y1[i-1])){
            brackets1_high[k] = x1i[i];
            brackets1_low[k] = x1i[i-1];
            //Print initial guesses for function 1 to the user
            cout<<"Bracketed Region function 1: " << brackets1_high[k] << " to " << brackets1_low[k]<<'\t';
            cout<<endl;
            cout<<"Guess function 1: "<<brackets1_high[k]<<'\t';
	        cout<<endl;
            data_out<<"Bracketed Region function 1: " << brackets1_high[k] << " to " << brackets1_low[k]<<endl;
            data_out<<"Guess function 1: "<<brackets1_high[k]<<endl;
            k++;       
       }
   }
   int max_func1 = k;

    k = 0;
   for(i=1;i<n-1;i++) { //generate bracketed regions based on change in sign from function. For function: e^x + x^2 + 3x - 2
    //check change in sign of f(x)
    if (std::signbit(y2[i]) != std::signbit(y2[i-1])){
            brackets2_high[k] = x1ii[i];
            brackets2_low[k] = x1ii[i-1];
            //Print initial guesses for function 2 to the user
            cout<<"Bracketed Region function 2: " << brackets2_high[k] << " to " << brackets2_low[k]<<'\t';
            cout<<endl;
            cout<<"Guess function 2: "<<brackets2_high[k]<<'\t';
            cout<<endl;
            data_out<<"Bracketed Region function 2: " << brackets2_high[k] << " to " << brackets2_low[k]<<endl;
            data_out<<"Guess function 2: "<<brackets2_high[k]<<endl;
            k++; 
       }
   }
   int max_func2 = k;

   k = 0;
   for(i=1;i<n-1;i++) { //generate bracketed regions based on change in sign from function. For function: e^x + x^2 + 3x - 2
    //check change in sign of f(x)
    if (std::signbit(y3[i]) != std::signbit(y3[i-1])){
            brackets3_high[k] = x1i[i];
            brackets3_low[k] = x1i[i-1];
            //Print initial guesses for function 2 to the user
            cout<<"Bracketed Region function 3: " << brackets3_high[k] << " to " << brackets3_low[k]<<'\t';
            cout<<endl;
            cout<<"Guess function 3: "<<brackets3_high[k]<<'\t';
            cout<<endl;
            data_out<<"Bracketed Region function 3: " << brackets3_high[k] << " to " << brackets3_low[k]<<endl;
            data_out<<"Guess function 3: "<<brackets3_high[k]<<endl;
            k++; 
       }
   }
   int max_func3 = k;

   k = 0;
   for(i=1;i<n-1;i++) { //generate bracketed regions based on change in sign from function. For function: e^x + x^2 + 3x - 2
    //check change in sign of f(x)
    if (std::signbit(y4[i]) != std::signbit(y4[i-1])){
            brackets4_high[k] = x1i[i];
            brackets4_low[k] = x1i[i-1];
            //Print initial guesses for function 2 to the user
            cout<<"Bracketed Region function 4: " << brackets4_high[k] << " to " << brackets4_low[k]<<'\t';
            cout<<endl;
            cout<<"Guess function 4: "<<brackets4_high[k]<<'\t';
            cout<<endl;
            data_out<<"Bracketed Region function 4: " << brackets4_high[k] << " to " << brackets4_low[k]<<endl;
            data_out<<"Guess function 4: "<<brackets4_high[k]<<endl;
            k++; 
       }
   }
   int max_func4 = k;

   k = 0;
   for(i=1;i<n-1;i++) { //generate bracketed regions based on change in sign from function. For function: e^x + x^2 + 3x - 2
    //check change in sign of f(x)
    if (std::signbit(y5[i]) != std::signbit(y5[i-1])){
            brackets5_high[k] = x1i[i];
            brackets5_low[k] = x1i[i-1];
            //Print initial guesses for function 2 to the user
            cout<<"Bracketed Region function 5: " << brackets5_high[k] << " to " << brackets5_low[k]<<'\t';
            cout<<endl;
            cout<<"Guess function 5: "<<brackets5_high[k]<<'\t';
            cout<<endl;
            data_out<<"Bracketed Region function 5: " << brackets5_high[k] << " to " << brackets5_low[k]<<endl;
            data_out<<"Guess function 5: "<<brackets5_high[k]<<endl;
            k++; 
       }
   }
   int max_func5 = k;

   //iterate through inital bracketed guesses from function 1 using Newton Method function to obtain all roots 
   for (i=0;i<max_func1;i++){
        func1 = 1;
        guess = brackets1_high[i];
        root = New_Meth(func1, guess);
        //Print Roots of function1 on Screen
        cout<<"Root function 1: "<<root<<'\t';
        cout<<endl;
        data_out<<"Root function 1: "<<root<<endl;
    }

    //iterate through inital bracketed guesses from function 2 using Newton Method function to obtain all roots 
    for (i=0;i<max_func2;i++){
            func2 = 2;
            guess = brackets2_high[i];
            root = New_Meth(func2, guess);
            //Print Roots of function2 on Screen
            cout<<"Root function 2: "<<root<<'\t';
            cout<<endl;
            data_out<<"Root function 2: "<<root<<endl;
        }

    for (i=0;i<max_func3;i++){
            func3 = 3;
            guess = brackets3_high[i];
            root = New_Meth(func3, guess);
            //Print Roots of function3 on Screen
            cout<<"Root function 3: "<<root<<'\t';
            cout<<endl;
            data_out<<"Root function 3: "<<root<<endl;
        }
    
    for (i=0;i<max_func4;i++){
            func4 = 4;
            guess = brackets4_high[i];
            root = New_Meth(func4, guess);
            //Print Roots of function4 on Screen
            cout<<"Root function 4: "<<root<<'\t';
            cout<<endl;
            data_out<<"Root function 4: "<<root<<endl;
        }

    for (i=0;i<max_func5;i++){
            func5 = 5;
            guess = brackets5_high[i];
            root = New_Meth(func5, guess);
            //Print Roots of function5 on Screen
            cout<<"Root function 5: "<<root<<'\t';
            cout<<endl;
            data_out<<"Root function 5: "<<root<<endl;
        }

}	
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//function to perform Newton's Method
double New_Meth(int func, double guess) {
    double y1_prime;
    double y2_prime;
    double y3_prime;
    double y4_prime;
    double y5_prime;
    double y1_func;
    double y2_func;
    double y3_func;
    double y4_func;
    double y5_func;

    int max = 10;
    int j = 0;
    double new_guess = 0;
    // if function 1 use function 1 -> f(x) = sin(x)+ln(x) - 1 and derivative of function1 -> f'(x) = cos(x)+(1/x)
    if (func == 1){
        for (j=0;j<max;j++) {
            y1_func = ((3./2.)*(pow(guess,2))) - 0.5;
            y1_prime = 3.*guess;
            // Run Newtons Method -> x_new = x_old - f(x_old)/f'(x_old)
            new_guess = guess - (y1_func/y1_prime);
            if (abs(y1_func) < std::pow(10,-7)){ // if tolerance of 10^-7 is reached break for loop return root
                break;
            }
            guess = new_guess;
        }
    }

    // if function 2 use function 2 -> e^x + x^2 + 3x - 2 and derivative of function 2 -> e^x + 2x + 3
    if (func == 2){
        for (j=0;j<max;j++) {
            y2_func = ((5./2.)*(pow(guess,3))) - ((3./2.)*(guess));
            y2_prime = ((15./2.)*(pow(guess,2))) - (3./2.);

            // Run Newtons Method -> x_new = x_old - f(x_old)/f'(x_old)
            new_guess = guess - (y2_func/y2_prime);
            if (abs(y2_func) < std::pow(10,-7)){ // if tolerance of 10^-7 is reached break for loop return root
                break;
            }
            guess = new_guess;
        }
    }

    if (func == 3){
        for (j=0;j<max;j++) {
            y3_func = ((35./8.)*(pow(guess,4))) - ((30./8.)*(pow(guess,2))) + (3./8.);
            y3_prime = (((35.*4.)/8.)*(pow(guess,3))) - (((30.*2.)/8.)*(guess));
    
            // Run Newtons Method -> x_new = x_old - f(x_old)/f'(x_old)
            new_guess = guess - (y3_func/y3_prime);
            if (abs(y3_func) < std::pow(10,-7)){ // if tolerance of 10^-7 is reached break for loop return root
                break;
            }
            guess = new_guess;
        }
    }

    if (func == 4){
        for (j=0;j<max;j++) {
            y4_func = ((63./8.)*(pow(guess,5))) - ((70./8.)*(pow(guess,3))) + ((15./8.)*(guess));
            y4_prime = (((63.*5.)/8.)*(pow(guess,4))) - (((70.*3.)/8.)*(pow(guess,2))) + ((15./8.));
        
            // Run Newtons Method -> x_new = x_old - f(x_old)/f'(x_old)
            new_guess = guess - (y4_func/y4_prime);
            if (abs(y4_func) < std::pow(10,-7)){ // if tolerance of 10^-7 is reached break for loop return root
                break;
            }
            guess = new_guess;
        }   
    }

    if (func == 5){
        for (j=0;j<max;j++) {
            y5_func = ((231./16.)*(pow(guess,6))) - ((315./16.)*(pow(guess,4))) + ((105./16.)*(pow(guess,2))) - (5./16.);
            y5_prime = (((231.*6.)/16.)*(pow(guess,5))) - (((315.*4.)/16.)*(pow(guess,3))) + (((105.*2.)/16.)*(guess));
        
            // Run Newtons Method -> x_new = x_old - f(x_old)/f'(x_old)
            new_guess = guess - (y5_func/y5_prime);
            if (abs(y5_func) < std::pow(10,-7)){ // if tolerance of 10^-7 is reached break for loop return root
                break;
            }
            guess = new_guess;
        }   
    }

    //return final root
  return new_guess;
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////