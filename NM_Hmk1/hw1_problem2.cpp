// hw1_problem2.cpp
// 
//*****************
#include <iostream>
#include <fstream>
#include <math.h>
#include <time.h>
#include <iomanip>
using namespace std;
//*****************

// declaration of output stream

ofstream data_out("output.txt"); // output data

int main() {
	
    int i;
    float a,b,c,r1,r2,q,disc;
    
    a = 1.;
    b = 10.;
    c = 1.;
    
    data_out<<setprecision (6)<<endl;
    
    for(i=0;i<4;i++) {
	    
	    data_out<<"b = "<<b<<endl;
   
  		// method 1
   
    	disc = sqrt(b*b-4.*a*c);
    	r1 = (-1.*b + disc)/(2.*a);
    	r2 = (-1.*b - disc)/(2.*a);
   
    	data_out<<r1<<'\t'<<r2<<endl;
   
   		// method 2
   
    	r1 = 2.*c/(-1.*b + disc);
    	r2 = 2.*c/(-1.*b - disc);
   
    	data_out<<r1<<'\t'<<r2<<endl;
     
    	// method 3
   
    	q = -0.5*(b + fabs(b)/b*disc);
   
    	r1 = q/a;
    	r2 = c/q;
   
    	data_out<<r1<<'\t'<<r2<<endl<<endl;
    	
    	b = b*10.;
	}    
}	
