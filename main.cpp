#include<iostream>
#include<vector>
#include<string>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

int main(int argc,char* argv[]) {
  if(argc != 2) return -1;

  char opecode[] = "><+-.,[]";
  //string opecode = "CHRISTMA";
  
  long mem[10000];
  long pointer = 0;
	
  string program(argv[1]);

  for(auto it = program.begin();it != program.end();it++) {
    if(*it == opecode[0])
	pointer++;
    else if(*it == opecode[1])
	pointer--;
    else if(*it == opecode[2])
	mem[pointer]++;
    else if(*it == opecode[3])
	mem[pointer]--;
    else if(*it == opecode[4])
        printf("%c",mem[pointer]);
    else if(*it == opecode[5])
	scanf("%1c",mem + pointer);
    else if(*it == opecode[6])
	while(++it != program.end() && *it != opecode[7]);
    else if(*it == opecode[7])
	while(--it != program.begin() && *it != opecode[6]);
    else 
      printf("%c‚Í•s³‚È–½—ß‚Å‚·"
  }

  return 0;
}




