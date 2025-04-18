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
ofstream data_out("C:/Users/rdesa/output_hmk5_prob1d.txt"); // output data
// the main part of the program - should always be type "int"

int main() {
	// variable declarations
    int i,j,k,l; // loop counters 
    const int n = 2; // number of points in discretization
    //double Tleft = 0.; // left boundary condition
    //double Tright = 1.;// right boundary condition
    //double length = 2; // length of system
    //double tcond = 1.; // thermal conductivity
    //double dx = length/(double(n)-1.); // discretization length
    //double T[] = {25,30,35,40,45,50,60,70,80,90,100,150,200,250,273,300,350,400,450,500,600,700};
    //double K[] = {459.5,317.7,233.3,180.3,143.2,118.4,85.2,66.6,54.4,46.1,40.2,23.3,16.5,12.6,11.5,10.5,8.8,7.6,6.9,6.1,5.1,4.5};
    //const int N = 22;
    //double Ybar = 0.;
    //double Yi_Ybar_2 = 0.;
    //double sumy = 0.;
    double A[n][n]; // coefficient matrix
    double L[n][n]; // lower triangular matrix
    double U[n][n]; // upper triangular matrix
    double x[n]; // solution vector
    double y[n]; // intermediate solution vector
    //double b[n]; // right side vector
    //double sum_xall[] = {0.,0.,0.,0.,0.};
    //double sum_xyall[] = {0.,0.,0.};
    double sum; // dummy variable to keep track of sums in decomposition

    //for(i=0;i<N;i++){
    //  sumy = sumy + K[i];
    //}
    //Ybar = sumy/N;

    //for(i=0;i<N;i++){
    //  Yi_Ybar_2 = Yi_Ybar_2 + (pow((K[i]-Ybar),2.));
    //}

    

	// coefficient matrix for conduction problem (you could enter or read in any square matrix of size n)
	
    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////// Change based on problem
    //for(i=0;i<n;i++) {
	//	  for(j=0;j<n;j++) A[i][j] = 0.;
	//}
  
  //A[0][0]
  //sum_xall[0] = N;
  //b[0]
  //sum_xyall[0] = sumy;
  //double tot_x = 0;
  //double tot_xy = 0;

  //for(i=1;i<5;i++){
  //  tot_x = 0.;
  //  tot_xy = 0.;
  //  for (j=0;j<N;j++){
  //    tot_x = tot_x + pow(T[j],i);
  //    if (i<=2){
  //    tot_xy = tot_xy + (pow(T[j],i))*K[j];
  //    }
  //  }   
  //  sum_xall[i] = tot_x;
  //  if (i<3){
  //  sum_xyall[i] = tot_xy;
  //  }
  //}

  //for(k=0;k<n;k++){
  //  b[k] = sum_xyall[k];
  //  for(l=0;(l<n);l++){
  //    A[k][l] = sum_xall[k+l];
  //  }
 // }

 A[0][0] = 1;
 A[0][1] = 1;
 A[1][0] = -0.57735;
 A[1][1] = 0.57735;
 double b[] = {2,0};
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

  ///x[i] should be coeffients

  //double K_at_T_list[22];
  
  //for(i=0;i<N;i++){
   // double K_at_T = 0;
   // for (j=0;j<n;j++){
    //    K_at_T = K_at_T + x[j]*pow(T[i],j);
    //}
  //K_at_T_list[i] = K_at_T;
 // }

 // double ks_diff = 0;
 // for(i=0;i<N;i++){
 //   ks_diff = ks_diff + pow((K[i]-K_at_T_list[i]),2);
 // }
  //double R = 0;
  //R = 1 - ks_diff/Yi_Ybar_2;
   
   for(i=0;i<n;i++)
   { 
    cout<<"Weights: "<<x[i]<<","<<'\t';
    cout<<endl;
  //  data_out<<"Coefficient: "<<x[i]<<","<<'\t';
    data_out<<endl;
   }

  // cout<<"R^2 Value: "<<R<<endl;
  // data_out<<"R^2 Value: "<<R<<endl;
   
  // for(i=0;i<N;i++) { 
  //  data_out<<K_at_T_list[i]<<","<<endl;
  //  }
  // cout<<endl;

}

