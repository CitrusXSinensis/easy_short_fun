#include <string>
#include <sstream>
#include <fstream>
#include <iostream>
using namespace std;

void getLines(int lineNum, int skipNum, string file) {
	ifstream fin{ file };
	string currentLine;
	for (int i = 0; i < skipNum; ++i) {
		if (!getline(fin, currentLine)) {
			break;
		}
	}
	for (int j = 0; j < lineNum; ++j) {
		if (!getline(fin, currentLine)) {
			break;
		}
		cout << currentLine << endl;
	}
}

int main(int argc, char *argv[]) {
	int lineNum = 10;
	int skipNum = 0;
	int argIndex1 = -1;
	int argIndex2 = -1;
	int fileNum = 0;
	int last = 0;
    for (int i = 1; i < argc; ++i) {
		if (string(argv[i]) == "-n") {
			istringstream iss{ argv[i + 1] };
			iss >> lineNum;
			argIndex1 = i;
			--fileNum;
		}
		else if (string(argv[i]) == "-s") {
			istringstream iss{ argv[i + 1] };
			iss >> skipNum;
			argIndex2 = i;
			--fileNum;
		}
		else {
			last = i;
			++fileNum;
		}
    }
	if (fileNum == 0) {
		string currentLine;
		for (int i = 0; i < skipNum; ++i) {
			if (!getline(cin, currentLine)) {
				break;
			}
		}
		for (int j = 0; j < lineNum; ++j) {
			if (!getline(cin, currentLine)) {
				break;
			}
			cout << currentLine << endl;
		}
	}
	for (int j = 1; j < argc; ++j) {
		if ((j != argIndex1) && (j != argIndex2) && (j != (argIndex1 + 1)) && (j != (argIndex2 + 1))) {
			if (fileNum != 1) {
				cout << "==> " << argv[j] << " <==" << endl;
			}
			getLines(lineNum, skipNum, argv[j]);
			if (j != last) {
				cout << endl;
			}
		}
	}
}

