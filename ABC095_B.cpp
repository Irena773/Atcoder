#include <iostream>

using namespace std;

int main(){
    int N, X;//N種類,Xグラム
    cin >> N >> X;

    int m[110];

    int S = 0;//m1,m2...mNの和
    int M = 1001001001;//m1,m2...mNのうち最小の値
    for(int i = 0; i < N; i++){
        cin >> m[i];
        S += m[i];
        if(m[i] < M ){
            M = m[i];
        }
    }
        int ans = N + (X - S) / M;
        cout << ans << endl;
}