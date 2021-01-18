#include <iostream>

using namespace std;

void printDecimal(int a, int b) {
    int iter = 0;
    while (a > 0) {
        // 첫 번째와 두 번째 사이에 소수점을 찍는다.
        if (iter++ == 1) cout << '.';
        cout << a / b << endl;
        a = (a % b) * 10;
        cout << "a: " << a << endl;
    }
}

int main() {
    int a, b;
    cin >> a >> b;
    printDecimal(a, b);
}