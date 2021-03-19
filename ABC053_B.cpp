#include <iostream>
#include <string>

using namespace std;

int main(){

    string s;
    cin >> s;
    string res;
    
    int head = 0, last = 0;
    for(int i = 0; i < s.size(); i++){
        if(s[i] == 'A'){
            head = i;
            break;
        }
    }

    for(int i = s.size()-1; i > 0; i--){
        if(s[i] == 'Z'){
            last = i;
            break;
        }
    }

    cout << last - head + 1 << endl;
}