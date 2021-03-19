#include <iostream>

using namespace std;
int main(){

    int N;
    bool OK = false;
    cin >> N;
    for(int a = 0;a <= N / 4; a++){
        for(int b = 0; b <= N / 7; b++){
            int X = 4 * a + 7 *b;
            if(N == X){
                OK = true;
                
            }
        }
    }
        if(OK == false)cout << "No" << endl;
        else cout << "Yes" << endl;
    
}