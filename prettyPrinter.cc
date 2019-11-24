#include <string>
#include <iostream>
#include <sstream>
using namespace std;

string makeIndent(int num) {
	string indent = "";
	for (int i = 0; i < num; ++i) {
		indent += " ";
	}
	return indent;
}

void prettyPrinter() {
	string indentS;
	string word;
	int newLineFlag = 0;
	int indent = 0;
	cin >> word;
	while (true) {
		if (word == ";") {
			if (newLineFlag == 1) {
				cout << indentS;
				newLineFlag = 0;
			}
			cout << ";" << endl;
			newLineFlag = 1;
			if (!(cin >> word)) break;
			indentS = makeIndent(indent);
		}
		else if (word == "{") {
			if (newLineFlag == 1) {
				cout << indentS;
				newLineFlag = 0;
			}
			cout << "{" << endl;
			newLineFlag = 1;
			++indent;
			if (!(cin >> word)) break;
			indentS = makeIndent(indent);
		}
		else if (word == "}") {
			--indent;
			indentS = makeIndent(indent);
			if (newLineFlag == 0) cout << endl;
			cout << indentS;
			cout << "}" << endl;
			newLineFlag = 1;
			if (!(cin >> word)) break;
			
		}
		else if (word == "//") {
			if (newLineFlag == 1) {
				cout << indentS;
				newLineFlag = 0;
			}
			cout << "//";
			getline(cin, word);
			cout << word << endl;
			newLineFlag = 1;
			if (!(cin >> word)) break;
			indentS = makeIndent(indent);
		}
		else {
			if (newLineFlag == 1) {
				cout << indentS;
				newLineFlag = 0;
			}
			cout << word;
			if (!(cin >> word)) break;
			if (word != "}") cout << " ";
		}
	}
}

int main() {
	prettyPrinter();
}

