#include <stdio.h>

int main(void)
{
	char arr[1000001];
	int i = 0;

	while (1)
	{
		scanf("%c", &arr[i]);
		
		if (arr[i] == '\n')
			break;
		i++;
	}

	int j = 0;
	int move_1 = 0;
	int move_2 = 0;

	while (1)
	{
		if (arr[j] == '0')
		{
			while (arr[j + 1] == '0')
				j++;
			move_1 += 1;
			j++;
		}
		else if (arr[j] == '1')
		{
			while (arr[j + 1] == '1')
				j++;
			move_2 += 1;
			j++;
		}
		if (arr[j] == '\n')
			break;
	}
	int min;

	if (move_1 > move_2)
		min = move_2;
	else
		min = move_1;
	
	printf("%d\n", min);
	return 0;
}
