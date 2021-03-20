#include <bits/stdc++.h>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){

    int N,x;//N人,x個のお菓子
    cin >> N >> x;
    vector<int> a(N);

    for(int i = 0; i < N; i++)cin >> a[i];

    sort(a.begin(), a.end());//小さい順にソート
   int sum = 0;
   int count = 0;

   for(int i = 0; i < N; i++){
       sum += a[i];
       if(sum <= x) count++;
       else break;
   }

   if(sum < x)count--;
   cout << count << endl;
}