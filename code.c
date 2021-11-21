#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
/*
Author: Maryam Abu gneem , ID: 305173346
*/
void Third() 
{
	int first = -1;
	int second = -1;
	int third = -1;
	int num;
	printf("Please enter a positive value int: \n");
	scanf("%d", &num);
	while (num > 0) 
	{
		if (num > first) 
		{
			third = second;
			second = first;
			first = num;
		}

		else if (num > second) 
		{
			third = second;
			second = num;
		}
		else if (num > third) 
		{
			third = num;
		}
		printf("Please enter a positive value int: \n");
		scanf("%d", &num);
	}
	printf("first = %d\n", first);
	printf("second = %d\n", second);
	printf("third = %d\n", third);
}

void Primes(int num)
{

	for (int i = 2; i < num; i++) 
	{
		if (num % i == 0)//if the number can be devided without a reminder 
		{
			num = num / i;
			printf("%d*", i);
			i = 1;
            
		}

	}
	printf("%d\n", num);

}

int id(long num)
{
	int mull = 1;
	int sum = 0, i, res;
	if ((num > 9999999) && (num < 1000000000))
	{
		for (i = 0; i < 9; i++)
		{
			res = (mull) * (num % 10);
			if (mull == 1)
			{
				mull = 2;
			}
			else
			{
				mull = 1;
			}
			if (res > 9)
			{
				res = (res % 10) + (res / 10);
			}
			sum += res;
			num = num / 10;
		}
		if (sum % 10 == 0)
		{
			return 1;
		}
		else
		{
			return 0;
		}
	}
	else
	{
		return 0;
	}
}


void Diamond(int num) 
{
	for (int i = 0; i < num; i++) //לולאה לחילק העליון
	{
		for (int k = 0; k < num - i - 1; k++) //לולאה של הרווחם מחןץ 
		{
			printf(" ");
		}
		printf("/");
		for (int j = 0; j < 2* i  ; j++) //  לולאה הרווחים מבפנים המועין
		{
			printf(" ");
		}
		printf("\\");
		printf("\n");
	}

	for (int i = num; i > 0; i--) //לולאה לחילק התחתון
	{
		for (int k = 0 ; k < num - i ; k++)//רווחים מחוץ
		{
			printf(" ");
		}
		printf("\\");
		for (int j = 0; j < 2 * (i -1); j++)//רווחים מבפנים
		{
			printf(" ");
		}
		printf("/");
		printf("\n");
	}
	

}
// A function that calculates how many digits there are in a number פונקצית עזר
int NumOfDigits(int num) 
{
	if (num < 10)
		return 1;
	int digits = 0;
	while (num > 0) 
	{
		num = num / 10;
		digits++;
	}
	return digits;
}


long Compose(int num1, int num2) 
{
	long result;
	int digits = NumOfDigits(num2);
	for (int i = 1; i <= digits; i++) 
	{
		num1 = num1 * 10;
	}
	num1 += num2;
	result = num1;
	return result;
}




int main() 
{
	int num;
	int flag = 1;
	while (flag == 1)
	{
		printf("Please choose the number you want\n1 - Third\n2 - Primes\n3 - ID\n4 - Diamond\n5 - Compose\n6 - Quit\n");
		scanf("%d", &num);
		switch (num)
		{
		case 1:
		{
			Third();
			break;
		}
		case 2:
		{
			int n;
			printf("Please enter a positive number\n");
			scanf("%d", &n);
			printf("The number you entered is made from the primal numbers:\n");
			Primes(n);
			break;
		}
		case 3:
		{
			long ID;
			int isLegal;
			printf("Please enter you ID number\n");
			scanf("%ld", &ID);
			isLegal = id(ID);
			if (isLegal == 1)
				printf("Your id is legal\n");
			else
				printf("Your id is not legal\n");
			break;
		}

		case 4:
		{
			int n;
			printf("Please enter a number between 1 - 10\n");
			scanf("%d", &n);
			if (n <= 10 && n > 0)
				Diamond(n);
			else
				printf("The number is not good");
			break;

		}

		case 5:
		{
			int num1, num2;
			long result;
			printf("Please enter num1:\n");
			scanf("%d", &num1);
			printf("Please enter num2:\n");
			scanf("%d", &num2);
			result = Compose(num1, num2);
			printf("The composed number is: %ld", result);
			printf("\n");
			break;
		}
		case 6:
		{
			printf("Goodbay\n");
			flag = 0;
			break;
		}

		default:
			printf("The number isnt in the valid range,please try again\n\n");
			break;
		}

	}

	return 0;
}