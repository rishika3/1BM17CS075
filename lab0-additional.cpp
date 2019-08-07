#include<iostream>
#include<conio.h>
using namespace std;
int main()
{
	int i, num, n, c=0, pos;
	cout<<"Enter the array1 size : ";
	cin>>n;
	int arr[n];
	cout<<"Enter Array1 Elements : ";
	for(i=0; i<n; i++)
	{
		cin>>arr[i];
	}
	cout<<"Enter the number to be search : ";
	cin>>num;
	for(i=0; i<n; i++)
	{
		if(arr[i]==num)
		{
			c=1;
			pos=i+1;
			break;
		}
	}
	if(c==0)
	{
		cout<<-1;
	}
	else
	{
		cout<<1<<endl;
	}

	cout<<"Enter the array2 size : ";
	cin>>n;
	cout<<"Enter Array2 Elements : ";
	for(i=0; i<n; i++)
	{
		cin>>arr[i];
	}
	cout<<"Enter the number to be search : ";
	cin>>num;
	for(i=0; i<n; i++)
	{
		if(arr[i]==num)
		{
			c=1;
			pos=i+1;
			break;
		}
	}
	if(c==0)
	{
		cout<<-1;
	}
	else
	{
		cout<<1<<endl;
	}
	getch();
}
