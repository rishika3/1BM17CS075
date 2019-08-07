#include <iostream>
using namespace std;
int main(){
   
   int i,n,largest;
   cout<<"Enter number of elements you want to enter: ";
   cin>>n;
   int a[n];
   cout<<"Enter Elements ";
     for(i = 0; i < n; i++) {
      cin>>a[i];
}
   largest= a[0];
   for(i = 1;i < n; i++) {
     
      if(largest < a[i])
         largest = a[i];
   } 
   cout<<"Largest element in array is: "<<largest;
   return 0;
}