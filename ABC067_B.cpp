#include <iostream>
#include <algorithm>

using namespace std;

int main(){


    int N,K;//N本の棒,K本の棒を選ぶ
    cin >> N >> K;
    int l[N];

    for(int i = 0; i < N; i++){
        cin >> l[i];
    }

    sort(l, l+N, greater<int>());//大きい順にソート
    int ans = 0;
    for(int i=0; i < K; i++){
        ans += l[i];
    }

    cout << ans << endl;
}