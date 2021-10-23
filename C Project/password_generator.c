/*

	Credit :
		2502004405 - Dimas Syauqi Syafa (Computer Science)
	
	Program :
		Password Generator -> Saved at file pass.txt
		
*/
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void randomPassword(int Length){
	int index = 0;
	int randomizer = 0;
	FILE *file;

	srand((unsigned int)(time(NULL)));

	char numbers[] = "0123456789";
	char letters[] = "abcdefghijklmnopqrstuvwxyz";
	char LETTERS[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	char symbols[] = "!@#$^&*?";
	char password[Length];

	file = fopen("ppaasswwoorrdd.txt", "wb+");
	if(file == NULL){
		system("fsutil file createnew ppaasswwoorrdd.txt 9999");
		file = fopen("ppaasswwoorrdd.txt", "w");
	}
	fprintf(file, "Password : ");
	
	randomizer = rand() % 4;
    printf(" $ Password : ");
	
	for(index=0; index<Length; index++){
		if(randomizer == 1){
			password[index] = numbers[rand() % 10];
			randomizer = rand() % 4;
			printf("%c", password[index]);
		}
		else if (randomizer == 2) {
            password[index] = symbols[rand() % 8];
            randomizer = rand() % 4;
            printf("%c", password[index]);
        }
        else if (randomizer == 3) {
            password[index] = LETTERS[rand() % 26];
            randomizer = rand() % 4;
            printf("%c", password[index]);
        }
        else {
            password[index] = letters[rand() % 26];
            randomizer = rand() % 4;
            printf("%c", password[index]);
        }
        fprintf(file, "%c",password[index]);
	}
	fprintf(file, "%c",password[index]);
	fclose(file);
	printf("\n");
	printf(" $ Data berhasil disimpan di : ppaasswwoorrdd.txt");
	printf("\n");
}

int main(){
	int Length;

    printf("\n $ Input Length Password : ");
    scanf("%d",&Length);

	randomPassword(Length);
	
	printf("\n");
	printf(" $ Press any key to exit");
	system("pause > 1");
	printf("\n");

	return 0;
}
