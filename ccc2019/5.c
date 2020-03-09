#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main()
{
    char *buf = NULL;
    int size;
    size_t length;
    char * pch;
    int count=0,i,j,N,K;
     
    size = getline(&buf, &length, stdin);
    pch = strtok (buf," ,.-");
    count=0;
    while (pch != NULL)
    {
        if(count==0){
            N=atoi(pch);  
        }
        else{
            K=atoi(pch);
        }
        pch = strtok (NULL, " ,.-");
        count++;
    }
    /*printf("%d,%d\n", N,K);*/
   
    int (*a)[N] = malloc(sizeof(int[N][N]));

    for (i=0;i<N;i++){
        count=0;
        j=0;
        size = getline(&buf, &length, stdin);
        pch = strtok (buf," ,.-");
        while (pch != NULL)
        {  
            a[i][j++]=atoi(pch);
            pch = strtok (NULL, " ,.-");
            count++;
        }
    }
	
	int max = 0;
	
	int row, col = 0;
	for (row=0; row < N-K+1; row++){
		for (col=0; col<row+1; col++){
			int temp = 0;
			i, j = 0;
			for (i=0;i<K;i++){
				for (j=0;j<i+1;j++){
					if (a[i + row][j + col]>temp){
						temp = a[i+row][j+col];
					}		
				}
			}
			/*printf("%d\n", temp);*/
			max += temp;
		}
	}
	
	printf("%d", max);
	
    return 0;
}