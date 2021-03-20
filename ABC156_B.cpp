#include <bits/stdc++.h>
using namespace std;

int main(){
    long long N;
    int K;
    cin >> N >> K;

    
    int count = 1;
    while(N > 0){
        if(N / K != 0){
            count++;
        }
        N /= K;
    }

    cout << count << endl;
}