#include <stdio.h>

#define LINESINFILE 1000
int main(void) 
{
	int left_num_found = 0;
	int numbers[LINESINFILE][3]; //array pro číslice a jejich kombinaci na řádku
	int linenum = 0; 
	char c;

	while ((c = getchar()) != EOF )
	{
		if (c == '\n')
		{
			left_num_found = 0;
			linenum++;
		}
		else if (c >= '0' && c <= '9')
		{
			if (left_num_found == 0)
			{
				left_num_found = 1;
				numbers[linenum][0] = c - '0';
			}
			if (left_num_found)
			{
				numbers[linenum][1] = c - '0';
			}

		}
	}	

	for (int i = 0; i < linenum; i++)
	{
		//combine numbers
		numbers[i][2] = numbers[i][0] * 10 + numbers[i][1] ;
	}

	int res = 0;
	//výsledek
	for (int i = 0; i < linenum; i++)
	{
		res += numbers[i][2];
	}
	printf("%d\n", res);

	//skládám to správně?
	// for (int i = 0; i < linenum; i++)
	// {
	// 	for (int j = 0; j < 3; j++)
	// 	{
	// 		printf("%d ", numbers[i][j]);
	// 	}
	// 	printf("\n");
	// }
}
