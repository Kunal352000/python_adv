#include<stdio.h>
#include<string.h>
void main()
{
	int flag=0;
	char s1[10];
	scanf("%s",s1);
	char s2[32][10]={"if","else","switch","case","default","break","int","float","char","double",
	"long","for","while","do","goto","void","return","continue","enum","sizeof","union",
	"volatile","struct","typedef","auto","signed","const","extern","register","unsigned"};
	int i,j;
	if(((s1[0]>='a') && (s1[0]<='z')) || ((s1[0]>='A') && (s1[0]<='Z')) || (s1[0]=='_'))
	{
		for(i=1;i<strlen(s1);i++)
		{
			if(((s1[i]>='a') && (s1[i]<='z')) || ((s1[i]>='A') && (s1[i]<='Z')) || 
			((s1[i]>='0') && (s1[i]<='9')) || ((s1[i])=='_'))
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
