// RK4.cpp
//
// This program implements a fourth-order Runge-Kutta algorithm to solve a single first-order ordinary differential equation 
//
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

double f1(double t, double x);	// the right hand side of the ODE dx/dt = f1(t,x)

// declaration of output stream

ofstream data_out("output.txt"); // output data

int main() {
	
	// variable declarations
    int i,j,k; // loop counters 
    
    double ttotal = 4.; // total time
    double delt = 0.1; // time step
    double t = 0.; // running time
    const int n = int(ttotal/delt); // number of points in discretization after initial value
    
    double k1, k2, k3, k4; // RK parameters
    
    double x10 = 1.; // initial condition
    double x1 = x10;
    
    data_out<<t<<'\t'<<x1<<endl; // initial condition
    
    for(i=1;i<=n;i++) {
	    
	    k1 = delt*f1(t,x1);
	    k2 = delt*f1(t + 0.5*delt, x1 + 0.5*k1);
	    k3 = delt*f1(t + 0.5*delt, x1 + 0.5*k2);
	    k4 = delt*f1(t + delt, x1 + k3);
	    
	    x1 = x1 + (k1 + 2.*k2 + 2.*k3 + k4)/6.;
	    t = t + delt;
	    
	    data_out<<t<<'\t'<<x1<<endl;	    
    }
}	
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
double f1(double t, double x) {
    double f;
    
    f = -2.*t - x;
     
  return f;
}
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
