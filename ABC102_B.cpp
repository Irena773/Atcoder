#include <bits/stdc++.h>
#include <iostream>
using namespace std;


int main(){

int N;
cin >> N;

int A[N];
for(int i = 0; i < N; i++)  cin >> A[i];


int min = A[0], max = A[0]; 
for(int i=1; i < N; i++){
    if(min > A[i])min = A[i];
    if(max < A[i])max = A[i];
}

cout << max - min << endl;
}