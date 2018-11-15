#include <iostream>
#include <vector>

using namespace std;

int main()
{
	vector<int> a = vector<int>(1, 10);
	vector<int> b = a;
	
	cout << a[0] << " " << b[0] << endl;
	
	b[0] = 76;
	
	cout << a[0] << " " << b[0] << endl;
	
	return 0;
}
