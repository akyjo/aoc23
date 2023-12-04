#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//magic macros
#define LINESINFILE 1000
#define NINEDIGITS 9

//strucc
typedef struct {
	char *key;
	int numeral;
} NumeralMap;

typedef struct {
	int leftmost_index;
	int leftmost;
	int rightmost_index;
	int rightmost;
} DigitsAndPosition;

//prototypes
DigitsAndPosition FindOutermostDigits(char* line);
int FindLeftmostDigit(char* line, NumeralMap map[]);
int FindRightmostDigit(char* line, NumeralMap map[]);
int CharToNum(char*);
int CmpCharAtAddress(char* line, char* map);

int main() 
{
	FILE *file;
	char line[100];

	int left_num_found = 0;
	int numbers[LINESINFILE][5]; //array pro číslice, indexy číslic a jejich kombinaci na řádku
	int linenum = 0; 
	char c;

	NumeralMap numeral_map[] = {
		{"one", 1},
		{"two", 2},
		{"three", 3},
		{"four", 4},
		{"five", 5},
		{"six", 6},
		{"seven", 7},
		{"eight", 8},
		{"nine", 9}
	};

	errno_t error_code;
	error_code = fopen_s(&file, "data_day1.txt", "r");
	if (error_code != 0)
	{
		perror("cant open file bla bla");
		return -1;
	}
	// DigitsAndPosition outermost;
	while (fgets(line, sizeof(line), file))
	{
		//iterate over line
		// outermost = FindOutermostDigits(line);
		numbers[linenum][0] = FindLeftmostDigit(line, numeral_map);
		numbers[linenum][1] = FindRightmostDigit(line, numeral_map);
		linenum++;

		//check for leftmost and rightmost digit
		//scan for leftmost and rightmost match from numeralmap
		//find out which are at the "edge"
	}
	fclose(file);
	// while ((c = getchar()) != EOF )
	//
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
	// for (int i = 0; i < linenum; i++)
	// {
	// 	for (int j = 0; j < 3; j++)
	// 	{
	// 		printf("%d ", numbers[i][j]);
	// 	}
	// 	printf("\n");
	// }
}

DigitsAndPosition FindOutermostDigits(char* line)
{
	int left_num_found = 0;
	DigitsAndPosition digits_and_positions;
	for (int i = 0; line[i] != '\0'; i++)
	{
		if (line[i] >= '0' && line[i] <= '9')
		{
			if (left_num_found == 0)
			{
				left_num_found = 1;
				digits_and_positions.leftmost = line[i] - '0';
				digits_and_positions.leftmost_index = i;
			}
			if (left_num_found)
			{
				digits_and_positions.rightmost = line[i] - '0';
				digits_and_positions.rightmost_index = i;
			}

		}
	}
	return digits_and_positions;
}	

int FindLeftmostDigit(char* line, NumeralMap map[])
{

	char* p1 = line;
	int charNumeric;

	for(int i = 0; i < strlen(line); i++)
	{
		charNumeric = CharToNum(p1);
		if (charNumeric > 0)
		{
			return charNumeric;
		}
		for (int j = 0; j < NINEDIGITS; j++)
		{
			if (CmpCharAtAddress(p1, map[j].key))
			{
				return map[j].numeral;
			}
		}
		p1++;
	}
	return 0;
}
int FindRightmostDigit(char* line, NumeralMap map[])
{
	char* p1 = line + strlen(line) - 1;
	int charNumeric;

	for(int i = strlen(line); i >= 0; i--)
	{
		charNumeric = CharToNum(p1);
		if (charNumeric > 0)
		{
			return charNumeric;
		}
		for (int j = 0; j < NINEDIGITS; j++)
		{
			if (CmpCharAtAddress(p1, map[j].key))
			{
				return map[j].numeral;
			}
		}
		p1--;
	}
	return 0;
}
//vrací 1 nebo 0 podle toho jestli se char na adrese rovná
int CmpCharAtAddress(char* line, char* map)
{
	int i=0,j=0;
	char* p3;
	char* posInMap = map;

	for(j = 0; j < strlen(map); j++)
	{
		if(*line == *posInMap)
		{
			line++;
			posInMap++;
		} 
		else
		return 0;
	}
	return 1;
}
int CharToNum(char* chachar)
{
	if (*chachar >= '1' && *chachar <= '9')
	{
		return *chachar - '0';
	}
	else 
	{
		return 0;
	}
}
