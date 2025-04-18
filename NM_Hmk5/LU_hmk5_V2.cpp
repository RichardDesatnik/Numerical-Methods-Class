// LU.cpp
// This program decomposes a matrix into LU format and solves a system of equations given a b vector
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
double q(double x);	// heat generation function, x is the position
// declaration of output stream
ofstream data_out("C:/Users/rdesa/output_hmk5_prob1d_n_6.txt"); // output data
// the main part of the program - should always be type "int"

int main() {
	// variable declarations
    int i,j,k,l; // loop counters 
    const int n = 6;//2,3,4,5 // number of points in discretization
    double A[n][n]; // coefficient matrix
    double L[n][n]; // lower triangular matrix
    double U[n][n]; // upper triangular matrix
    double x[n]; // solution vector
    double y[n]; // intermediate solution vector
    double sum; // dummy variable to keep track of sums in decomposition

//n=2

 //A[0][0] = 1;
 //A[0][1] = 1;
 //A[1][0] = -0.57735;
 //A[1][1] = 0.57735;
 //double b[] = {2,0};


//n=3
// A[0][0] = 1;
// A[0][1] = 1;
// A[0][2] = 1;
// A[1][0] = -.774597;
// A[1][1] = 0;
// A[1][2] = .774597;
// A[2][0] = pow(-.774597,2);
// A[2][1] = 0;
// A[2][2] = pow(.774597,2);

// double b[] = {2.,0,(2./3.)};

//n=4
// A[0][0] = 1;
// A[0][1] = 1;
// A[0][2] = 1;
// A[0][3] = 1;
// A[1][0] = -.339981;
// A[1][1] = .339981;
// A[1][2] = -.861136;
// A[1][3] = .861136;
// A[2][0] = pow(-.339981,2);
// A[2][1] = pow(.339981,2);
// A[2][2] = pow(-.861136,2);
// A[2][3] = pow(.861136,2);
// A[3][0] = pow(-.339981,3);
// A[3][1] = pow(.339981,3);
// A[3][2] = pow(-.861136,3);
// A[3][3] = pow(.861136,3);

// double b[] = {2.,0,(2./3.),0};

//n = 5
// A[0][0] = 1.;
// A[0][1] = 1.;
// A[0][2] = 1.;
// A[0][3] = 1.;
// A[0][4] = 1.;

// A[1][0] = -.538469;
// A[1][1] = -.90618;
// A[1][2] = 0.;
// A[1][3] = .90618;
// A[1][4] = .538469;

// A[2][0] = pow(-.538469,2.);
// A[2][1] = pow(-.90618,2.);
// A[2][2] = pow(0.,2.);
// A[2][3] = pow(.90618,2.);
// A[2][4] = pow(.538469,2.);

// A[3][0] = pow(-.538469,3.);
// A[3][1] = pow(-.90618,3.);
// A[3][2] = pow(0.,3.);
// A[3][3] = pow(.90618,3.);
// A[3][4] = pow(.538469,3.);

// A[4][0] = pow(-.538469,4.);
// A[4][1] = pow(-.90618,4.);
// A[4][2] = pow(0.,4.);
// A[4][3] = pow(.90618,4.);
// A[4][4] = pow(.538469,4.);

// double b[] = {2.,0,(2./3.),0,(2./5.)};

 //n = 6
 A[0][0] = 1.;
 A[0][1] = 1.;
 A[0][2] = 1.;
 A[0][3] = 1.;
 A[0][4] = 1.;
 A[0][5] = 1.;

 A[1][0] = -.93247;
 A[1][1] = -.661209;
 A[1][2] = -.238619;
 A[1][3] = .238619;
 A[1][4] = .661209;
 A[1][5] = .93247;

 A[2][0] = pow(-.93247,2.);
 A[2][1] = pow(-.661209,2.);
 A[2][2] = pow(-.238619,2.);
 A[2][3] = pow(.238619,2.);
 A[2][4] = pow(.661209,2.);
 A[2][5] = pow(.93247,2.); 

 A[3][0] = pow(-.93247,3.);
 A[3][1] = pow(-.661209,3.);
 A[3][2] = pow(-.238619,3.);
 A[3][3] = pow(.238619,3.);
 A[3][4] = pow(.661209,3.);
 A[3][5] = pow(.93247,3.);

 A[4][0] = pow(-.93247,4.);
 A[4][1] = pow(-.661209,4.);
 A[4][2] = pow(-.238619,4.);
 A[4][3] = pow(.238619,4.);
 A[4][4] = pow(.661209,4.);
 A[4][5] = pow(.93247,4.);

 A[5][0] = pow(-.93247,5.);
 A[5][1] = pow(-.661209,5.);
 A[5][2] = pow(-.238619,5.);
 A[5][3] = pow(.238619,5.);
 A[5][4] = pow(.661209,5.);
 A[5][5] = pow(.93247,5.);

 double b[] = {2.,0,(2./3.),0,(2./5.),0};
      //////////////////////////////////////////////Insert LU
      // initialize L and U
   for(i=0;i<n;i++) {
    for(j=0;j<n;j++){
      L[i][j] = 0.;
      U[i][j] = 0.;
    }
  //}
  for(i=0;i<n;i++){ // for Crout reduction
  U[i][i]=1.;
  }
  }
  // Do the LU decomposition using the Crout reduction
  for(i=0;i<n;i++) { // loop over pairs of L columns and U rows. The three levels of loop indicate n^3 behavior
    // first, column i of L
      for(j=0;j<n;j++) { // i is the row
     sum=0.;
     for(k=0;k<=i-1;k++){ 
      sum = sum + L[j][k]*U[k][i];
     }
     L[j][i] = A[j][i] - sum;
   }
 // second, row i of U	   
     for(j=i+1;j<n;j++){ // j is the column
        sum = 0.;
        for(k=0;k<=i-1;k++){ 
        sum = sum + L[i][k]*U[k][j];
        }
        U[i][j] = (A[i][j] - sum)/L[i][i];
      }
  }
  y[0] = b[0]/L[0][0];
  for(i=1;i<n;i++) {
    sum = 0.;
    for(j=0;j<i;j++){
      sum = sum + L[i][j]*y[j];
    }
    y[i] = (b[i]-sum)/L[i][i];
  }
  //for(i=0;i<n;i++) cout<<y[i]<<'\t';
  //cout<<endl<<endl;;
  
  // second, find the x vector
  x[n-1] = y[n-1];
  for(i=1;i<n;i++) {
    j = n-i-1;
    sum = 0;
    for(k=j+1;k<n;k++){ 
    sum = sum + U[j][k]*x[k];
    }
    x[j] = y[j] - sum;
  }
      ///////////////////////////////////////////////

   
   for(i=0;i<n;i++)
   { 
    cout<<"Weights: "<<x[i]<<","<<'\t';
    cout<<endl;
    data_out<<"Weights: "<<x[i]<<","<<'\t';
    data_out<<endl;
   }

}

