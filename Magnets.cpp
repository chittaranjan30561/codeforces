#include <iostream>
using namespace std;
 
int main() {
	// your code goes here
	int n;
	cin>>n;
	int ans=1;
	string prev;
	cin>>prev;
	string cur;
	for(int i=1;i<n;i++){
	    cin>>cur;
	    //cout<<cur<<" \n";
	    if(prev[1]==cur[0]){
	        ans++;
	    }
	    prev=cur;
	}
	
	cout<<ans<<"\n";
	return 0;
}
