#include <iostream>

using namespace std;

int main(){

    int N;
    bool OK = false;
    cin >> N;
    for(int a = 1; a <= 9; a++){
        for(int b = 1; b <= 9; b++){
            if(N == a * b){
                OK = true;
            }
        }
    }

    if(OK == true)cout << "Yes" << endl;
    else cout << "No" << endl;
}