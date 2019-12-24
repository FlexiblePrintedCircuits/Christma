#include<iostream>
#include<iterator>
#include<fstream>
#include<vector>
#include<string>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

int main(int argc,char* argv[]) {
  if (argc > 2) return -1;

  string file_name = "tree.bf";

  //コマンドライン引数からファイル名を取得  
  if (argc == 2) {
    string file_name = argv[1];
    string program(argv[1]);
  }

  std::ifstream ifs(file_name);

  std::istreambuf_iterator<char> it(ifs);
  std::istreambuf_iterator<char> last;
  std::string str(it, last);

  // ファイルが正常に開かなかった時の例外処理
  if (ifs.fail()) {
      std::cerr << "ERROR: not found file." << std::endl;
      return -1;
  }

  string::iterator ptr;

  char opecode[] = "><+-.,[]";
  //string opecode = "CHRISTMA";
  
  char mem[10000] = {0};
  long pointer = 0;
  
  for(ptr = str.begin(); ptr != str.end(); ptr++){
    if(*ptr == opecode[0])
	    pointer++;
    else if(*ptr == opecode[1])
	    pointer--;
    else if(*ptr == opecode[2])
	    mem[pointer]++;
    else if(*ptr == opecode[3])
	    mem[pointer]--;
    else if(*ptr == opecode[4])
        printf("%c",mem[pointer]);
    else if(*ptr == opecode[5])
	    scanf("%1c",mem + pointer);
    else if(*ptr == opecode[6] && mem[pointer] == 0) {
        while(++ptr != str.end() && *ptr != opecode[7]);
    }
    else if(*ptr == opecode[7] && mem[pointer] != 0) {
	    while(--ptr != str.begin() && *ptr != opecode[6]);
	    //ptr++;
    }
    else if(*ptr == 'A')
        printf("?");
    else 
      // printf("%c�͕s���Ȗ��߂ł�");
      continue;
  }

  return 0;
}




