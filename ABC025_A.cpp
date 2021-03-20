#include <bits/stdc++.h>
using namespace std;

long long N;

long long calc(int N){

    int res = 0;
    while(N > 0){
        res += N % 10;
        N /= 10;
    }

    return res;
}
int main(){

   cin >> N;
   //大きな値で初期化
   long long res = 1LL << 60;
   for(long long A = 1; A < N; A++){
       long long B = N - A;
       long long tmp = calc(A) + calc(B);

       res = min(res, tmp);
   }

   cout << res << endl;
}