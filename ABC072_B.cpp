#include <iostream>
#include <string>
using namespace std;

int main(){

    string s;
    cin >> s;
    string ans;

    for(int i = 0; i < s.size(); i+=2){
        //奇数文字目だけ抜き出す
        if(i % 2 == 0) ans += s[i];
    }

    cout << s << endl;

}