#include <iostream>
using namespace std;
 
int main() {
	// your code goes here
	int n;
	cin>>n;
	int a[n],b[n];
	for(int i=0;i<n;i++){
	    cin>>a[i];
	}
	for(int i=0;i<n;i++){
	    b[a[i]-1]=i+1;
	}
	for(int i=0;i<n;i++){
	    cout<<b[i]<<" ";
	}
	cout<<"\n";
	return 0;
}
