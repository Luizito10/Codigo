#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#define N 256
#define L 5
//Ainda em processo de construção, porem com a base pronta!!
char transforma_minuscula(char palavra[L][N]);
int verifica_letras(char palavra[L][N]);
int verifica_repetida(char palavra[L][N]);
int main(){
	int teste = 1, i, j, pos=0, l=5, n=256;
	char palavra[L][N];
	char ordem[L][N];
	while(teste == 1)
    {
        teste = 0;
        system("cls");
        for (i=0;i<L;i++)
        {
            printf("Informe a palavra %d: ", i+1);
            fgets(palavra[i],N,stdin);
            palavra[i][strlen(palavra[i])-1]='\0';
        }
        transforma_minuscula(palavra);
        if(verifica_letras(palavra)==1)
            teste = 1;
        if(verifica_repetida(palavra)==1)
            teste = 1;
	}
	for (i=0;i<L;i++){
		pos=0;
		for(j=0;j<L;j++)
			if(strcmp(palavra[i],palavra[j])==1)
			pos++;
		strcpy(ordem[pos],palavra[i]);
	}
	for(i = 0; i < L; i++)
    printf("\n------------------\n%s", ordem[i]);
    printf("\n------------------\n");
	return 0;
}

char transforma_minuscula(char palavra[L][N])
{
    int i, j;
    for (i = 0; i < L; i++)
        for(j = 0 ; j <strlen(palavra[i]); j++)
            palavra[i][j] = tolower(palavra[i][j]);
    return palavra;
}
int verifica_letras(char palavra[L][N])
{
    int i=0, j;
    for (i = 0; i < L; i++)
        for(j = 0 ; j <strlen(palavra[i]); j++)
            if(isalpha(palavra[i][j])==0)
            {
                printf("\n==================================================================");
                printf("\nDesculpe-me, mas insira palavras contendo apenas letras por favor!");
                printf("\n==================================================================");
                getchar();
                return 1;
            }
    return 0;
}

int verifica_repetida(char palavra[L][N])
{
    int i, j=1;
    for(i=0; i<L; i++)
        for(j=i+1;j<L;j++)
            if(strcmp(palavra[i],palavra[j])==0)
            {
                printf("\n=======================================================");
                printf("\nDesculpe-me, mas insira palavras diferentes por favor!");
                printf("\n=======================================================");
                getchar();
                return 1;
            }
    return 0;
}
