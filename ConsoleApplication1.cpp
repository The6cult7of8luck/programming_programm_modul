#include <iostream>
#include <string>

using namespace std;

int table() {
    string b(5, (char)205);

    cout << (char)201 << b << b << b << b << b << b << b << b << b << (char)187 << "\n\n";
    cout << (char)186 << "               Vremena goda                  " << (char)186 << "\n\n";
    cout << (char)204 << b << b << (char)205 << (char)203 << b << b << (char)203 << b << b << (char)203 << b << b << (char)205 << (char)185 << "\n\n";
    cout << (char)186 << "   Zima    " << (char)186 << "   Vesna  " << (char)186 << "   Leto   " << (char)186 << "   Osen    " << (char)186 << "\n\n";
    cout << (char)200 << b << b << (char)205 << (char)202 << b << b << (char)202 << b << b << (char)202 << b << b << (char)205 << (char)188 << "\n\n";;
    return 0;
}

int book() {
    cout << "Name       : \"The war and the peace\"\n";
    cout << "Avtor      : L.N. Tolstoj\n";
    cout << "Izdatelstvo: Piter\n";
    cout << "pages      : 500\n\n";
    return 0;
}

int dub() {
    cout << "\"U Lukomor\'a dub zelenij,\nZlataya zep na dube tom,\nI dnem i nochju kot echenij\nVse hodit po cepi krugom\"\n\n";
    return 0;
}

int main()
{
    cout << "Zadanie 1:\n\n";
    book();
    cout << "Zadanie 2:\n\n";
    dub();
    cout << "Zadanie 3:\n\n";
    table();
    return 0;

}
