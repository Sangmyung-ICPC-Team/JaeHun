#include <stdio.h>
#include <string.h>

int main(void)
{
	char arr[1000001], *token;
	int cnt;

	gets(arr);

	token = strtok(arr, " ");

	cnt = 0;
	while (token != NULL)
	{
		cnt++;
		token = strtok(NULL, " ");
	}

	printf("%d\n", cnt);
	return 0;
}
