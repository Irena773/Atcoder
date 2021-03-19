#include <bits/stdc++.h>
#include <algorithm>
using namespace std;

int main(){

    int N,T,A;
    cin >> N >> T >> A;

    int index = 0;
    int r = 0;

    for(int i = 1; i <= N; i++){

        int x;
        cin >> x; 
        x = abs(A * 1000 - (T * 1000 - x * 6));
        if(x < r || i == 1){
            r = x;
            index = i;
        }

    }
    cout << index  << endl;
}