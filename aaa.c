#include<stdio.h>
#include<string.h>
void main()
{
	int flag=0;
	char a1[10];
	scanf("%s",a1);
	char a2[32][10]={"if","else","switch","case","default","break","int","float","char","double",
	"long","for","while","do","goto","void","return","continue","enum","sizeof","union",
	"volatile","struct","typedef","auto","signed","const","extern","register","unsigned"};
	int i,j;
	if(((a1[0]>='a') && (a1[0]<='z')) || ((a1[0]>='A') && (a1[0]<='Z')) || (a1[0]=='_'))
	{
		for( i=1;i<strlen(a1);i++)
		{
			if(((a1[i]>='a') && (a1[i]<='z')) || ((a1[i]>='A') && (a1[i]<='Z')) || 
			((a1[i]>='0') && (a1[i]<='9')) || ((a1[i])=='_'))
			{
			}
			else
			{
					flag=1;
					break;
			}
		}
		for(j=0;j<32;j++)
		{
			if(strcmp(a1,a2[j])==0)
			{
				flag=1;
				break;
			}
		}
		if(flag==0)
		{
			printf("Valid Identifier");
		}
		else
		{
			printf("Invalid Identifier");
		}
	}
	else
	{
		printf("Invalid Identifier");
	}
}
