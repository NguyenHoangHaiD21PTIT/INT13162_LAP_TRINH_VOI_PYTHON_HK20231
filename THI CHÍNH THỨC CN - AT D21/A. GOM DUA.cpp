#include<bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        long long a = 0, b = 0;//số số 1, số số 2
        while(n--){
            int x; cin>>x;
            if(x==1) a++;
            else if (x==2) b++;
            else {
                b++;
                a+=x-2;
            }
        }
        cout<<a/2+b/2<<endl;
    }
}
