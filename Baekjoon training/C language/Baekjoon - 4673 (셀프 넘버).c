#include <stdio.h>

int selfnumber(int num)
{
	int result = num;
	while (num > 0)
	{
		if (num == 0)
			break;
		result += num % 10;
		num /= 10;
	}
	return result;
}

int main(void)
{
	int arr[10001] = { 0, };

	for (int i = 1; i < 10001; i++)
	{
		int temp;
		temp = selfnumber(i);
		if (temp < 10001)
			arr[temp] = 1;
	}

	for (int i = 1; i < 10001; i++)
	{
		if (arr[i] != 1)
			printf("%d\n", i);
	}
	return 0;
}
